# Rough Aegis prototype

This is a tiny, dependency-free Python HTTP demo that accepts one transaction and returns a toy composite risk score. It illustrates the intended flow only: simple deterministic rules, a placeholder amount heuristic for anomaly scoring, and a small stand-in graph signal. It is intentionally rough and does not implement the designed microservices.

## Run

From this directory:

```sh
python app.py
```

In another terminal, send:

```sh
curl -X POST http://127.0.0.1:8080/api/v1/transactions \
  -H "Content-Type: application/json" \
  -d '{"transaction_id":"demo-1","amount":125000,"country":"IN","transactions_last_10m":6,"shared_device_fraud_reports":1}'
```

`GET /healthz` returns a basic health response. Decision ranges mirror the architecture proposal: 0–199 approve, 200–599 step up, 600–799 review, 800–1000 decline.

## Limits

No trained model, Kafka, persistence, authentication, tokenisation, graph database, concurrency hardening, or production security is included. Scores are illustrative; do not connect this demo to real payment traffic or use its decisions operationally.
