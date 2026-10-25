# Event Storming — 50+ domain events

Policies: hot-path scoring is **orchestration** (risk-scoring fan-out). Investigation is **orchestration** (saga worker). Enrichment pipeline is **choreography**.

## Aggregates
Transaction, EnrichedTransaction, CustomerProfile, Rule, ModelVersion, GraphSnapshot, RiskDecision, FraudCase, Notification, AuditBlock, CompositeIncident, IntegrityFinding, Card, Device.

## Commands → events (catalogue)

1. TransactionSubmitted → transaction_received  
2. TransactionPersisted → transaction_persisted  
3. PanTokenised → pan_tokenised  
4. TraceAssigned → trace_id_assigned  
5. EnrichmentStarted → enrichment_started  
6. DeviceLookupCompleted → device_fingerprint_attached  
7. GeoLookupCompleted → ip_geo_attached  
8. ProfileLoaded → customer_profile_loaded  
9. TransactionEnriched → transaction_enriched  
10. VendorTimeout → enrichment_degraded  
11. RulesEvaluateRequested → rule_evaluation_started  
12. VelocityWindowUpdated → velocity_counter_updated  
13. RuleTriggered → rule_triggered  
14. RulePassedAll → rules_cleared  
15. RuleEvaluationCompleted → rule_evaluated  
16. MlScoreRequested → ml_inference_started  
17. FeaturesFetched → features_fetched  
18. ChallengerScored → shadow_score_emitted  
19. MlScored → anomaly_scored  
20. ModelDriftDetected → model_drift_detected  
21. GraphLookupRequested → graph_lookup_started  
22. GraphUpdated → graph_edge_written  
23. CommunityFlagged → fraud_community_detected  
24. TemplateMatched → fraud_template_matched  
25. ShortPathFound → known_fraud_path_found  
26. GraphLookupCompleted → graph_signals_ready  
27. GraphTimeout → graph_degraded  
28. ScoreAggregated → risk_score_computed  
29. ThresholdApplied → risk_action_selected  
30. ExplanationBuilt → explanation_generated  
31. DecisionPublished → risk_decision_made  
32. AutoApproved → transaction_auto_approved  
33. StepUpRequested → step_up_challenged  
34. StepUpPassed → step_up_passed  
35. StepUpFailed → step_up_failed  
36. AutoDeclined → transaction_auto_declined  
37. ReviewQueued → review_enqueued  
38. AlertRaised → fraud_alert_raised  
39. AlertsCorrelated → composite_incident_opened  
40. TerminalIsolated → pos_terminal_circuit_opened  
41. CaseCreated → case_created  
42. AnalystAssigned → case_assigned  
43. CardFreezeRequested → card_freeze_requested  
44. CardFrozen → card_frozen  
45. CaseResolvedFraud → case_confirmed_fraud  
46. CaseResolvedFP → case_false_positive  
47. CaseEscalated → case_escalated  
48. CardBlocked → card_permanently_blocked  
49. ReplacementIssued → card_reissue_started  
50. ChargebackOpened → chargeback_initiated  
51. NotificationQueued → notification_requested  
52. NotificationDelivered → notification_sent  
53. NotificationFailed → notification_failed  
54. AuditAppended → audit_event_chained  
55. SwitchCbsMismatch → integrity_mismatch_detected  
56. SwiftAnomaly → swift_anomaly_detected  
57. GeoVelocityBreach → geo_velocity_breached  
58. RuleActivated → rule_activated  
59. RuleRolledBack → rule_rolled_back  
60. ModelPromoted → champion_replaced  

Read models: FraudStatsHourly, GeoHeatmap, RuleEffectiveness, ModelPerformance, CaseBacklog.

External systems: Networks, UPI, CBS, Mobile, Vendors, FIU-IND, Monolith ACL.

See `diagrams/day06_event_storming.puml` for a condensed visual (not all 60 boxes — catalogue above is the source of truth).
