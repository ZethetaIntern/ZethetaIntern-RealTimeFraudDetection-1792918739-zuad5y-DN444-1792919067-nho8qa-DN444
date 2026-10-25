# Latency budget per hop (Latency Hunter)

Critical path for an authorisation, **parallel** detect after enrich.

Assumptions: in-region Mumbai, mTLS Envoy sidecar ~0.4 ms/hop, protobuf serdes ~0.3 ms, p99.

| Hop | Component | p99 estimate (ms) | Method |
|---|---|---|---|
| 1 | Kong TLS + JWT + schema | 4 | JWT RS256 cached JWKS |
| 2 | Envoy ingress → ingestion | 0.5 | mesh |
| 3 | Tokenise + persist outbox | 8 | PG primary same AZ |
| 4 | Kafka produce acks=all ISR=2 | 6 | local cluster |
| 5 | Enrich consume + Redis profile + vendor cache | 12 | vendors async; cache hit required on hot path |
| 6a | Rule evaluate + Redis windows | 25 | budget |
| 6b | ML ONNX + feature fetch | 10 | budget |
| 6c | Graph 2-hop lookup | 50 | budget; timeout 45 ms then fallback |
| 7 | Aggregate + explain + produce decision | 8 | |
| 8 | Gateway response | 2 | |

Hops 6a–6c **run concurrently**. Detection wait = max(25, 10, 50) + 2 ms merge = **52 ms** typical worst engine, with **100 ms combined SLA** leaving ~48 ms slack for GC and retries-disabled-on-hot-path.

End-to-end p99: 4+0.5+8+6+12+52+8+2 ≈ **92.5 ms** compute/IO + queueing. Headroom to **200 ms pipeline SLO** covers Kafka jitter and one enriched-cache miss.

If graph p99 threatens the 100 ms combined budget, **fail that signal** (fallback + safety margin +20 points) rather than retry. Retries are disabled on the authorisation path; they exist on Kafka consumers.
