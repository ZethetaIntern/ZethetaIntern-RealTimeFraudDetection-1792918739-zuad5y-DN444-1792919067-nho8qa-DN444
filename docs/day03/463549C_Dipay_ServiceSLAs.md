# Service SLA specification

Error-budget policy (all Tier-1): **freeze production deploys** for that service when the 30-day error budget is exhausted until the budget recovers or a P1 hotfix is approved by CTO + CRO.

| Service | p50 | p95 | p99 | Availability | Throughput | Error budget | Depends on |
|---|---|---|---|---|---|---|---|
| txn-ingestion | 8 ms | 20 ms | 30 ms | 99.99% | 50k TPS system, 5k/pod | 4.32 min/30d | Kafka produce acks=all |
| enrichment-profile | 12 ms | 25 ms | 40 ms | 99.99% | 50k TPS | same | Redis, reference-data cache |
| reference-data | 3 ms | 8 ms | 15 ms | 99.99% | cacheable | same | Postgres |
| rule-engine | 8 ms | 18 ms | **25 ms** | 99.99% | 50k TPS | same | Redis velocity |
| anomaly-detection | 4 ms | 8 ms | **10 ms** | 99.99% | 50k TPS | same | Redis features, ONNX |
| graph-analysis (hot path) | 15 ms | 35 ms | **50 ms** | 99.95% | 20k TPS lookup | 21.6 min/30d | Neo4j read replica |
| risk-scoring (orchestrate) | 40 ms | 80 ms | **100 ms** | 99.99% | 50k TPS | 4.32 min | rules+ML+graph in parallel |
| case-management | 80 ms | 200 ms | 400 ms | 99.9% | 200 TPS | 43 min | Postgres |
| notification | 50 ms accept | 200 ms | 500 ms | 99.9% | 5k TPS | 43 min | vendors |
| audit-compliance | 10 ms append | 30 ms | 50 ms | 99.99% | 50k TPS | 4.32 min | Kafka |
| alert-correlation | 20 ms | 50 ms | 80 ms | 99.9% | 1k TPS alerts | 43 min | Redis |
| integrity-monitor | 30 s reconcile | n/a | n/a | 99.9% | batch | 43 min | CBS logs, Timescale |
| dashboards / UI | 200 ms | 500 ms | 1 s | 99.9% | interactive | 43 min | CQRS views |

**Pipeline (authorisation):** p50 < 50 ms, p95 < 150 ms, **p99 < 200 ms** end-to-end including network to gateway.  
**Detection gRPC fan-out combined:** p99 **100 ms** (brief A1.4). See `463549C_Dipay_LatencyBudget.md`.

Other SLOs from the brief: detection rate > 95%; FPR < 0.5%; Kafka lag < 1000 msgs/partition; 5xx < 0.1% per service.
