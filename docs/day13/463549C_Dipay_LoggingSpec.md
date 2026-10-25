# Structured logging

Format: JSON to stdout → Fluent Bit → ES.

Mandatory fields: `ts`, `level`, `service`, `env`, `trace_id`, `span_id`, `transaction_id` (if any), `msg`, `error_code`.

PII: never log PAN, CVV, OTP, full email, full phone. `card_hash` allowed. IPs truncated to /24 in INFO; full IP only DEBUG in non-prod.

Retention: app logs 90 days; PCI detailed audit 1 year; RBI transaction evidence 7 years (not in ES — object storage).
