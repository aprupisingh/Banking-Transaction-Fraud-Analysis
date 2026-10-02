-- We'll calculate:

-- Total transaction amount
-- Average transaction amount
-- Minimum transaction amount
-- Maximum transaction amount
-- Total amount involved in fraudulent transactions
-- Average fraudulent transaction amount

select count(*) as total_transactions,
round(sum(amount),2) as total_transaction_amount,

    ROUND(AVG(amount), 2) AS average_transaction_amount,

    ROUND(MIN(amount), 2) AS minimum_transaction_amount,

    ROUND(MAX(amount), 2) AS maximum_transaction_amount,

    SUM(
        CASE
            WHEN is_fraud = 1 THEN amount
            ELSE 0
        END
    ) AS total_fraud_transaction_amount,

    ROUND(
        AVG(
            CASE
                WHEN is_fraud = 1 THEN amount
                ELSE NULL
            END
        ),
        2
    ) AS average_fraud_transaction_amount

FROM banking_transactions_features;