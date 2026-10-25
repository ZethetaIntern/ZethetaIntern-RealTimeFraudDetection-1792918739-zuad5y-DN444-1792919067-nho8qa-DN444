# Domain Glossary — ShieldPay Fraud Platform

Minimum 50 terms. Ubiquitous language for all bounded contexts.

| # | Term | Definition |
|---|---|---|
| 1 | PAN | Primary Account Number — the full card number. Never stored raw; tokenised or hashed (`card_number_hash`). |
| 2 | BIN | Bank Identification Number — first 6–8 digits of PAN identifying issuer and product. |
| 3 | MCC | Merchant Category Code — four-digit ISO 18245 code (e.g. 7995 gambling, 6051 crypto). |
| 4 | AFA | Additional Factor of Authentication (India) — typically SMS OTP for CNP, plus 3-D Secure. |
| 5 | Tokenisation | Replacement of PAN with a surrogate token (RBI card-on-file mandate, Oct 2022). |
| 6 | Chargeback | Issuer-initiated reversal of a settled transaction after a dispute. |
| 7 | False positive rate | Share of legitimate transactions incorrectly flagged. Target < 0.5%. |
| 8 | Detection rate | Share of known/confirmed fraud correctly flagged. Target > 95%. |
| 9 | SIM-swap | Attacker ports the victim’s mobile number to a new SIM to intercept OTPs. |
| 10 | Enumeration attack | Automated low-value probes of stolen PAN ranges to find live cards. |
| 11 | Synthetic identity | Mix of real and fabricated PII used to open accounts and build a credit history. |
| 12 | Money mule | Account used to receive and onward-transfer stolen funds, often a bridge node in the graph. |
| 13 | CP fraud | Card-present fraud at POS/ATM (counterfeit, lost/stolen, card-never-received). |
| 14 | CNP fraud | Card-not-present fraud (e-commerce, MOTO). ~75% of global card fraud. |
| 15 | ATO | Account takeover — stolen credentials used to transact or change profile data. |
| 16 | Friendly / first-party fraud | Genuine cardholder disputing a valid purchase (chargeback fraud). |
| 17 | Triangulation fraud | Stolen-card purchase shipped to a buyer who paid the fraudster on another channel. |
| 18 | Skimming | Capture of mag-stripe data via a device on ATM/POS. |
| 19 | EMV fallback | Chip failure causes mag-stripe authorisation — higher fraud risk. |
| 20 | Contactless (tap) | Low-value no-PIN CP; emerging fraud vector. |
| 21 | UPI | India’s Unified Payments Interface; collect-request, QR, and PIN-phishing patterns. |
| 22 | RuPay | Domestic Indian card scheme with distinct BIN ranges. |
| 23 | Velocity | Count/sum of activity in a time window (card, device, merchant, IP). |
| 24 | Step-up authentication | Extra challenge (OTP, biometric) when score is 200–599. |
| 25 | Risk score | Composite 0–1000 from rules, ML, and graph. |
| 26 | Explainability | Human-readable attribution of a decision (rules fired, SHAP features, graph paths). |
| 27 | SHAP | Feature attributions for tree models used in explanations. |
| 28 | LIME | Model-agnostic local explanations. |
| 29 | Feature store | Online (Redis) + offline (PostgreSQL/Spark) store of ML features. |
| 30 | PSI | Population Stability Index — data-drift statistic; alert if > 0.25. |
| 31 | Champion-challenger | Production model vs shadow candidates on the same traffic. |
| 32 | Bounded context | DDD boundary with its own language and data ownership. |
| 33 | Anti-corruption layer | Adapter that stops legacy models leaking into new services. |
| 34 | Strangler Fig | Incremental replacement of the monolith by intercepting traffic. |
| 35 | Saga | Sequence of local transactions with compensations instead of 2PC. |
| 36 | CQRS | Separate write pipeline from read/materialised views. |
| 37 | Event sourcing | State as an append-only event log (used for Audit). |
| 38 | Outbox | Transactional publish of events alongside DB writes. |
| 39 | Consumer lag | Kafka offset delay; SLO < 1000 messages/partition. |
| 40 | DLQ | Dead-letter queue for poison messages after N retries. |
| 41 | mTLS | Mutual TLS between sidecars; zero-trust mesh. |
| 42 | Circuit breaker | Opens when error rate exceeds threshold; uses fallback. |
| 43 | Bulkhead | Isolation of thread/connection pools per dependency. |
| 44 | Canary | Percentage traffic shift to a new version with automated analysis. |
| 45 | Blue-green | Two production slots; atomic switch and instant rollback. |
| 46 | RPO / RTO | Recovery point / time objectives per service tier. |
| 47 | PCI DSS | Payment Card Industry Data Security Standard (v4.0). |
| 48 | STR / SAR | Suspicious Transaction Report to FIU-IND (and equivalent SAR elsewhere). |
| 49 | FIU-IND | Financial Intelligence Unit — India. |
| 50 | GDPR right to erasure | Conflicts with RBI 7-year retention; handled by jurisdiction + pseudonymisation. |
| 51 | Watchlist | Compromised PAN ranges, mule accounts, botnet IPs, sanctioned entities. |
| 52 | Device fingerprint | Browser/OS/canvas/IMEI signal used as a graph node. |
| 53 | Correlation ID / trace_id | Propagated across gRPC and Kafka for end-to-end tracing. |
| 54 | Impossible travel | Two geos closer in time than physically possible. |
| 55 | Community detection | Louvain clustering of densely linked entities (possible ring). |
| 56 | PageRank / betweenness | Centrality measures for shared infrastructure and mule bridges. |
| 57 | Merkle audit chain | Hash of each audit event includes previous hash; tamper-evident. |
| 58 | Error budget | Allowed unreliability; freeze deploys when exhausted. |
| 59 | p99 latency | 99th percentile latency SLA for a hop or the full pipeline. |
| 60 | Polyglot persistence | Different datastores per service (Postgres, Redis, Neo4j, ES, Timescale). |
