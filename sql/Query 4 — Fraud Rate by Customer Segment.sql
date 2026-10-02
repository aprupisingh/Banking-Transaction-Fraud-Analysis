We will calculate:

Total transactions per customer segment
Fraud transactions per segment
Non-fraud transactions per segment
Observed fraud rate %

select customer_segment,
count(*) as total_transactions,
sum(
case when is_fraud = 1 then 1 else 0
end
)as fraud_transactions,

sum(
case when is_fraud= 0 then 1 else 0 end ) as non_fraud_transactions,
round(
sum( case when is_fraud =1 then 1 else 0 end)/count(*) * 100,2
)as fraud_rate_percentage

from banking_transactions_features
group by customer_segment
order by fraud_rate_percentage desc; 



