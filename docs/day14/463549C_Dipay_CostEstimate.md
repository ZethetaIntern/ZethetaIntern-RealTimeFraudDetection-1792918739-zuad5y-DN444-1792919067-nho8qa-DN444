# Cost estimate (Cost Optimizer)

Assumptions: AWS ap-south-1, 50k TPS peak, 2.4M txn/day (~28 TPS average — **design for peak breach/enumeration**, not average). Peak sizing used below with 40% headroom. Numbers are order-of-magnitude USD/month.

| Item | Estimate |
|---|---|
| EKS compute (m6i / c6i + ONNX c6i) | $38,000 |
| Kafka MSK 60 P | $9,000 |
| Aurora PG + Redis + Neo4j (incl replica) | $14,000 |
| ES + Grafana/AMP | $4,000 |
| NAT/transfer + enrichment API | $6,000 |
| DR warm Singapore 30% | $12,000 |
| **Total** | **~$83k / month** |

Cost per transaction at 2.4e6 * 30 ≈ 72M txn/month: **~$0.00115 / txn**.

Legacy colo + Oracle licences + fraud losses ₹53 cr/quarter (~$5M+/qtr at typical FX) dwarf infra. Target: return FPR to 0.5% and close 15-min gap → fraud losses toward ₹12 cr/qtr. Infra is < 5% of one quarter’s incremental fraud.

Build vs buy: device fingerprint **buy** (ThreatMetrix); graph **build** on Neo4j; rules **build** (issuer IP).
