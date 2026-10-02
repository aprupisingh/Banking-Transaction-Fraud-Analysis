-- SELECT COUNT(*) AS total_rows
-- FROM banking_transactions_features
-- WHERE amount IS NOT NULL;
-- SELECT amount
-- FROM banking_transactions_features
-- WHERE amount IS NOT NULL
-- ORDER BY amount
-- LIMIT 1 OFFSET 44999;
select 
  case 
     when amount >= 9184.75  then " High value"
     else 'Noramal Value'
     end as transaction_value_category,
     count(*) as Total_transactions,
     sum(
       case 
          when is_fraud=1 then 1 else 0 end
          ) as fraud_transactions,
     sum(
     case when is_fraud= 0 then 1 else 0 end 
         )as non_fraud_transactions,
     
     round(
         sum(
         case 
            when is_fraud = 1 then 1 else 0 end 
         )/count(*) *100,2
         ) as fraud_rate_percentage,
rOUND(SUM(amount), 2) AS total_transaction_amount,

    ROUND(AVG(amount), 2) AS average_transaction_amount

FROM banking_transactions_features

GROUP BY transaction_value_category
ORDER BY fraud_rate_percentage DESC;