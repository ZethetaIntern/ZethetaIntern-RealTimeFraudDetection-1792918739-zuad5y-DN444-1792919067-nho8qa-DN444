# Encryption and secrets

| Layer | Control |
|---|---|
| In transit external | TLS 1.3 at Kong |
| In transit internal | Istio mTLS STRICT |
| At rest | AES-256 (cloud KMS CMK) on PG, Redis TLS, Neo4j encryption |
| PAN | Tokenisation; only `card_hash` (HMAC-SHA256 with Vault key) in events |
| Keys | HashiCorp Vault; 90-day rotation; app roles per service |
| PII in logs | Mask PAN, OTP, email local-part (see logging spec) |
| Kafka | SSL + ACLs; audit topic produce-only for services, read for audit-compliance |
