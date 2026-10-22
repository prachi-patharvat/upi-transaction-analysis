# Power BI Dashboard Guide

## Import the data
1. Open Power BI Desktop.
2. Choose **Get data → Text/CSV**.
3. Select `data/upi_transactions_sample.csv` and load it.
4. In Power Query, confirm `transaction_date` is Date, `amount_inr` is Decimal Number, and the remaining columns are text unless you create an hour number.

## Suggested one-page layout

### KPI cards
- Total transactions: count of `transaction_id`
- Total attempted value: sum of `amount_inr`
- Successful transactions: count filtered to `status = SUCCESS`
- Success rate: successful transaction count divided by total transaction count

### Charts
- Line chart: `transaction_date` by month vs transaction count
- Donut chart: `status` vs transaction count
- Bar chart: `city` vs transaction count
- Bar chart: `merchant_category` vs transaction count
- Column chart: transaction hour vs transaction count
- Slicers: city, status, payment method, merchant category

## Example DAX measures

```DAX
Total Transactions = COUNTROWS(transactions)

Attempted Value INR = SUM(transactions[amount_inr])

Successful Transactions =
CALCULATE(COUNTROWS(transactions), transactions[status] = "SUCCESS")

Success Rate % = DIVIDE([Successful Transactions], [Total Transactions], 0)
```

Format `Success Rate %` as Percentage. If your imported table has a different name, replace `transactions` with the actual table name.

## Screenshot for GitHub
When the dashboard is ready, take a screenshot and save it in the project's `images/` folder. Do not add a screenshot until you have actually built the dashboard.
