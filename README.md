# 🏦 Banking Transaction & Fraud Analysis

An end-to-end **Data Analytics project** focused on analyzing 50K+ banking transactions to understand transaction volumes, customer spending patterns, account activity, fraud patterns, and potentially unusual transaction behavior using **Python, Pandas, NumPy, SQL, MySQL, and Power BI**.

## 📌 Project Overview

This project follows a complete data analytics workflow:

**Raw Data → Data Cleaning → EDA → Statistical Analysis → SQL Analysis → Fraud & Anomaly Analysis → Visualization → Power BI Dashboard**

The analysis focuses on:

- Transaction volume and transaction amount analysis
- Customer spending behavior
- Account activity
- Transaction type and channel analysis
- Fraud rate analysis
- High-value transactions
- IP risk score analysis
- Failed transaction attempts
- Location, device, and merchant category analysis
- Potentially anomalous transaction patterns

## 🛠️ Tools & Technologies

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **SQL**
- **MySQL**
- **MySQL Workbench**
- **Power BI**
- **Git & GitHub**

## 📊 Dataset

The dataset contains **50K+ transaction records** with information such as:

`transaction_id`, `customer_id`, `account_id`, `transaction_date`, `transaction_type`, `amount`, `balance_before`, `balance_after`, `account_type`, `customer_segment`, `channel`, `location`, `merchant_category`, `device_type`, `status`, `ip_risk_score`, `failed_attempts_24h`, and `is_fraud`.

## 🐍 Python Analysis

Python was used for:

- Data loading and inspection
- Data cleaning
- Missing-value and duplicate analysis
- Data type validation
- Exploratory Data Analysis
- Customer spending analysis
- Transaction analysis
- Fraud analysis
- Statistical analysis
- Data visualization
- Transaction-level feature analysis
  ## 🧹 Data Cleaning

The data preparation process included:

- Checking missing values
- Checking duplicate transactions
- Validating data types
- Converting date/time columns
- Checking invalid or inconsistent values
- Reviewing transaction amounts
- Preparing categorical columns for analysis
- Creating derived analytical features

---

## 📈 Exploratory Data Analysis

The exploratory analysis focuses on understanding transaction and customer behavior.

### Areas Analyzed

- Transaction volume
- Transaction amount distribution
- Customer spending
- Account activity
- Transaction types
- Transaction channels
- Customer segments
- Merchant categories
- Locations
- Device types
- Transaction status
- Fraud distribution

---

## 🗄️ SQL & MySQL Analysis

MySQL was used to perform structured business analysis on the transaction data.

### Key SQL Analysis

- Overall transaction analysis
- Fraud rate analysis
- Fraud by transaction type
- Fraud by customer segment
- Fraud by channel
- Fraud by location
- Fraud by account type
- Fraud by device type
- Fraud by merchant category
- Monthly transaction trends
- Customer spending analysis
- Account activity analysis
- High-frequency customers
- High-value transactions
- IP risk analysis
- Failed attempts analysis
- Transaction status analysis
- Fraud transaction investigation
- Anomaly analysis

---

## 🚨 Fraud & Anomaly Analysis

Fraud patterns were analyzed using the `is_fraud` indicator.

An exploratory anomaly score was also created using multiple transaction-level indicators:

- High transaction amount
- High IP risk score
- Multiple failed attempts

Each indicator contributes one point to the anomaly score.


0 → No flagged indicators
1 → One flagged indicator
2 → Two flagged indicators
3 → Three flagged indicators

## 🗄️ SQL & MySQL Analysis

SQL was used to perform business-oriented analysis including:

- Overall transaction analysis
- Fraud rate analysis
- Fraud by transaction type
- Fraud by customer segment
- Fraud by channel
- Fraud by location
- Fraud by account type
- Fraud by device type
- Fraud by merchant category
- Monthly transaction trends
- Customer spending analysis
- Account activity analysis
- High-frequency customers
- High-value transactions
- IP risk analysis
- Failed attempts analysis
- Transaction status analysis
- Fraud transaction investigation
- Anomaly analysis

## 🚨 Fraud & Anomaly Analysis

Fraud patterns were analyzed using the `is_fraud` indicator.

An exploratory anomaly score was also created using multiple transaction-level indicators:

- High transaction amount
- High IP risk score
- Multiple failed attempts

Each indicator contributes one point to the anomaly score. Transactions with multiple potentially unusual characteristics were investigated further.

> **Note:** The anomaly score is an exploratory analytical technique and does not independently determine whether a transaction is fraudulent.

## 📈 Power BI Dashboard

An interactive Power BI dashboard is being developed to provide a business-friendly view of the analysis.

Planned dashboard sections include:

- **Fraud Overview**
- **Transaction Analysis**
- **Fraud & Anomaly Analysis**

Key KPIs include:

- Total Transactions
- Total Transaction Amount
- Total Customers
- Total Accounts
- Fraud Transactions
- Fraud Rate
- Average Transaction Amount
- Maximum Transaction Amount

## 💡 Key Business Questions

This project investigates questions such as:

- What is the overall transaction volume and value?
- What are the customer spending patterns?
- How active are different accounts?
- Does observed fraud rate vary across transaction channels?
- Does observed fraud rate differ across customer segments?
- Which transaction types have different observed fraud rates?
- How does fraud vary by location and device type?
- Are high-value transactions associated with other potentially unusual indicators?
- How do IP risk scores and failed attempts vary across transactions?
## 🎯 Skills Demonstrated

**Data Cleaning | Exploratory Data Analysis | Statistical Analysis | Python | Pandas | NumPy | Matplotlib | SQL | MySQL | Data Visualization | Fraud Analysis | Anomaly Analysis | Customer Analytics | Power BI | Git & GitHub**

---

## 🚀 Future Improvements

- Develop a machine learning model for fraud classification
- Perform advanced feature engineering
- Evaluate models using Precision, Recall, F1-Score, and ROC-AUC
- Implement advanced anomaly detection techniques
- Improve Power BI dashboard interactivity
- Build an automated data pipeline
- Develop customer risk segmentation

## 📁 Project Structure

```text
Banking-Transaction-Fraud-Analysis/
│
├── data/
│   └── banking_transactions_features.csv
│
├── python/
│   ├── 01_data_loading.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda.py
│   ├── 04_fraud_analysis.py
│   └── 05_visualization.py
│
├── sql/
│   ├── 01_database_setup.sql
│   ├── 02_transaction_analysis.sql
│   ├── 03_fraud_analysis.sql
│   ├── 04_transaction_type.sql
│   ├── 05_customer_segment.sql
│   ├── 06_channel_analysis.sql
│   ├── 07_high_value_transactions.sql
│   ├── 08_monthly_trend.sql
│   ├── 09_account_type.sql
│   ├── 10_device_type.sql
│   ├── 11_merchant_category.sql
│   ├── 12_location_analysis.sql
│   ├── 13_ip_risk_analysis.sql
│   ├── 14_failed_attempts.sql
│   ├── 15_anomaly_analysis.sql
│   ├── 16_status_analysis.sql
│   ├── 17_customer_spending.sql
│   ├── 18_account_activity.sql
│   ├── 19_high_frequency_customers.sql
│   ├── 20_high_risk_transactions.sql
│   ├── 21_multiple_risk_indicators.sql
│   ├── 22_fraud_transactions.sql
│   └── 23_project_summary.sql
│
├── visualizations/
│
├── powerbi/
│   └── Banking_Fraud_Analysis.pbix
│
├── .gitignore
└── README.md

