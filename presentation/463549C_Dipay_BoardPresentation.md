# Aegis — Risk & Technology Board presentation outline

**Audience:** CTO, CRO, VP Engineering, Head of Compliance, CFO  

## 1. Executive summary (1 minute)

ShieldPay's 2012 monolith and 15-minute batch scoring gap cannot meet the current fraud environment. Aegis proposes an incremental, event-driven replacement that keeps payment decisions explainable and supports a 200 ms end-to-end p99 objective. Decision requested: approve a phased discovery/pilot, subject to security, latency, and fraud-outcome gates.

## 2. Problem and outcomes (2 minutes)

- Scenario baseline: 2.4 million transactions/day; fraud attempts rose 340%; quarterly losses rose from ₹12 crore to ₹53 crore.
- Objectives: close the batch gap, target >95% detection and <0.5% false positives, make decisions auditable, and isolate service failures.
- These are design targets from the project brief, not measured prototype results.

## 3. Architecture overview (3 minutes)

Walk the Board through [`C4 Level 1`](../diagrams/c4_level1_system_context.puml) and [`C4 Level 2`](../diagrams/c4_level2_container.puml). Ingestion normalises/tokenises transactions; enrichment prepares signals; rule, anomaly, and graph checks run in parallel; scoring applies thresholds; Kafka carries audit and downstream events. The target is a 12-service decomposition with independent data ownership.

## 4. Detection strategy and decision explainability (2 minutes)

- Rules provide deterministic, versioned controls and fast containment.
- ML/anomaly serving identifies deviations; champion/challenger validates changes in shadow traffic.
- Graph analysis detects shared devices, mule paths, and coordinated rings.
- The response includes score components and reasons; each decision is retained for investigation.

## 5. Resilience and security (2 minutes)

Discuss bounded timeouts, circuit breakers, bulkheads, and explicit fallback behavior when a signal provider is unavailable. Service-to-service mTLS, least-privilege authorization, tokenised PAN, key management, and retention controls support PCI DSS, RBI, and GDPR obligations. Compliance sign-off is a release gate.

## 6. Operational readiness and migration (2 minutes)

Use the Strangler Fig pattern and anti-corruption layer, beginning with shadow scoring and limited channel/canary traffic. Monitor decision latency, consumer lag, model drift, error budgets, and fraud outcomes. Multi-region recovery, rollback, runbooks, and chaos exercises are part of readiness.

## 7. Economics and risks (2 minutes)

The initial order-of-magnitude estimate is about $83k/month under a 50k TPS peak design assumption; validate with workload tests and cloud pricing before procurement. Key risks include latency under peak load, model drift, graph freshness, false-positive customer friction, data residency, and migration parity. Each has a measurable pilot gate and a named operational owner in the full plan.

## 8. Decision and next steps (1 minute)

Request approval for a bounded pilot: validate load and fallback behavior, reconcile shadow decisions against the monolith, complete compliance threat modeling, then return with evidence before ramping traffic. Repository ownership transfer is a separate candidate action after review.
