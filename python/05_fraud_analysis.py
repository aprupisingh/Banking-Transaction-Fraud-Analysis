import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
input_file = project_root / "Data" / "processed" / "banking_transactions_features.csv"
output_folder = project_root / "Data" / "analysis"
output_folder.mkdir(parents=True, exist_ok=True)

# Load data
if not input_file.exists():
    raise FileNotFoundError(f"Processed dataset not found: {input_file}")

df = pd.read_csv(input_file)

print("=" * 60)
print("STATISTICAL FRAUD AND ANOMALY ANALYSIS")
print("=" * 60)
print(f"\nTotal transactions: {len(df):,}")

# Basic fraud summary
fraud_count = df["is_fraud"].value_counts().sort_index()
print("\nFraud Distribution:")
print(fraud_count)

fraud_summary = (
    df.groupby("is_fraud")
    .agg(
        transactions=("transaction_id", "count"),
        total_amount=("amount", "sum"),
        average_amount=("amount", "mean"),
        median_amount=("amount", "median")
    )
    .reset_index()
)
print("\nFraud Summary:")
print(fraud_summary)

# Fraud rate by transaction type
fraud_by_transaction_type = (
    df.groupby("transaction_type")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum"),
        total_amount=("amount", "sum")
    )
)
fraud_by_transaction_type["fraud_rate"] = (
    fraud_by_transaction_type["fraud_transactions"]
    / fraud_by_transaction_type["transactions"]
) * 100
fraud_by_transaction_type = fraud_by_transaction_type.sort_values("fraud_rate", ascending=False)

print("\n" + "=" * 70)
print("FRAUD BY TRANSACTION TYPE")
print("=" * 70)
print(fraud_by_transaction_type)

# Fraud rate by customer segment
fraud_by_segment = (
    df.groupby("customer_segment")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum"),
        total_amount=("amount", "sum"),
        average_amount=("amount", "mean")
    )
)
fraud_by_segment["fraud_rate"] = (
    fraud_by_segment["fraud_transactions"] / fraud_by_segment["transactions"]
) * 100

print("\n" + "=" * 70)
print("FRAUD BY CUSTOMER SEGMENT")
print("=" * 70)
print(fraud_by_segment.sort_values("fraud_rate", ascending=False))

# Fraud rate by channel
fraud_by_channel = (
    df.groupby("channel")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum"),
        total_amount=("amount", "sum"),
        average_amount=("amount", "mean")
    )
)
fraud_by_channel["fraud_rate"] = (
    fraud_by_channel["fraud_transactions"] / fraud_by_channel["transactions"]
) * 100

print("\n" + "=" * 70)
print("FRAUD BY CHANNEL")
print("=" * 70)
print(fraud_by_channel.sort_values("fraud_rate", ascending=False))

# Fraud by IP risk
ip_risk_analysis = (
    df.groupby("is_high_risk_ip")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum"),
        average_ip_risk=("ip_risk_score", "mean")
    )
)
ip_risk_analysis["fraud_rate"] = (
    ip_risk_analysis["fraud_transactions"] / ip_risk_analysis["transactions"]
) * 100

print("\n" + "=" * 70)
print("FRAUD BY IP RISK")
print("=" * 70)
print(ip_risk_analysis)

# Fraud by failed attempts
failed_attempt_analysis = (
    df.groupby("failed_attempts_24h")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)
failed_attempt_analysis["fraud_rate"] = (
    failed_attempt_analysis["fraud_transactions"] / failed_attempt_analysis["transactions"]
) * 100

print("\n" + "=" * 70)
print("FRAUD BY FAILED ATTEMPT")
print("=" * 70)
print(failed_attempt_analysis)

# Fraud by transaction frequency
frequency_analysis = (
    df.groupby("is_high_frequency_transaction")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum"),
        average_transactions_24h=("transactions_24h", "mean")
    )
)
frequency_analysis["fraud_rate"] = (
    frequency_analysis["fraud_transactions"] / frequency_analysis["transactions"]
) * 100

print("\n" + "=" * 70)
print("FRAUD BY TRANSACTION FREQUENCY")
print("=" * 70)
print(frequency_analysis)

# High-value transaction analysis
high_value_analysis = (
    df.groupby("is_high_value_transaction")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum"),
        average_amount=("amount", "mean"),
        total_amount=("amount", "sum")
    )
)
high_value_analysis["fraud_rate"] = (
    high_value_analysis["fraud_transactions"] / high_value_analysis["transactions"]
) * 100

print("\n" + "=" * 70)
print("HIGH-VALUE TRANSACTION ANALYSIS")
print("=" * 70)
print(high_value_analysis)

# IQR outlier detection
Q1 = df["amount"].quantile(0.25)
Q3 = df["amount"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

print("\n" + "=" * 70)
print("TRANSACTION AMOUNT OUTLIERS")
print("=" * 70)
print(f"Q1: {Q1:,.2f}")
print(f"Q3: {Q3:,.2f}")
print(f"IQR: {IQR:,.2f}")
print(f"Lower Bound: {lower_bound:,.2f}")
print(f"Upper Bound: {upper_bound:,.2f}")

df["is_amount_outlier"] = (
    (df["amount"] < lower_bound) | (df["amount"] > upper_bound)
).astype(int)

outlier_analysis = (
    df.groupby("is_amount_outlier")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum"),
        average_amount=("amount", "mean")
    )
)
outlier_analysis["fraud_rate"] = (
    outlier_analysis["fraud_transactions"] / outlier_analysis["transactions"]
) * 100

print("\nOutlier Analysis:")
print(outlier_analysis)

# Fraud by risk category
risk_category_analysis = (
    df.groupby("risk_category", observed=True)
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum"),
        average_amount=("amount", "mean")
    )
)
risk_category_analysis["fraud_rate"] = (
    risk_category_analysis["fraud_transactions"] / risk_category_analysis["transactions"]
) * 100

print("\n" + "=" * 70)
print("FRAUD BY RISK CATEGORY")
print("=" * 70)
print(risk_category_analysis)

# Customer-level analysis
customer_analysis = (
    df.groupby("customer_id")
    .agg(
        transactions=("transaction_id", "count"),
        total_spending=("amount", "sum"),
        average_transaction=("amount", "mean"),
        maximum_transaction=("amount", "max"),
        fraud_transactions=("is_fraud", "sum"),
        average_ip_risk=("ip_risk_score", "mean"),
        average_failed_attempts=("failed_attempts_24h", "mean")
    )
)
customer_analysis["fraud_rate"] = (
    customer_analysis["fraud_transactions"] / customer_analysis["transactions"]
) * 100

print("\n" + "=" * 70)
print("CUSTOMER-LEVEL ANALYSIS")
print("=" * 70)
print(customer_analysis.sort_values("total_spending", ascending=False).head(10))

# Save analysis tables
fraud_summary.to_csv(output_folder / "fraud_summary.csv", index=False)
fraud_by_transaction_type.to_csv(output_folder / "fraud_by_transaction_type.csv")
fraud_by_segment.to_csv(output_folder / "fraud_by_segment.csv")
fraud_by_channel.to_csv(output_folder / "fraud_by_channel.csv")
ip_risk_analysis.to_csv(output_folder / "fraud_by_ip_risk.csv")
failed_attempt_analysis.to_csv(output_folder / "fraud_by_failed_attempts.csv")
frequency_analysis.to_csv(output_folder / "fraud_by_frequency.csv")
high_value_analysis.to_csv(output_folder / "high_value_analysis.csv")
outlier_analysis.to_csv(output_folder / "amount_outlier_analysis.csv")
risk_category_analysis.to_csv(output_folder / "risk_category_analysis.csv")
customer_analysis.to_csv(output_folder / "customer_analysis.csv")

print("\n" + "=" * 70)
print("STATISTICAL ANALYSIS COMPLETED")
print("=" * 70)
print(f"\nAnalysis files saved in: {output_folder}")