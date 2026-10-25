# Dead-letter queue strategy

Poison: Avro decode fail, or handler throws after **3** retries with exponential backoff (50 ms, 200 ms, 800 ms) **off** the auth path (async consumers only).

| Step | Action |
|---|---|
| 1 | Log error with `trace_id`, `transaction_id`, exception class |
| 2 | Produce to `fraud.dlq` with headers: `original-topic`, `original-partition`, `original-offset`, `exception`, `attempts` |
| 3 | Increment `fraud_dlq_total{topic,reason}` |
| 4 | P3 if DLQ rate > 0.01% of topic; P2 if > 0.1% for 5 min |

Replay: `tools/dlq-replay` copies records back after a hotfix, preserving keys. Binary blobs that fail schema are parked in object storage, not retried blindly.

Auth-path gRPC failures do **not** DLQ the customer wait: they trigger **fallback scoring** and still emit `audit.events` + `fraud.decisions` with `degraded=true`.
