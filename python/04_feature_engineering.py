import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
input_file = project_root / "Data" / "cleaned" / "banking_transactions_50000_cleaned.csv"
output_folder = project_root / "Data" / "processed"
output_folder.mkdir(parents=True, exist_ok=True)
output_file = output_folder / "banking_transactions_features.csv"

# Load cleaned data
df = pd.read_csv(input_file)
print("=" * 60)
print("FEATURE ENGINEERING")
print(f"\nOriginal rows: {len(df):,}")
print(f"\nOriginal columns: {len(df.columns)}")

# Convert Datetime
df["transaction_datetime"] = pd.to_datetime(
    df["transaction_date"], errors="coerce"
)

# Extract transaction hour
df["transaction_hour"] = df["transaction_datetime"].dt.hour

# Extract transaction day of week
df["transaction_day_of_week"] = df["transaction_datetime"].dt.day_name()

# Extract month number and name
df["transaction_month"] = df["transaction_datetime"].dt.month
df["transaction_month_name"] = df["transaction_datetime"].dt.month_name()

# Weekend indicator
df["is_weekend"] = (df["transaction_datetime"].dt.dayofweek >= 5).astype(int)

# Amount to balance ratio
df["amount_to_balance_ratio"] = df["amount"] / df["balance_before"]

# high value transaction
high_value_threshold = df["amount"].quantile(0.95)
df["is_high_value_transaction"] = (df["amount"] > high_value_threshold).astype(int)
print(f"\nHigh value transaction threshold: ${high_value_threshold:,.2f}")

# High transaction frequency
frequency_threshold = df["transactions_24h"].quantile(0.95)
df["is_high_frequency_transaction"] = (df["transactions_24h"] > frequency_threshold).astype(int)
print(f"\nHigh frequency transaction threshold: {frequency_threshold:,.2f}")

#  High IP risk

risk_threshold = (
    df["ip_risk_score"].quantile(0.95)
)

df["is_high_risk_ip"] = (
    df["ip_risk_score"]
    >= risk_threshold
).astype(int)


print(
    f"High IP-risk threshold: "
    f"{risk_threshold:.2f}"
)



#  Multiple failed attempts


df["has_multiple_failed_attempts"] = (
    df["failed_attempts_24h"] >= 2
).astype(int)



# Unusual transaction hour


df["is_unusual_hour"] = (
    (df["transaction_hour"] < 6)
    | (df["transaction_hour"] >= 23)
).astype(int)



# Risk indicator


df["risk_indicator"] = (
    df["is_high_value_transaction"]
    + df["is_high_frequency_transaction"]
    + df["is_high_risk_ip"]
    + df["has_multiple_failed_attempts"]
    + df["is_unusual_hour"]
)



#  Risk category


df["risk_category"] = pd.cut(
    df["risk_indicator"],
    bins=[-1, 1, 3, 5],
    labels=[
        "Low",
        "Medium",
        "High"
    ]
)


#  Display new features


new_features = [
    "transaction_hour",
    "transaction_day_of_week",
    "transaction_month",
    "transaction_month_name",
    "is_weekend",
    "amount_to_balance_ratio",
    "is_high_value_transaction",
    "is_high_frequency_transaction",
    "is_high_risk_ip",
    "has_multiple_failed_attempts",
    "is_unusual_hour",
    "risk_indicator",
    "risk_category"
]

print("\nNew features:")
print(df[new_features].head())



#  Compare risk category with fraud

risk_analysis = (
    df.groupby("risk_category", observed=True)
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

risk_analysis["fraud_rate"] = (
    risk_analysis["fraud_transactions"]
    / risk_analysis["transactions"]
) * 100

print("\nFraud rate by risk category:")
print(risk_analysis)



#  Save processed dataset

df.to_csv(
    output_file,
    index=False
)



# 20. Final report
# -----------------------------------

print("\n" + "=" * 60)
print("FEATURE ENGINEERING COMPLETED")
print("=" * 60)

print(
    f"Rows: {len(df):,}"
)

print(
    f"Columns: {len(df.columns)}"
)

print(
    f"Saved to: {output_file}"
)