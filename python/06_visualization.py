import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
input_file = project_root / "Data" / "processed" / "banking_transactions_features.csv"
output_folder = project_root / "visualization"
output_folder.mkdir(parents=True, exist_ok=True)

# Load Data
df = pd.read_csv(input_file)
print("=" * 70)
print("Banking transaction and fraud visualization")
print ("="*70)
print(f"\nTotal transaction:{len(df):,}")

# create fraud label
df["fraud_label"] = df["is_fraud"].map({
    0: "Non-Fraud",
    1: "Fraud"
})

# Fraud avs non_fraud

fraud_counts=df["fraud_label"].value_counts()
plt.figure(figsize=(8,5))
fraud_counts.plot(kind="bar")

plt.title("Fraud vs Non-Fraud Transactions")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    output_folder / "fraud_vs_non_fraud.png",
    dpi=300
)

plt.show()
plt.close()



# FRAUD RATE BY TRANSACTION TYPE


transaction_type_analysis = (
    df.groupby("transaction_type")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

transaction_type_analysis["fraud_rate"] = (
    transaction_type_analysis["fraud_transactions"]
    / transaction_type_analysis["transactions"]
) * 100

transaction_type_analysis = (
    transaction_type_analysis
    .sort_values("fraud_rate", ascending=False)
)


plt.figure(figsize=(9, 5))

sns.barplot(
    x=transaction_type_analysis.index,
    y=transaction_type_analysis["fraud_rate"]
)

plt.title("Fraud Rate by Transaction Type")
plt.xlabel("Transaction Type")
plt.ylabel("Fraud Rate (%)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    output_folder / "fraud_rate_by_transaction_type.png",
    dpi=300
)

plt.show()
plt.close()



#  FRAUD RATE BY CUSTOMER SEGMENT


segment_analysis = (
    df.groupby("customer_segment")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

segment_analysis["fraud_rate"] = (
    segment_analysis["fraud_transactions"]
    / segment_analysis["transactions"]
) * 100

segment_analysis = (
    segment_analysis
    .sort_values("fraud_rate", ascending=False)
)


plt.figure(figsize=(9, 5))

sns.barplot(
    x=segment_analysis.index,
    y=segment_analysis["fraud_rate"]
)

plt.title("Fraud Rate by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Fraud Rate (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    output_folder / "fraud_rate_by_customer_segment.png",
    dpi=300
)

plt.show()
plt.close()



# FRAUD RATE BY CHANNEL


channel_analysis = (
    df.groupby("channel")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

channel_analysis["fraud_rate"] = (
    channel_analysis["fraud_transactions"]
    / channel_analysis["transactions"]
) * 100

channel_analysis = (
    channel_analysis
    .sort_values("fraud_rate", ascending=False)
)


plt.figure(figsize=(9, 5))

sns.barplot(
    x=channel_analysis.index,
    y=channel_analysis["fraud_rate"]
)

plt.title("Fraud Rate by Transaction Channel")
plt.xlabel("Channel")
plt.ylabel("Fraud Rate (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    output_folder / "fraud_rate_by_channel.png",
    dpi=300
)

plt.show()
plt.close()



# FRAUD RATE BY RISK CATEGORY

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


plt.figure(figsize=(8, 5))

sns.barplot(
    x=risk_analysis.index,
    y=risk_analysis["fraud_rate"]
)

plt.title("Fraud Rate by Risk Category")
plt.xlabel("Risk Category")
plt.ylabel("Fraud Rate (%)")

plt.tight_layout()

plt.savefig(
    output_folder / "fraud_rate_by_risk_category.png",
    dpi=300
)

plt.show()
plt.close()



#  HIGH-VALUE TRANSACTIONS


high_value_analysis = (
    df.groupby("is_high_value_transaction")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

high_value_analysis["fraud_rate"] = (
    high_value_analysis["fraud_transactions"]
    / high_value_analysis["transactions"]
) * 100

high_value_analysis.index = [
    "Normal Value",
    "High Value"
]


plt.figure(figsize=(8, 5))

sns.barplot(
    x=high_value_analysis.index,
    y=high_value_analysis["fraud_rate"]
)

plt.title("Fraud Rate: High-Value vs Normal Transactions")
plt.xlabel("Transaction Value")
plt.ylabel("Fraud Rate (%)")

plt.tight_layout()

plt.savefig(
    output_folder / "fraud_rate_high_value.png",
    dpi=300
)

plt.show()
plt.close()



#  HIGH-FREQUENCY TRANSACTIONS


frequency_analysis = (
    df.groupby("is_high_frequency_transaction")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

frequency_analysis["fraud_rate"] = (
    frequency_analysis["fraud_transactions"]
    / frequency_analysis["transactions"]
) * 100

frequency_analysis.index = [
    "Normal Frequency",
    "High Frequency"
]


plt.figure(figsize=(8, 5))

sns.barplot(
    x=frequency_analysis.index,
    y=frequency_analysis["fraud_rate"]
)

plt.title("Fraud Rate: High vs Normal Transaction Frequency")
plt.xlabel("Transaction Frequency")
plt.ylabel("Fraud Rate (%)")

plt.tight_layout()

plt.savefig(
    output_folder / "fraud_rate_high_frequency.png",
    dpi=300
)

plt.show()
plt.close()


# HIGH IP RISK


ip_analysis = (
    df.groupby("is_high_risk_ip")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

ip_analysis["fraud_rate"] = (
    ip_analysis["fraud_transactions"]
    / ip_analysis["transactions"]
) * 100

ip_analysis.index = [
    "Normal IP Risk",
    "High IP Risk"
]


plt.figure(figsize=(8, 5))

sns.barplot(
    x=ip_analysis.index,
    y=ip_analysis["fraud_rate"]
)

plt.title("Fraud Rate: High vs Normal IP Risk")
plt.xlabel("IP Risk")
plt.ylabel("Fraud Rate (%)")

plt.tight_layout()

plt.savefig(
    output_folder / "fraud_rate_ip_risk.png",
    dpi=300
)

plt.show()
plt.close()


#  FAILED ATTEMPTS


failed_analysis = (
    df.groupby("has_multiple_failed_attempts")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

failed_analysis["fraud_rate"] = (
    failed_analysis["fraud_transactions"]
    / failed_analysis["transactions"]
) * 100

failed_analysis.index = [
    "Fewer Failed Attempts",
    "Multiple Failed Attempts"
]


plt.figure(figsize=(8, 5))

sns.barplot(
    x=failed_analysis.index,
    y=failed_analysis["fraud_rate"]
)

plt.title("Fraud Rate by Failed Login Attempts")
plt.xlabel("Failed Attempts")
plt.ylabel("Fraud Rate (%)")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    output_folder / "fraud_rate_failed_attempts.png",
    dpi=300
)

plt.show()
plt.close()



#  TRANSACTION AMOUNT DISTRIBUTION#

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="amount",
    hue="fraud_label",
    bins=50,
    kde=True
)

plt.title("Transaction Amount Distribution")
plt.xlabel("Transaction Amount")
plt.ylabel("Number of Transactions")

plt.tight_layout()

plt.savefig(
    output_folder / "transaction_amount_distribution.png",
    dpi=300
)

plt.show()
plt.close()



#  RISK SCORE DISTRIBUTION


plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="risk_indicator",
    hue="fraud_label"
)

plt.title("Fraud Distribution by Risk Indicator")
plt.xlabel("Risk Indicator")
plt.ylabel("Number of Transactions")

plt.tight_layout()

plt.savefig(
    output_folder / "fraud_by_risk_indicator.png",
    dpi=300
)

plt.show()
plt.close()



#  WEEKDAY VS WEEKEND


weekend_analysis = (
    df.groupby("is_weekend")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

weekend_analysis["fraud_rate"] = (
    weekend_analysis["fraud_transactions"]
    / weekend_analysis["transactions"]
) * 100

weekend_analysis.index = [
    "Weekday",
    "Weekend"
]


plt.figure(figsize=(8, 5))

sns.barplot(
    x=weekend_analysis.index,
    y=weekend_analysis["fraud_rate"]
)

plt.title("Fraud Rate: Weekday vs Weekend")
plt.xlabel("Day Type")
plt.ylabel("Fraud Rate (%)")

plt.tight_layout()

plt.savefig(
    output_folder / "fraud_rate_weekend.png",
    dpi=300
)

plt.show()
plt.close()



#  TRANSACTION HOUR


hour_analysis = (
    df.groupby("transaction_hour")
    .agg(
        transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

hour_analysis["fraud_rate"] = (
    hour_analysis["fraud_transactions"]
    / hour_analysis["transactions"]
) * 100


plt.figure(figsize=(12, 5))

plt.plot(
    hour_analysis.index,
    hour_analysis["fraud_rate"],
    marker="o"
)

plt.title("Fraud Rate by Transaction Hour")
plt.xlabel("Transaction Hour")
plt.ylabel("Fraud Rate (%)")

plt.xticks(range(0, 24))

plt.grid(True)

plt.tight_layout()

plt.savefig(
    output_folder / "fraud_rate_by_hour.png",
    dpi=300
)

plt.show()
plt.close()



#  COMPLETION MESSAGE


print("\n" + "=" * 70)
print("VISUALIZATION COMPLETED")
print("=" * 70)

print(
    f"\nCharts saved to: {output_folder}"
)