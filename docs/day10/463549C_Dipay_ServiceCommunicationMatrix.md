# Service communication matrix (least privilege)

Rows call columns. S = sync gRPC, A = async Kafka, — = forbidden.

| from \ to | ing | enr | ref | rul | ml | gr | rs | cm | nt | au | ac | im |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gateway | S | — | — | — | — | — | S | S | — | — | — | — |
| ingestion | — | A | S | — | — | — | S* | — | — | A | — | A |
| enrichment | — | — | S | — | — | A | A | — | — | A | — | — |
| reference | — | — | — | — | — | — | — | — | — | A | — | — |
| rules | — | — | S | — | — | — | — | — | — | A | — | — |
| ml | — | — | — | — | — | — | — | — | — | A | — | — |
| graph | — | — | — | — | — | — | — | — | — | A | — | — |
| risk-scoring | — | — | — | S | S | S | — | A | A | A | A | — |
| case | — | — | — | — | — | — | — | — | A | A | — | — |
| notification | — | — | — | — | — | — | — | — | — | A | — | — |
| audit | — | — | — | — | — | — | — | — | — | — | — | — |
| alert-corr | — | — | — | — | — | — | — | A | A | A | — | — |
| integrity | — | — | — | — | — | — | — | A | A | A | A | — |

\*Ingestion may call risk-scoring synchronously on the issuer-auth path; Kafka still emitted.
