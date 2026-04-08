-- ============================================================================
-- CLINIC MANAGEMENT SYSTEM - QUERIES
-- ============================================================================
-- Business analytics queries for clinic sales, expenses, and profitability
-- ============================================================================

-- ============================================================================
-- Q1: REVENUE BY SALES CHANNEL
-- ============================================================================
-- Scenario: How much revenue did each sales channel generate?
-- Result: Total sales amount grouped and ranked by channel

SELECT 
    sales_channel,
    COUNT(*) AS number_of_sales,
    SUM(amount) AS total_revenue,
    AVG(amount) AS average_sale
FROM clinic_sales
GROUP BY sales_channel
ORDER BY total_revenue DESC;

-- ============================================================================
-- Q2: TOTAL REVENUE AND EXPENSES (Monthly Overview)
-- ============================================================================
-- Scenario: Get total revenue, expenses, and profit for November 2021
-- Logic: Sum all sales and sum all expenses, then calculate profit/loss

SELECT 
    'November 2021' AS period,
    (SELECT SUM(amount) FROM clinic_sales) AS total_revenue,
    (SELECT SUM(amount) FROM expenses) AS total_expenses,
    ((SELECT SUM(amount) FROM clinic_sales) - (SELECT SUM(amount) FROM expenses)) AS profit_loss;

-- ============================================================================
-- Q3: DAILY PROFIT/LOSS ANALYSIS
-- ============================================================================
-- Scenario: Show profit/loss for each day (sales minus expenses on that day)
-- Logic: Group sales by date, group expenses by date, then calculate difference
-- Note: Uses COALESCE to handle dates with no sales or no expenses

SELECT 
    COALESCE(DATE(cs.sale_date), DATE(e.expense_date)) AS transaction_date,
    COALESCE(SUM(cs.amount), 0) AS daily_revenue,
    COALESCE(SUM(e.amount), 0) AS daily_expenses,
    COALESCE(SUM(cs.amount), 0) - COALESCE(SUM(e.amount), 0) AS daily_profit_loss
FROM clinic_sales cs
FULL OUTER JOIN expenses e 
    ON DATE(cs.sale_date) = DATE(e.expense_date)
GROUP BY COALESCE(DATE(cs.sale_date), DATE(e.expense_date))
ORDER BY transaction_date;

-- Alternative for MySQL (FULL OUTER JOIN not supported):
-- ============================================================================
-- Q3: DAILY PROFIT/LOSS ANALYSIS (MySQL Compatible)
-- ============================================================================

SELECT 
    transaction_date,
    COALESCE(daily_revenue, 0) AS daily_revenue,
    COALESCE(daily_expenses, 0) AS daily_expenses,
    COALESCE(daily_revenue, 0) - COALESCE(daily_expenses, 0) AS daily_profit_loss
FROM (
    SELECT DATE(sale_date) AS transaction_date, SUM(amount) AS daily_revenue
    FROM clinic_sales
    GROUP BY DATE(sale_date)
) sales_by_day
LEFT JOIN (
    SELECT DATE(expense_date) AS transaction_date, SUM(amount) AS daily_expenses
    FROM expenses
    GROUP BY DATE(expense_date)
) expenses_by_day
ON sales_by_day.transaction_date = expenses_by_day.transaction_date

UNION ALL

SELECT 
    transaction_date,
    0 AS daily_revenue,
    daily_expenses,
    -daily_expenses AS daily_profit_loss
FROM (
    SELECT DATE(expense_date) AS transaction_date, SUM(amount) AS daily_expenses
    FROM expenses
    GROUP BY DATE(expense_date)
) expenses_by_day
LEFT JOIN (
    SELECT DATE(sale_date) AS transaction_date
    FROM clinic_sales
    GROUP BY DATE(sale_date)
) sales_by_day
ON expenses_by_day.transaction_date = sales_by_day.transaction_date
WHERE sales_by_day.transaction_date IS NULL
ORDER BY transaction_date;

-- ============================================================================
-- Q4: PROFITABILITY BY SALES CHANNEL
-- ============================================================================
-- Scenario: Which channel is most profitable after accounting 
-- for proportional expenses?
-- Logic: Calculate revenue by channel, allocate expenses proportionally

SELECT 
    cs.sales_channel,
    SUM(cs.amount) AS channel_revenue,
    ROUND(
        SUM(cs.amount) * CAST(SUM(e.amount) AS DECIMAL) / 
        (SELECT SUM(amount) FROM clinic_sales),
        2
    ) AS allocated_expenses,
    ROUND(
        SUM(cs.amount) - 
        (SUM(cs.amount) * CAST(SUM(e.amount) AS DECIMAL) / 
         (SELECT SUM(amount) FROM clinic_sales)),
        2
    ) AS channel_profit
FROM clinic_sales cs
CROSS JOIN expenses e
GROUP BY cs.sales_channel
ORDER BY channel_profit DESC;

-- ============================================================================
-- Q5: HIGH-VALUE SALES SUMMARY
-- ============================================================================
-- Scenario: Identify high-value transactions (top 3 sales)

SELECT 
    sale_id,
    sales_channel,
    amount,
    sale_date,
    RANK() OVER (ORDER BY amount DESC) AS sales_rank
FROM clinic_sales
WHERE RANK() OVER (ORDER BY amount DESC) <= 3
ORDER BY sales_rank;

-- MySQL compatible version (no window functions in WHERE):
SELECT 
    sale_id,
    sales_channel,
    amount,
    sale_date,
    RANK() OVER (ORDER BY amount DESC) AS sales_rank
FROM clinic_sales
ORDER BY amount DESC
LIMIT 3;

-- ============================================================================
-- BONUS: EXPENSE DETAILS
-- ============================================================================
-- Shows when expenses were incurred and identifies peak expense days

SELECT 
    expense_id,
    amount,
    expense_date,
    ROUND(amount / (SELECT SUM(amount) FROM expenses) * 100, 2) AS percentage_of_total
FROM expenses
ORDER BY amount DESC;
