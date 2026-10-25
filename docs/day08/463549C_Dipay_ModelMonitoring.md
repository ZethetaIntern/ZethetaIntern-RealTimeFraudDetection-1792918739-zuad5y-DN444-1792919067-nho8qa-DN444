# Model monitoring

1. **Data drift:** PSI hourly per feature; alert PSI > 0.25.  
2. **Prediction drift:** KS test on score distribution vs last week.  
3. **Performance:** join predictions to chargebacks (30–90 d lag); weekly precision/recall.  
4. **Retrain triggers:** PSI > 0.25 or weekly detection < 90% or 90-day cadence.  
5. Dashboards: `configs/grafana/fraud_detection.json` spec.
