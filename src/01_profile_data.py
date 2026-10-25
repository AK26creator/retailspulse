from pathlib import Path

import pandas as pd

# Locate the project directory
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Locate the raw dataset
file_path = PROJECT_DIR / "data" / "online_retail_II.xlsx"

# Read the first worksheet
df = pd.read_excel(file_path, sheet_name=0)

# Display the first five records
print("\n--- FIRST FIVE RECORDS ---")
print(df.head())

# Display the number of rows and columns
print("\n--- DATASET SIZE ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Display column names and data types
print("\n--- DATA TYPES ---")
print(df.info())

# Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Check duplicate rows
print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

# Statistical summary
print("\n--- STATISTICAL SUMMARY ---")
print(df.describe(include="all").T)

# Save the profiling report
report_path = PROJECT_DIR / "reports" / "data_profile.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(f"Rows: {df.shape[0]}\n")
    file.write(f"Columns: {df.shape[1]}\n\n")
    file.write("Missing values:\n")
    file.write(df.isnull().sum().to_string())
    file.write("\n\nDuplicate rows:\n")
    file.write(str(df.duplicated().sum()))
    file.write("\n\nStatistical summary:\n")
    file.write(df.describe(include="all").T.to_string())

print("\nProfiling complete!")
print("Report saved to:", report_path)