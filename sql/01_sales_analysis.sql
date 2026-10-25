SELECT
    ROUND(SUM(Revenue), 2) AS total_revenue
FROM retail_transactions;

SELECT
    YearMonth,
    ROUND(SUM(Revenue), 2) AS monthly_revenue
FROM retail_transactions
GROUP BY YearMonth
ORDER BY YearMonth;

SELECT
    StockCode,
    MAX(Description) AS product_name,
    ROUND(SUM(Revenue), 2) AS total_revenue,
    SUM(Quantity) AS units_sold
FROM retail_transactions
GROUP BY StockCode
ORDER BY total_revenue DESC
LIMIT 10;

SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS total_revenue,
    COUNT(DISTINCT Invoice) AS total_invoices
FROM retail_transactions
GROUP BY Country
ORDER BY total_revenue DESC;

SELECT
    Customer_ID,
    COUNT(DISTINCT Invoice) AS order_count,
    ROUND(SUM(Revenue), 2) AS customer_revenue
FROM retail_transactions
WHERE Customer_ID IS NOT NULL
GROUP BY Customer_ID
HAVING COUNT(DISTINCT Invoice) > 1
ORDER BY customer_revenue DESC
LIMIT 20;

WITH monthly_sales AS (
    SELECT
        YearMonth,
        SUM(Revenue) AS revenue
    FROM retail_transactions
    GROUP BY YearMonth
)
SELECT
    YearMonth,
    ROUND(revenue, 2) AS revenue,
    ROUND(
        revenue - LAG(revenue) OVER (ORDER BY YearMonth),
        2
    ) AS revenue_change
FROM monthly_sales
ORDER BY YearMonth;