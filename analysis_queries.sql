-- UPI Transaction Analysis Dashboard
-- Example SQL uses SQLite-compatible syntax.
-- First import data/upi_transactions_sample.csv into a table named transactions.

-- 1. Total transactions and attempted transaction value
SELECT COUNT(*) AS total_transactions,
       ROUND(SUM(amount_inr), 2) AS attempted_value_inr
FROM transactions;

-- 2. Count and value by transaction status
SELECT status,
       COUNT(*) AS transaction_count,
       ROUND(SUM(amount_inr), 2) AS amount_inr
FROM transactions
GROUP BY status
ORDER BY transaction_count DESC;

-- 3. Success rate
SELECT ROUND(100.0 * SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) / COUNT(*), 2)
       AS success_rate_percent
FROM transactions;

-- 4. Monthly trend (SQLite date functions)
SELECT strftime('%Y-%m', transaction_date) AS month,
       COUNT(*) AS transaction_count,
       ROUND(SUM(amount_inr), 2) AS attempted_value_inr
FROM transactions
GROUP BY strftime('%Y-%m', transaction_date)
ORDER BY month;

-- 5. Cities with the most transactions
SELECT city, COUNT(*) AS transaction_count,
       ROUND(SUM(amount_inr), 2) AS attempted_value_inr
FROM transactions
GROUP BY city
ORDER BY transaction_count DESC;

-- 6. Merchant categories by transaction count
SELECT merchant_category, COUNT(*) AS transaction_count,
       ROUND(SUM(amount_inr), 2) AS attempted_value_inr
FROM transactions
GROUP BY merchant_category
ORDER BY transaction_count DESC;

-- 7. Average amount for successful transactions only
SELECT ROUND(AVG(amount_inr), 2) AS average_successful_amount_inr
FROM transactions
WHERE status = 'SUCCESS';

-- 8. Hourly transaction activity (transaction_time is stored as HH:MM:SS)
SELECT CAST(substr(transaction_time, 1, 2) AS INTEGER) AS transaction_hour,
       COUNT(*) AS transaction_count
FROM transactions
GROUP BY transaction_hour
ORDER BY transaction_hour;

-- 9. Review failed transactions for investigation (not a fraud conclusion)
SELECT transaction_id, transaction_date, transaction_time, amount_inr, city, payment_method
FROM transactions
WHERE status = 'FAILED'
ORDER BY amount_inr DESC;
