# Five-tier rate limiting

Counters in Redis `INCR` + TTL. Headers: `X-RateLimit-Limit`, `Remaining`, `Reset`.

| Tier | Default | Purpose |
|---|---|---|
| Per-merchant | Contract TPS (1000 large acquirer, 100 small) | Enumeration from a single MID |
| Per-IP | 50 req/min | Distributed scripted attacks |
| Per-endpoint | POST /transactions tighter than GET /dashboard | Protect hot path |
| Global | 50,000 TPS | Cluster ceiling |
| Adaptive | If fraud rate > 5% for 5 min, merchant limit × 0.5 | Breach aftermath |

429 JSON `{code: RATE_LIMIT, message, trace_id}`.
