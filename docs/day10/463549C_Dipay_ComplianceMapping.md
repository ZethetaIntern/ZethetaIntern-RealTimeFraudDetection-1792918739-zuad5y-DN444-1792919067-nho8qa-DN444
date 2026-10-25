# PCI DSS v4.0, RBI, GDPR → architecture

## PCI DSS (selected reqs)

| Requirement | Component |
|---|---|
| 3.x Protect stored account data | Tokenisation; no raw PAN in PG; hashes only |
| 4.x Encrypt transmission | TLS 1.3 + mTLS |
| 1 / 7 Network & access | NetworkPolicies + Istio AuthorizationPolicy + RBAC |
| 5 / 6 Vuln / secure software | Image scan in CI, distroless, non-root |
| 8 Identify users | JWT unique `sub`, no shared admins |
| 10 Logging | audit.events hash chain + ES with 1y PCI detail |
| 11 Test security | Chaos + pen-test window; WAF at edge |
| 12 Policy | Runbooks + dual control on audit |

## RBI / FIU-IND

| Requirement | Component |
|---|---|
| Real-time fraud monitoring | Aegis hot path |
| AFA / OTP | STEP_UP action 200–599 |
| Card-on-file tokenisation | Ingestion tokeniser |
| Report fraud > ₹2 lakh card | audit-compliance STR job |
| 7-year transaction retention | Kafka infinite + object lock for decisions |
| UPI-specific patterns | VEL-005 and channel dimension |

## GDPR

| Requirement | Component |
|---|---|
| Minimisation | hashes not PAN; purpose=fraud |
| Lawful basis | legitimate interest / legal obligation |
| Access / portability | DSAR API on profile + decisions |
| Erasure vs RBI 7y | **IN/SG**: retain; **EU cardholders**: pseudonymise identifiers after local max, keep hash-chain of decisions without direct identifiers |
| Breach notify | P1 runbook |

No single admin can UPDATE audit (Wirecard): dual approval break-glass, append-only IAM deny delete.
