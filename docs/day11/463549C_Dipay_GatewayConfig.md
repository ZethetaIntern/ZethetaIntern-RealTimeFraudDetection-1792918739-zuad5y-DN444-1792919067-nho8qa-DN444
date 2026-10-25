# Kong / edge gateway configuration

Plugins: jwt, rate-limiting-advanced (Redis), request-validator (OpenAPI), correlation-id, prometheus, request-transformer (REST→gRPC transcoding), response-transformer (rate limit headers), bot-detection.

Circuit breaker at edge: Kong `unhealthy` upstream if 50% 5xx over 10s; fail closed for POST /transactions only if **all** scoring pods down — else serve fallback rule-only via remaining pods.

SSL: TLS1.3, OCSP staple. Cache GET risk-score 5 seconds (`Cache-Control: private, max-age=5`).
