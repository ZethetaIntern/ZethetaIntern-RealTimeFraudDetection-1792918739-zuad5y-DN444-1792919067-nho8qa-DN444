# Service decomposition table

Target: 8–12 independently deployable services. Aegis uses **12**.

| Service | Context | Responsibility | Language / framework | Datastore | Team |
|---|---|---|---|---|---|
| `txn-ingestion` | Transaction Ingestion | Normalise channels, tokenise PAN, produce Kafka | Go, gRPC + REST | PostgreSQL | Payments Edge (4) |
| `enrichment-profile` | Customer Profile | Enrich + maintain behavioural profile | Java 21 / Spring | PostgreSQL, Redis | Identity (4) |
| `reference-data` | Reference Data | BIN, MCC, watchlists, FX, holidays | Go | PostgreSQL | Data Ops (3) |
| `rule-engine` | Fraud Analysis | Evaluate versioned YAML rules | Java 21 | PostgreSQL, Redis cache | Detection Rules (5) |
| `anomaly-detection` | Fraud Analysis | ML inference + ensemble | Python 3.11 / FastAPI + ONNX Runtime | Redis (features), MLflow metadata in PG | ML Platform (5) |
| `graph-analysis` | Fraud Analysis | Relationship queries | Kotlin / Java + Neo4j driver | Neo4j | Graph (4) |
| `risk-scoring` | Risk Scoring | Combine signals, explain, threshold | Go | PostgreSQL | Decisioning (4) |
| `case-management` | Case Management | Cases, assignment, chargebacks | TypeScript / NestJS | PostgreSQL | Ops Products (5) |
| `notification` | Notification | Multi-channel send + retry | Go | PostgreSQL | Comms (3) |
| `audit-compliance` | Audit | Hash-chain, STR, DSAR | Java 21 | Kafka infinite + QLDB/Postgres append-only | Compliance Eng (4) |
| `alert-correlation` | Alert Correlation | Composite incidents, auto-contain | Go | Redis, PostgreSQL | Detection Ops (3) |
| `integrity-monitor` | Integrity | Switch vs CBS, SWIFT z-score | Go | TimescaleDB | Channel Risk (3) |

Front-end containers (not counted in the 12): Case UI, Analytics Dashboard, Rule Console. Platform containers: Kong, Istio/Envoy, Kafka, Schema Registry, Prometheus, Grafana, Jaeger, Elasticsearch.
