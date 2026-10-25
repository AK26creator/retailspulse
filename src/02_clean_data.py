
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

RAW_FILE = PROJECT_DIR / "data" / "online_retail_II.xlsx"
OUTPUT_FILE = PROJECT_DIR / "data" / "retail_cleaned.csv"
QUALITY_FILE = PROJECT_DIR / "reports" / "cleaning_report.txt"

# Load the first worksheet
df = pd.read_excel(RAW_FILE, sheet_name=0)

original_rows = len(df)

# Standardize column names
df.columns = [
    str(column).strip().replace(" ", "_")
    for column in df.columns
]

# Convert columns into their expected data types
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], errors="coerce"
)

df["Quantity"] = pd.to_numeric(
    df["Quantity"], errors="coerce"
)

df["Price"] = pd.to_numeric(
    df["Price"], errors="coerce"
)

# Convert Customer_ID to a nullable integer
# Missing customer IDs remain missing rather than becoming zero
df["Customer_ID"] = pd.to_numeric(
    df["Customer_ID"], errors="coerce"
).astype("Int64")

# Remove exact duplicate rows
duplicate_count = int(df.duplicated().sum())
df = df.drop_duplicates().copy()

# Remove rows without essential transaction information
required_columns = [
    "Invoice",
    "Description",
    "InvoiceDate",
    "Quantity",
    "Price"
]

missing_required = int(
    df[required_columns].isna().any(axis=1).sum()
)

df = df.dropna(subset=required_columns).copy()

# Retain positive-quantity, positive-price lines
# for the primary sales analysis
invalid_quantity = int((df["Quantity"] <= 0).sum())
invalid_price = int((df["Price"] <= 0).sum())

df = df[
    (df["Quantity"] > 0) &
    (df["Price"] > 0)
].copy()

# Calculate transaction-line revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# Extract useful date fields
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month

# Count missing customer IDs before saving
missing_customer_ids = int(df["Customer_ID"].isna().sum())

# Save missing values as \N for MySQL LOAD DATA imports
df.to_csv(
    OUTPUT_FILE,
    index=False,
    na_rep=r"\N"
)

# Create cleaning report
with open(QUALITY_FILE, "w", encoding="utf-8") as file:
    file.write("RETAILPULSE DATA CLEANING REPORT\n")
    file.write("=" * 40 + "\n")
    file.write(f"Original rows: {original_rows}\n")
    file.write(
        f"Exact duplicate rows removed: {duplicate_count}\n"
    )
    file.write(
        f"Rows with missing required fields: {missing_required}\n"
    )
    file.write(
        "Rows with non-positive quantities in deduplicated data: "
        f"{invalid_quantity}\n"
    )
    file.write(
        "Rows with non-positive prices in deduplicated data: "
        f"{invalid_price}\n"
    )
    file.write(f"Final rows: {len(df)}\n")
    file.write(
        f"Rows removed overall: {original_rows - len(df)}\n"
    )
    file.write(
        f"Missing customer IDs retained: {missing_customer_ids}\n"
    )
    file.write(f"Final revenue total: {df['Revenue'].sum():.2f}\n")

print("Cleaning completed!")
print("Original rows:", original_rows)
print("Final rows:", len(df))
print("Total revenue:", round(df["Revenue"].sum(), 2))
print("Missing customer IDs retained:", missing_customer_ids)
print("Saved to:", OUTPUT_FILE)

