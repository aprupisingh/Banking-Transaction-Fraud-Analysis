import pandas as pd
import numpy as np
# load the cleaned dataset
file_path = "Data/cleaned/banking_transactions_50000_cleaned.csv"
df=pd.read_csv(file_path)
# Convert date column
df['transaction_date']=pd.to_datetime(df['transaction_date'], errors='coerce')

# Basic Information
print("=" * 60)
print("Exploratory data analysis")
print("="*60)

print("\nDataset Shape:")
print(df.shape)

# Total transaction

total_transaction = len(df)
print(f"\nTotal transactions:{total_transaction:,}")

# Total transaction value  
total_transaction_value = df['amount'].sum()
print(f"\nTotal transaction value: ${total_transaction_value:,.2f}")

# Average transaction value
average_transaction_value = df['amount'].mean()
print (f"\nAverage transaction value: ${average_transaction_value:,.2f}")

# Median transaction value
median_transaction_value = df['amount'].median()
print(f"\nMedian transaction value: ${median_transaction_value:,.2f}")

# Minimum transaction
minimum_transaction = df['amount'].min()
print(f"{minimum_transaction:,.2f} is the minimum transaction value")

# Maximum transaction
maximum_transaction = df['amount'].max()
print(f"{maximum_transaction:,.2f} is the maximum transaction value")

# Transaction type Distribution
print("\n" + "="*60)
print("Transaction Type Distribution")
print("="*60)
transaction_type_count =(
    df["transaction_type"].value_counts()
)
for transaction_type, count in transaction_type_count.items():
    print(f"{transaction_type}: {count}")

#  Transaction value by type
transaction_value_by_type=(
    df.groupby("transaction_type")["amount"].sum().sort_values(ascending=False)
)
print("\n" + "="*60)
print("Transaction Value by Type")
print("="*60)
print(transaction_value_by_type)

# Channel analysis

print("\n"+"="*60)
print("Channel Analysis")
print("="*60)
channel_count =(df["channel"].value_counts())

print(channel_count)

# Customer segment analysis
print("\n" + "=" *60)

print("Customer Segment Analysis")
print("=" * 60)
 
segment_analysis = (
    df.groupby("customer_segment").agg(
        transactions=("transaction_id","count"),
        total_amount=("amount","sum"),
        average_amount=("amount","mean")
    ).sort_values(by="total_amount", ascending=False)
)
print(segment_analysis)

# Location analysis
print("\n" + "=" *60)
location_analysis =(
    df.groupby("location").agg(
        transactions=("transaction_id","count"),
        total_amount=("amount","sum"),
        average_amount=("amount","mean")
    ).sort_values("total_amount",ascending=False)
)
print(location_analysis)


# Fraud analysis
print("\n" + "=" *60)
print("Fraud Analysis")
print("=" * 60)
fraud_count = df["is_fraud"].sum()
fraud_rate =(df["is_fraud"].mean()*100)
print(f"Fraudulent transactions: {fraud_count:,}")
print(f"Fraud rate: {fraud_rate:.2f}%")

# Fraud by transaction type
fraud_by_type = (
    df.groupby("transaction_type").agg(transactions = ("transaction_id" , "count"),
                                       fraud_transactions = ("is_fraud","sum"))
)

fraud_by_type ["fraud_rate"]= (
    fraud_by_type["fraud_transactions"]/fraud_by_type["transactions"]
)*100

fraud_by_type = fraud_by_type.sort_values("fraud_rate",ascending=False)
print("\nFraud by Transaction Type :")
print(fraud_by_type)

# Fraud By channel 
fraud_by_channel=(
    df.groupby("channel").agg(
        transactions = ("transaction_id","count"),
        fraud_transactions =("is_fraud","sum")
    )
)

fraud_by_channel = fraud_by_channel.sort_values("fraud_transactions",ascending=False)
print("\nFraud by Channel:")
print(fraud_by_channel)

# Fraud by customer segment
fraud_by_segment = (df.groupby("customer_segment").agg(
    transactions=("transaction_id","count"),
    fraud_transactions = ("is_fraud" , "sum")
))
fraud_by_segment["fraud_rate"] = (
    fraud_by_segment["fraud_transactions"]/fraud_by_segment["transactions"]
)*100
fraud_by_segment = fraud_by_segment.sort_values("fraud_rate",ascending=False)
print("\nFraud by Customer Segment:")
print(fraud_by_segment)

# high Value transactions
high_value_threshold = df["amount"].quantile(0.95)

high_value_transactions = df[
    df["amount"] >= high_value_threshold
]

print("\n" + "=" * 60)
print("HIGH-VALUE TRANSACTIONS")
print("=" * 60)

print(
    f"95th percentile threshold: "
    f"{high_value_threshold:,.2f}"
)

print(
    f"High-value transactions: "
    f"{len(high_value_transactions):,}"
)

print(
    f"Fraud among high-value transactions: "
    f"{high_value_transactions['is_fraud'].sum():,}"
)

# Risk score analysis

print("\n" + "=" * 60)
print("IP RISK SCORE ANALYSIS")
print("=" * 60)

print(
    df["ip_risk_score"].describe()
)

# Failed attempt analysis
print("\n" + "=" * 60)
print("FAILED ATTEMPTS ANALYSIS")
print("=" * 60)

failed_attempt_analysis = (
    df.groupby("failed_attempts_24h")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

failed_attempt_analysis["fraud_rate"] = (
    failed_attempt_analysis["fraud_transactions"]
    / failed_attempt_analysis["transactions"]
) * 100

print(failed_attempt_analysis)

# Transactions in 24 hours


print("\n" + "=" * 60)
print("TRANSACTION FREQUENCY ANALYSIS")
print("=" * 60)

frequency_analysis = (
    df.groupby("transactions_24h")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

frequency_analysis["fraud_rate"] = (
    frequency_analysis["fraud_transactions"]
    / frequency_analysis["transactions"]
) * 100

print(frequency_analysis)


#  End


print("\n" + "=" * 60)
print("EDA COMPLETED")
print("=" * 60)