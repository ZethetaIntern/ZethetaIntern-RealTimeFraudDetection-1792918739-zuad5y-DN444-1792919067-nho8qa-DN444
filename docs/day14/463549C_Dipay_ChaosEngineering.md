# Chaos experiments (5+)

| # | Experiment | Expected | Validate |
|---|---|---|---|
| 1 | Kill random rule-engine pod | HPA + remaining pods; p99 blip < SLO | Grafana replicas, no 5xx burst |
| 2 | Network partition scoring↔graph | Circuit open 10s; fallback +20 score; `degraded=true` | Jaeger, decisions degraded rate |
| 3 | +200 ms latency injection on ML | Timeout 20 ms; ensemble uses rules+graph only | ML timeout metric |
| 4 | Kill Kafka broker | Leader election; produce p99 spike then recover; no offset loss | ISR, lag |
| 5 | Trigger PG failover | App retries, RTO < 5 min Tier 1 | Probe success |
| 6 | Chaos Gorilla (AZ) | Mesh + PDB keep minAvailable | availability SLO |

Tooling: Chaos Mesh / Litmus on staging weekly; production game-day quarterly.
