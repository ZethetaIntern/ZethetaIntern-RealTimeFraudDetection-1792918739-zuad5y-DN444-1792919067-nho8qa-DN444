# Legacy Monolith Analysis — ShieldPay (starting state)

Source: simulation Section B1.1 plus Event Storming of the current transaction lifecycle.

## 1. As-is technical snapshot

| Attribute | Current state |
|---|---|
| Application | Single Java WAR on Apache Tomcat 8.5, bare metal, Mumbai colo |
| Age / size | Built 2012; ~1.2M LOC; 500+ fraud rules in `switch` / `if` trees |
| Database | One Oracle 19c instance, 45 TB, no read replicas, no cross-region replica |
| Analytics | 3-second typical analytical queries; mixed OLTP + OLAP |
| ML | Logistic regression, trained 6 months ago, **batch every 15 minutes** via cron |
| Deploy | Saturday 4-hour maintenance window, manual |
| Mesh / containers | None |
| Single point of failure | Oracle + the JVM process itself |

## 2. Business capabilities (monolith modules → capability)

| Monolith area | Business capability | Target bounded context |
|---|---|---|
| Channel adapters (ISO 8583, NPCI UPI, ecom HTTP) | Transaction capture & normalisation | Transaction Ingestion |
| Customer master + device table | Behavioural profile | Customer Profile |
| MCC/BIN static tables | Reference data | Reference Data |
| Java switch rules | Fraud rule evaluation | Rule Engine |
| Nightly/15-min scoring job | Anomaly / ML scoring | Anomaly Detection |
| (absent) | Relationship / ring detection | Graph Analysis |
| Score + threshold if-blocks | Composite risk decision | Risk Scoring |
| Analyst desktop (Swing/JSP) | Investigation workflow | Case Management |
| SMTP/SMS vendor calls | Customer & ops alerting | Notification |
| Oracle `AUDIT_LOG` table (mutable UPDATE allowed) | Regulatory evidence | Audit & Compliance |
| Ad-hoc SQL reports | Ops dashboards | CQRS read models |
| (absent) | Alert correlation / auto-containment | Alert Correlation |

## 3. External integrations (as-is)

| System | Protocol | Direction | Notes |
|---|---|---|---|
| Visa / Mastercard / RuPay | ISO 8583 via switch | Bidirectional | Auth request/response on critical path |
| NPCI UPI | NPCI APIs | Bidirectional | Collect + pay |
| Core banking (CBS) | SOAP, 800 ms typical | Outbound | Balance / account status |
| Customer mobile app | REST + push | Outbound notify; inbound step-up | |
| SMS aggregator | HTTP | Outbound | OTP and fraud SMS |
| Email (SendGrid-like) | HTTP | Outbound | |
| RBI / FIU-IND reporting | SFTP batch nightly | Outbound | Not real-time |
| Chargeback (Visa VROL etc.) | File + API | Bidirectional | |
| ThreatMetrix / MaxMind | HTTPS | Outbound | Device + IP — currently best-effort, often skipped under load |
| Legacy HVAC/vendor VPN analogues | Site-to-site | Inbound | Weak third-party monitoring (Target lesson) |

## 4. Architectural pain points (why Q3 2025 failed)

1. **Batch scoring gap.** Fraudsters timed spend immediately after the 15-minute cron. Need **inline inference < 10 ms p99**.
2. **Hard-coded rules.** Business cannot change velocity thresholds without a Saturday release. Need YAML/JSON rule lifecycle with simulation.
3. **Single 45 TB Oracle.** Analytical queries contend with authorisations. Need polyglot persistence and CQRS.
4. **No graph.** Synthetic identity ring shared devices/addresses — invisible to row-level rules.
5. **Mutable audit table.** Wirecard-class integrity failure: `UPDATE`/`DELETE` possible by DBA.
6. **No correlation.** POS malware would page 1,797 times (Target). Need composite incidents.
7. **No geo-velocity service independent of the ATM switch** (Cosmos Bank). Switch compromise bypasses CBS checks.
8. **Manual deploy / no HPA.** Cannot absorb 10× burst from enumeration after a breach.
9. **False positives 0.3% → 2.1%.** No per-rule performance dashboard, no shadow A/B.
10. **No fallbacks.** If Oracle is slow, the whole issuer either times out (revenue loss) or auto-approves (fraud loss).

## 5. Transaction lifecycle today (commands / events / aggregates)

See `diagrams/day01_event_storming.puml`.

**Aggregates:** Transaction, CustomerProfile, RuleSet (implicit in code), FraudCase, Notification, AuditEntry.

**Commands:** SubmitTransaction, EnrichTransaction, EvaluateRules, BatchScore, MakeRiskDecision, NotifyCustomer, CreateCase, AssignAnalyst, ResolveCase.

**Events (initial set):** `transaction_received`, `transaction_enriched`, `rule_evaluated`, `ml_scored`, `risk_decision_made`, `case_created`, `case_assigned`, `case_resolved`, `notification_sent`.

Day 6 expands this to 50+ events after decomposition.

## 6. Migration stance

Use **Strangler Fig**: API gateway dual-writes new traffic to Aegis while the anti-corruption layer translates Oracle records for in-flight cases. Freeze new features on the WAR. Retire modules in order: Notification → Case Management → Rules → Scoring → Ingestion last (riskiest cut-over).
