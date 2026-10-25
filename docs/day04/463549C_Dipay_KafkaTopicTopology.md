# Kafka topic topology

Naming: `domain.entity.action`. Production RF=3, min.insync.replicas=2. Dev RF=1.

Partition count ≈ ceil(peak_TPS / desired_per_partition_TPS). Peak 50k TPS, ~1k TPS/partition → **60 partitions** on transaction topics.

Keying: `card_number_hash` on transaction-like topics so a card is totally ordered on one partition.

| Topic | Partitions | RF | Retention | Key | Consumers (group) |
|---|---|---|---|---|---|
| `transactions.raw` | 60 | 3 | 30d | card_hash | enrichment (`cg-enrich`) |
| `transactions.enriched` | 60 | 3 | 30d | card_hash | scoring orchestrator, graph-sync, feature-stream (`cg-score`, `cg-graph`, `cg-feat`) |
| `fraud.alerts` | 24 | 3 | 90d | card_hash | case-mgmt, alert-correlation, notify |
| `fraud.decisions` | 60 | 3 | 90d | card_hash | notify, audit, CQRS, case |
| `audit.events` | 24 | 3 | **infinite** | resource_id | audit-compliance, regulator export |
| `notifications.outbound` | 12 | 3 | 7d | customer_hash | notification workers |
| `graph.updates` | 24 | 3 | 14d | entity_id | graph-analysis writer |
| `integrity.switch_cbs` | 12 | 3 | 30d | terminal_id | integrity-monitor |
| `fraud.dlq` | 12 | 3 | 30d | original_topic | replay tool |
| `model.shadow_scores` | 12 | 3 | 14d | card_hash | champion-challenger logger |

Plus compact topics: `cqrs.fraud_stats`, `cqrs.geo_heatmap` (changelog).

## Consumer notes

- Scoring **may** also be invoked synchronously from ingestion for network-auth; Kafka is still produced for replay and CQRS.
- Idempotent producers, transactional outbox on ingestion.
- Exactly-once is **not** claimed end-to-end; consumers are idempotent on `transaction_id`.
