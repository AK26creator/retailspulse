# RetailPulse — Retail Sales Analytics & Customer Intelligence

RetailPulse is an end-to-end retail analytics project that transforms retail transaction data into actionable business insights using Python, MySQL, and Power BI.

The project covers data profiling, data cleaning, SQL-based analysis, KPI development, and interactive dashboard reporting.

## Project Overview

Retail businesses generate large amounts of transaction data. Analyzing this data helps identify revenue trends, understand customer activity, and evaluate product and geographical sales performance.

RetailPulse demonstrates how raw transaction data can be processed, analyzed, and presented through an interactive business intelligence dashboard.

## Technology Stack

* Python
* Pandas
* MySQL
* SQL
* Microsoft Power BI

## Project Workflow

1. Profile the source dataset using Python.
2. Identify missing values, duplicate records, and invalid transactions.
3. Clean the data and calculate transaction revenue.
4. Load the processed data into MySQL.
5. Write SQL queries to analyze sales performance.
6. Connect MySQL to Power BI.
7. Build an interactive dashboard with KPIs, charts, and filters.

## Dashboard Features

The Power BI dashboard includes:

* **Total Revenue:** Sum of transaction revenue.
* **Total Orders:** Distinct invoice count.
* **Units Sold:** Total quantity sold.
* **Unique Customers:** Distinct customer count.
* **Monthly Revenue Trend:** Revenue changes over time.
* **Top 10 Products:** Products ranked by revenue.
* **Revenue by Country:** Geographical sales comparison.
* **Country Filter:** Interactive filtering of dashboard results.

## Data Preparation

The project uses the Online Retail II dataset.

The cleaning workflow includes:

* Inspecting data quality and structure.
* Removing duplicate records.
* Removing records with missing required transaction fields.
* Excluding non-positive quantities and prices.
* Calculating revenue as quantity multiplied by unit price.
* Creating year, month, and year-month fields for time-based analysis.

Customer identifiers are not available for every transaction in the original dataset. Customer-related metrics should therefore be interpreted with this limitation in mind.

## Sample Validation

The final MySQL table used for the dashboard contains 2,000 records.

Validation checks confirmed:

* Total records: 2,000
* Distinct transaction combinations: 2,000
* Total sample revenue: 35,849.38
* Revenue calculation mismatches: 0

**Important:** These figures describe the 2,000-row project sample, not the complete original dataset. Dashboard results must not be interpreted as the overall performance of the full retail dataset.

## Repository Structure

```text
RetailPulse/
├── data/
├── reports/
├── src/
├── sql/
├── dashboard/
├── screenshots/
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/RetailPulse.git
cd RetailPulse
```

### 2. Create a Python environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare MySQL

* Install and start MySQL Server.
* Create a database named `retailpulse`.
* Create the `retail_transactions` table using the project's SQL schema.
* Obtain the dataset from the original source and run the Python cleaning workflow.
* Import the prepared data into MySQL.

Database credentials and local machine settings should be configured locally rather than committed to the repository.

### 5. Run the Python workflow

Execute the scripts in the following order:

```bash
python src/01_profile_data.py
python src/02_clean_data.py
python src/03_sales_analysis.py
```

Check each script's input and output paths before running it.

### 6. Open the Power BI dashboard

Open the `.pbix` report from the `dashboard` directory in Power BI Desktop.

Configure the MySQL connection for your own environment if prompted.

## Dataset

Source: UCI Machine Learning Repository — Online Retail II

Dataset information: https://archive.ics.uci.edu/dataset/502/online+retail+ii

The dataset contains historical retail transactions. This project uses a 2,000-row sample for its final dashboard, so findings are illustrative rather than representative of the complete dataset.

## Limitations

* Dashboard results are based on a sample of 2,000 records.
* The source dataset does not provide actual product costs, so profit and profit-margin calculations are not included.
* Customer-level analysis is limited by missing customer identifiers.
* The dashboard describes the available transaction data and does not establish causal relationships.

## Skills Demonstrated

* Data profiling and cleaning
* Python and Pandas
* MySQL database operations
* SQL aggregation and analytical queries
* KPI development
* Power BI dashboard development
* Data validation
* Business insight communication

## Author

Akash Kumar Singh

B.Tech — Artificial Intelligence and Data Science

GitHub: https://github.com/AK26creator
