USE banking_fraud_analysis;
show columns from banking_transactions_features like '%fraud%' ;
USE banking_fraud_analysis;

SELECT
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN is_fraud = 1 THEN 1 ELSE 0 END) AS fraud_transactions,
    SUM(CASE WHEN is_fraud = 0 THEN 1 ELSE 0 END) AS non_fraud_transactions,
    ROUND(
        SUM(CASE WHEN is_fraud = 1 THEN 1 ELSE 0 END)
        / COUNT(*) * 100,
        2
    ) AS fraud_rate_percentage
FROM banking_transactions_features;