import pandas as pd
from pathlib import Path

file_path = Path(__file__).resolve().parents[1] / "Data" / "raw" / "banking_transactions_50000.csv"
df = pd.read_csv(file_path)
print("=" * 60)
print("Data Quality Check")
print("=" * 60)

# Basic Information
print("\n1.Dataset shape")
print(df.shape)

print("\n2.Dataset info")
print(df.info())

print("\n3.Dataset Type")
print(df.dtypes)

# Missing Values
print("\n4.Missing values")
print(df.isnull().sum())

print("\n5.Duplicate values")
print(df.duplicated().sum())

print("\n6.Unique values")
print(df.nunique())

print ("\n7.Transaction date range")
print("-" * 30)
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

print(
    "Start:",
    df["transaction_date"].min()
)

print(
    "End  :",
    df["transaction_date"].max()
)

# transaction amount
print("\n8.Transaction amount")
print(df["amount"].describe())
print("\n9.Transaction amount distribution")
print(df["amount"].value_counts().head(10))
print(df["amount"].value_counts().tail(10))
print("\n10. Negative transaction amounts")
print("-" * 30)

negative_amounts = (
    df["amount"] < 0
).sum()

print(
    f"Negative amounts: "
    f"{negative_amounts:,}"
)
# Fraud analysis
print("\n11. Fraud analysis")
fraud_count = df["is_fraud"].sum()
fraud_percentage = (fraud_count / len(df)) * 100
print(f"Fraudulent transactions: {fraud_count:,} ({fraud_percentage:.2f}%)")
# Transaction status
print("\n12. Transaction status")
print(df["status"].value_counts())

print("\n13. Transaction types")
print(df["transaction_type"].value_counts())

print("\n14. Locations")
print(df["location"].value_counts())
print("\n15. IP risk score")
print("-" * 30)

print(
    df["ip_risk_score"].describe()
)

print("\n16. Failed attempts in 24 hours")
print("-" * 30)

print(
    df["failed_attempts_24h"]
    .value_counts()
    .sort_index()
)

print("\n17. Transactions in 24 hours")
print("-" * 30)

print(
    df["transactions_24h"].describe()
)

print("\n" + "=" * 60)
print("DATA QUALITY CHECK COMPLETED")
print("=" * 60)











