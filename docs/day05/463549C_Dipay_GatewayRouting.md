# API gateway routing (Kong)

| External REST | Auth | Transform | Upstream gRPC | Timeout |
|---|---|---|---|---|
| POST /api/v1/transactions | JWT merchant | JSON → ComputeRequest (via ingestion then score) | RiskScoring.ComputeScore after ingest | 200 ms |
| GET /api/v1/transactions/{id}/risk-score | JWT | path id | scoring read API | 100 ms |
| GET /api/v1/cases | JWT analyst | query | case-management | 2 s |
| PUT /api/v1/cases/{id}/decision | JWT analyst + step-up | body | case-management | 2 s |
| GET/POST /api/v1/rules | JWT rule_manager | YAML | rule-engine mgmt | 2 s |
| GET /api/v1/dashboard/metrics | JWT viewer | — | CQRS API | 1 s |

gRPC deadlines: RuleEngine.Evaluate 50 ms; Anomaly.Score 20 ms; Graph.Analyse 45 ms; Risk.ComputeScore 120 ms.  
Retries: **none** on POST /transactions; 1 retry on idempotent GETs.
