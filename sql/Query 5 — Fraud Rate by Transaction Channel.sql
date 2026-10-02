select 
channel, 
count(*) as total_transactions,
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
group by channel
order by fraud_rate_percentage desc; 