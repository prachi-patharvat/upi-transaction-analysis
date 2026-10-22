# Excel Analysis Guide

1. Open `data/upi_transactions_sample.csv` in Excel.
2. Select the data and press **Ctrl+T** to turn it into a table.
3. Check that `transaction_date` is recognized as a date and `amount_inr` as a number.
4. Create a PivotTable:
   - **Transactions by status:** Rows = `status`; Values = Count of `transaction_id` and Sum of `amount_inr`.
   - **Monthly trend:** Rows = `transaction_date` (group by Months); Values = Count of `transaction_id` and Sum of `amount_inr`.
   - **City comparison:** Rows = `city`; Values = Count of `transaction_id`.
   - **Category comparison:** Rows = `merchant_category`; Values = Count of `transaction_id`.
5. Insert a line chart for monthly trends and bar charts for status, city, and category.
6. Add a title, clear labels, and a short note: “Synthetic sample data for learning; not actual PhonePe data.”
