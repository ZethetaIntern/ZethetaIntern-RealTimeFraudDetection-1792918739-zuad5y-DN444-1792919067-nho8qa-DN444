# ML model serving architecture

**Inference engine:** ONNX Runtime in a Python FastAPI process with models pre-loaded (warm-up on `startup`). Justification: LightGBM/XGBoost and sklearn isolation forest all export to ONNX; p99 < 10 ms on CPU; no GPU required at ShieldPay’s 50k TPS with horizontal scale. TensorFlow Serving reserved if LSTM sequence model is promoted.

**Registry:** MLflow — model type, train date, dataset size, metrics, approver, deploy date.

**Pipeline:** train → holdout → pre-prod → **canary 5%** → 100%.

**Ensemble:**  
`ml_score = 0.5 * supervised_gbdt + 0.3 * isolation_forest + 0.2 * sequence_lstm`  
then min-max to 0–1000.

**A/B traffic** via Istio 5/25/50/100 and champion-challenger shadow (Day 8 companion doc).

Dockerfile-style: distroless python, USER 1000, `/healthz` includes `model_loaded=true`.
