# RetailPulse

Retail transaction data profiling, cleaning, and sales analysis.

## Project contents

- `data/online_retail_II.xlsx` - source workbook
- `data/retail_cleaned.csv` - cleaned transaction data used by the analysis
- `src/01_profile_data.py` - profiles the source workbook
- `src/02_clean_data.py` - cleans the source data and writes a cleaning report
- `src/03_sales_analysis.py` - analyzes cleaned transactions and creates charts
- `sql/01_sales_analysis.sql` - sales-analysis queries for a `retail_transactions` table
- `reports/` - generated reports and charts

## Run the Python pipeline

From the project root, install the dependencies and run the scripts in order:

```powershell
python -m pip install -r requirements.txt
python src/01_profile_data.py
python src/02_clean_data.py
python src/03_sales_analysis.py
```

The scripts read and write files under `data/` and `reports/`.
