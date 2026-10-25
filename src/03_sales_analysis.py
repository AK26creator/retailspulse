from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

PROJECT_DIR = Path(__file__).resolve().parents[1]

DATA_FILE = PROJECT_DIR / "data" / "retail_cleaned.csv"
REPORT_DIR = PROJECT_DIR / "reports"

df = pd.read_csv(DATA_FILE, parse_dates=["InvoiceDate"])

# Monthly revenue
monthly = (
    df.groupby("YearMonth", as_index=False)["Revenue"]
    .sum()
    .sort_values("YearMonth")
)

monthly["Revenue_Change_Pct"] = (
    monthly["Revenue"].pct_change() * 100
)

print("\n--- MONTHLY SALES ---")
print(monthly.to_string(index=False))

# Top products
top_products = (
    df.groupby("StockCode", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Units_Sold=("Quantity", "sum"),
        Product_Name=("Description", "first")
    )
    .sort_values("Revenue", ascending=False)
    .head(10)
)

print("\n--- TOP PRODUCTS ---")
print(top_products.to_string(index=False))

# Country performance
country_sales = (
    df.groupby("Country", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Invoices=("Invoice", "nunique")
    )
    .sort_values("Revenue", ascending=False)
    .head(10)
)

print("\n--- TOP COUNTRIES ---")
print(country_sales.to_string(index=False))

# Plot monthly revenue
sns.set_theme(style="whitegrid")

plt.figure(figsize=(12, 6))
sns.lineplot(
    data=monthly,
    x="YearMonth",
    y="Revenue",
    marker="o"
)

plt.title("RetailPulse: Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(REPORT_DIR / "monthly_revenue.png", dpi=150)
plt.close()

# Plot top products
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_products,
    x="Revenue",
    y="StockCode"
)

plt.title("RetailPulse: Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product Code")
plt.tight_layout()

plt.savefig(REPORT_DIR / "top_products.png", dpi=150)
plt.close()

# Plot country performance
plt.figure(figsize=(12, 6))
sns.barplot(
    data=country_sales,
    x="Revenue",
    y="Country"
)

plt.title("RetailPulse: Top 10 Countries by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig(REPORT_DIR / "country_sales.png", dpi=150)
plt.close()

# Data-quality summary
quality_summary = pd.DataFrame({
    "Metric": [
        "Rows",
        "Unique invoices",
        "Unique identified customers",
        "Missing customer IDs",
        "Total revenue",
        "Total units sold"
    ],
    "Value": [
        len(df),
        df["Invoice"].nunique(),
        df["Customer_ID"].nunique(),
        df["Customer_ID"].isna().sum(),
        df["Revenue"].sum(),
        df["Quantity"].sum()
    ]
})

quality_summary.to_csv(
    REPORT_DIR / "quality_summary.csv",
    index=False
)

print("\nCharts and summary saved to:", REPORT_DIR)