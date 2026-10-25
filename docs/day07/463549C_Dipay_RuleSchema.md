# Rule engine configuration schema

Canonical JSON Schema: `configs/rules/rule.schema.json`.  
Authoring format: YAML that validates against that schema.

Capabilities: nested AND/OR/NOT, temporal windows, entity scopes, actions (flag, block, score_adjust, notify, step_up_auth), metadata, `max_evaluation_time_ms`. New rule types add fields as optional (backward compatible) without engine releases when the evaluator already knows the operator.

Priority: integer order, short-circuit on `block`. Chaining: `score_adjust` accumulates; later rules see `running_score`.
