import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
input_file = project_root / "Data" / "raw" / "banking_transactions_50000.csv"
output_folder = project_root / "Data" / "cleaned"
output_file = output_folder / "banking_transactions_50000_cleaned.csv"

df = pd.read_csv(input_file)

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)

print(f"\nOriginal rows: {len(df):,}")
print(f"Original columns: {len(df.columns)}")
cleaned_df = df.copy()
print("\nMissing values before cleaning:")
print(cleaned_df.isnull().sum())
duplicate_rows = cleaned_df.duplicated().sum()

print(f"\nDuplicate rows found: {duplicate_rows:,}")

cleaned_df = cleaned_df.drop_duplicates()

print(
    f"Rows after removing duplicates: "
    f"{len(cleaned_df):,}"
)

# remove duplicate transaction ids

duplicate_ids = (
    cleaned_df["transaction_id"].duplicated().sum()
)

print(
    f"\nDuplicate transaction IDs: "
    f"{duplicate_ids:,}"
)

cleaned_df = cleaned_df.drop_duplicates(
    subset="transaction_id",
    keep="first"
)

print(
    f"Rows after transaction ID check: "
    f"{len(cleaned_df):,}"
)
# clean transaction date
cleaned_df["transaction_date"] = pd.to_datetime(
    cleaned_df["transaction_date"],
    errors="coerce"
)

invalid_dates = cleaned_df["transaction_date"].isnull().sum()

print(
    f"Invalid transaction dates: "
    f"{invalid_dates:,}"
)

# convert the amount into numeric
cleaned_df["amount"] = pd.to_numeric(
    cleaned_df["amount"],
    errors="coerce"
)
print(cleaned_df["amount"].isnull().sum())
# convert balance columns to numeric
for column in ["balance_before", "balance_after"]:
    cleaned_df[column] = pd.to_numeric(
        cleaned_df[column],
        errors="coerce"
    )
    print(f"Missing {column} values: {cleaned_df[column].isnull().sum():,}")

# convert the risk related column
cleaned_df["ip_risk_score"] = pd.to_numeric(
    cleaned_df["ip_risk_score"],
    errors="coerce"
)

print(cleaned_df["ip_risk_score"].isnull().sum())

for column in ["transactions_24h", "failed_attempts_24h"]:
    cleaned_df[column] = pd.to_numeric(
        cleaned_df[column],
        errors="coerce"
    )
    print(f"Missing {column} values: {cleaned_df[column].isnull().sum():,}")

# clean categorical text columns and label missing values
for column in ["location", "merchant_category", "device_type"]:
    cleaned_df[column] = (
        cleaned_df[column]
        .astype("string")
        .str.strip()
        .replace("", pd.NA)
        .fillna("Unknown")
    )

output_folder.mkdir(parents=True, exist_ok=True)
cleaned_df.to_csv(output_file, index=False)

print(f"\nCleaned file saved to: {output_file}")
print(f"Cleaned rows: {len(cleaned_df):,}")
