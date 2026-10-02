-- CREATE DATABASE banking_fraud_analysis;
use banking_fraud_analysis;
-- select database();
SHOW TABLES;

-- total number of rows.
SELECT COUNT(*) AS total_transactions
FROM banking_transactions_features;

select *from banking_transactions_features limit 10 ;
describe banking_transactions_features;