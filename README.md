# UPI Transaction Analysis Dashboard

A beginner-friendly data analytics portfolio project that explores UPI-style payment transactions using Python, SQL, Excel, and Power BI.

> **Data notice:** `data/upi_transactions_sample.csv` is a synthetic dataset created for practice. It is not real PhonePe data and contains no real customer information. Do not describe the findings as PhonePe's actual business results.

## Business questions

1. How many transactions were recorded, and what was their total value?
2. What percentage of transactions succeeded, failed, or remained pending?
3. How do transaction count and transaction value change month by month?
4. Which cities and merchant categories have the most activity?
5. Which hours have the highest transaction volume?
6. What is the average transaction value for successful payments?

## Project files

- `data/upi_transactions_sample.csv` — 1,200 sample transactions.
- `python/analyze_transactions.py` — cleans and analyzes the data, then saves summary CSVs and charts.
- `sql/analysis_queries.sql` — SQL queries for key business questions.
- `POWER_BI_GUIDE.md` — steps to build a dashboard in Power BI.
- `EXCEL_GUIDE.md` — steps to explore the dataset in Excel.
- `requirements.txt` — Python library needed for the analysis.

## Run the Python analysis

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Install the required package:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the analysis:

   ```bash
   python python/analyze_transactions.py
   ```

The script creates an `outputs/` folder containing summary tables and PNG charts.

## Build the dashboard

Follow `POWER_BI_GUIDE.md` to import the CSV into Power BI and create KPI cards, monthly trends, status breakdowns, city/category comparisons, and an hourly chart. You can also use the same CSV in Excel following `EXCEL_GUIDE.md`.

## Important definitions

- **Transaction count:** number of transaction records.
- **Transaction value:** sum of transaction amounts. This is the value attempted, unless filtered to successful transactions.
- **Success rate:** successful transactions divided by all transactions, multiplied by 100.
- **Average successful transaction value:** average amount among successful transactions only.

## How to discuss this project in an interview

Explain the question you wanted to answer, how you checked and cleaned the data, what each metric means, and what the charts show after you run the analysis. Only report actual values produced by your own run. Do not claim that this is production work or real PhonePe data.

## Next improvement ideas

- Add more months of sample data and compare periods.
- Add a filter for payment method and merchant category in Power BI.
- Create a separate page focused on failed and pending payments.
- Add screenshots of your finished dashboard to the `images/` folder.
