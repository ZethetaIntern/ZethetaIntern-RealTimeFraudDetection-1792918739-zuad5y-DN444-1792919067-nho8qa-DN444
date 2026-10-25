# Bounded Context Map — Aegis (ShieldPay)

## Heuristics applied

| Heuristic | Application |
|---|---|
| Business capability | One primary capability per service |
| Data ownership | No shared Oracle; each context owns its store |
| Team size | 3–5 engineers per service (VP Engineering lens) |
| Change frequency | Rule authoring changes daily; ingestion protocol rarely — split |
| Scalability | Graph queries ≠ 50k TPS ingest path |
| Failure isolation | Graph or ML outage must not stop rule-based decisions |

## Contexts

### 1. Transaction Ingestion
Receives POS, ecom, ATM, UPI; protocol translation; PAN tokenisation; `trace_id`; publish `transactions.raw`.

### 2. Enrichment & Customer Profile
Device fingerprint, IP geo, BIN/MCC join, incremental profile (amounts, hours, geos, devices).

### 3. Reference Data
MCC, BIN, FX, holidays, country risk, watchlists. Supplier to Enrichment and Rules.

### 4. Fraud Rule Evaluation
Deterministic YAML rules, velocity windows, shadow mode.

### 5. Anomaly Detection
Model serving, feature fetch, ensemble score.

### 6. Graph Analysis
Property graph of cards/devices/IPs/merchants; path, community, templates.

### 7. Risk Scoring
Weighted / max / Bayesian combination; thresholds; explanations.

### 8. Case Management
Human review, assignment, chargeback hooks.

### 9. Notification
SMS, email, push, merchant webhook, Slack/PagerDuty. Conformist on `fraud.decisions` schema.

### 10. Audit & Compliance
Append-only hash-chained events; RBI/PCI/GDPR reports.

### 11. Alert Correlation & Containment
Groups related alerts (store, signature, window); auto P1; circuit-break compromised terminals (Target).

### 12. Integrity & Channel Monitoring
Independent CBS vs switch log compare; SWIFT anomaly (Cosmos). Could sit with Alert Correlation in a smaller org; kept separate so a switch compromise is a **different failure domain** from POS malware correlation.

## Context mapping

| Upstream | Downstream | Pattern |
|---|---|---|
| Ingestion | Enrichment | Customer–Supplier |
| Enrichment | Rule / ML / Graph | Customer–Supplier |
| Rule / ML / Graph | Risk Scoring | Customer–Supplier |
| Risk Scoring | Notification, Case, Audit | Conformist (event schema) |
| Reference Data | Enrichment, Rules | Customer–Supplier |
| Legacy Monolith | All new services | Anti-Corruption Layer |
| Shared IDs (`txn_id`, `risk_action`) | All | Shared Kernel |
| Audit | Regulators | Open Host Service |

No circular runtime dependencies: scoring never calls case management; case management emits commands via Kafka.

## Trade-off notes (Decomposition Master)

- **Feature Store** is not a 13th bounded context; it is infrastructure owned by Anomaly Detection with a gRPC `GetFeatures` used by Rules for velocity keys.
- **Integrity Monitoring** vs Ingestion: keeping them split means ATM authorisation can be independently checksummed even if ingest is healthy but the switch is lying.
- **Notification** is isolated so SMS vendor latency cannot block the 100 ms decision.
