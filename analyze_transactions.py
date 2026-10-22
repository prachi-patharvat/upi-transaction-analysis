"""Analyze the synthetic UPI transaction dataset for a portfolio project."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "upi_transactions_sample.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

# 1. Load data and convert columns to the correct data types.
df = pd.read_csv(DATA_FILE)
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")
df["amount_inr"] = pd.to_numeric(df["amount_inr"], errors="coerce")
df["status"] = df["status"].astype("string").str.strip().str.upper()
df["month"] = df["transaction_date"].dt.to_period("M").astype("string")
df["hour"] = pd.to_datetime(df["transaction_time"], format="%H:%M:%S", errors="coerce").dt.hour

# 2. Basic data quality checks.
quality = pd.DataFrame({
    "check": ["row_count", "duplicate_transaction_ids", "missing_values_total", "invalid_amount_rows"],
    "result": [len(df), int(df["transaction_id"].duplicated().sum()), int(df.isna().sum().sum()), int((df["amount_inr"] <= 0).sum())]
})
quality.to_csv(OUT / "data_quality_checks.csv", index=False)

# 3. Calculate the headline metrics.
success = df[df["status"] == "SUCCESS"]
metrics = pd.DataFrame([
    ("Total transactions", len(df)),
    ("Total attempted transaction value (INR)", round(df["amount_inr"].sum(), 2)),
    ("Successful transactions", len(success)),
    ("Failed transactions", int((df["status"] == "FAILED").sum())),
    ("Pending transactions", int((df["status"] == "PENDING").sum())),
    ("Success rate (%)", round((df["status"] == "SUCCESS").mean() * 100, 2)),
    ("Successful transaction value (INR)", round(success["amount_inr"].sum(), 2)),
    ("Average successful transaction value (INR)", round(success["amount_inr"].mean(), 2)),
], columns=["metric", "value"])
metrics.to_csv(OUT / "headline_metrics.csv", index=False)

# 4. Export breakdown tables for Excel / Power BI.
monthly = df.groupby("month", dropna=False).agg(
    transaction_count=("transaction_id", "count"),
    attempted_value_inr=("amount_inr", "sum"),
    successful_count=("status", lambda s: (s == "SUCCESS").sum()),
).reset_index()
monthly.to_csv(OUT / "monthly_summary.csv", index=False)
status = df.groupby("status").agg(transaction_count=("transaction_id", "count"), amount_inr=("amount_inr", "sum")).reset_index()
status.to_csv(OUT / "status_summary.csv", index=False)
city = df.groupby("city").agg(transaction_count=("transaction_id", "count"), attempted_value_inr=("amount_inr", "sum")).sort_values("transaction_count", ascending=False).reset_index()
city.to_csv(OUT / "city_summary.csv", index=False)
category = df.groupby("merchant_category").agg(transaction_count=("transaction_id", "count"), attempted_value_inr=("amount_inr", "sum")).sort_values("transaction_count", ascending=False).reset_index()
category.to_csv(OUT / "category_summary.csv", index=False)
hourly = df.groupby("hour", dropna=False).agg(transaction_count=("transaction_id", "count")).reset_index()
hourly.to_csv(OUT / "hourly_summary.csv", index=False)

# 5. Create simple charts. Matplotlib uses its default color palette.
plt.figure(figsize=(10, 5))
plt.plot(monthly["month"], monthly["transaction_count"], marker="o")
plt.title("Monthly Transaction Count")
plt.xlabel("Month")
plt.ylabel("Number of transactions")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUT / "monthly_transaction_count.png", dpi=150)
plt.close()

plt.figure(figsize=(7, 5))
plt.bar(status["status"], status["transaction_count"])
plt.title("Transactions by Status")
plt.xlabel("Status")
plt.ylabel("Number of transactions")
plt.tight_layout()
plt.savefig(OUT / "transactions_by_status.png", dpi=150)
plt.close()

plt.figure(figsize=(10, 5))
plt.bar(hourly["hour"].astype("Int64").astype(str), hourly["transaction_count"])
plt.title("Transactions by Hour of Day")
plt.xlabel("Hour (0–23)")
plt.ylabel("Number of transactions")
plt.tight_layout()
plt.savefig(OUT / "transactions_by_hour.png", dpi=150)
plt.close()

print("Analysis complete. Output files saved in:", OUT)
print("\nHeadline metrics:\n", metrics.to_string(index=False))
print("\nData quality checks:\n", quality.to_string(index=False))
