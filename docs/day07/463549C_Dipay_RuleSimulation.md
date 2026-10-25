# Rule simulation (backtest)

Input: draft rule + 30 days `transactions.enriched` + confirmed labels (chargeback + analyst).

Output report:

- transactions evaluated  
- flagged count  
- confirmed fraud in flagged (TP)  
- confirmed legitimate in flagged (FP)  
- detection rate, false positive rate  
- estimated annual fraud prevented = TP amount × 12/1 month sample  
- estimated annual customer friction = FP count × step-up cost  

A/B: shadow 7 days on live traffic; compare lift vs control; activate only if FPR does not rise > 10% relative and detection +≥ 2%.
