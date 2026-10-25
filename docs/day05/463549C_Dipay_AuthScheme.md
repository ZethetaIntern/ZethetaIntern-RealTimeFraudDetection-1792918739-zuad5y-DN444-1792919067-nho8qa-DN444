# Authentication and authorisation

## External
- JWT RS256, issuer `https://id.shieldpay.example`, audience `aegis-api`.
- Machine clients: OAuth2 client_credentials.
- Legacy: API keys in Kong (sunset 90 days post-cutover).

## RBAC claims → permissions

| Role | Permissions |
|---|---|
| `merchant` | POST transactions, GET own risk-score |
| `analyst` | cases read/write decision |
| `rule_author` | create draft rules |
| `rule_approver` | activate rules |
| `auditor` | read-only audit queries, no PAN |
| `admin` | ops; **cannot** mutate audit store without dual control |

## Internal
- Istio mTLS STRICT.
- AuthorizationPolicy: least privilege (notification cannot call rule-engine).
- Cardholder data access logged to `audit.events`.
