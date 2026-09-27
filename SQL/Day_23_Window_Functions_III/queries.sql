-- ==========================================================
-- Day 23: Window Functions III Practice (MySQL 8.0+ Compatible)
-- ==========================================================

USE retail_analytics;

DROP TABLE IF EXISTS daily_branch_revenue;

CREATE TABLE daily_branch_revenue (
    record_id INT PRIMARY KEY,
    branch_name VARCHAR(50) NOT NULL,
    sale_date DATE NOT NULL,
    revenue DECIMAL(10, 2) NOT NULL
);

INSERT INTO daily_branch_revenue (record_id, branch_name, sale_date, revenue) VALUES
(1,  'Indiranagar Flagship', '2026-09-01', 12000.00),
(2,  'Indiranagar Flagship', '2026-09-02', 15000.00),
(3,  'Indiranagar Flagship', '2026-09-03', 9000.00),
(4,  'Indiranagar Flagship', '2026-09-04', 18000.00),
(5,  'Indiranagar Flagship', '2026-09-05', 22000.00),
(6,  'Indiranagar Flagship', '2026-09-06', 14000.00),
(7,  'Indiranagar Flagship', '2026-09-07', 25000.00),
(8,  'Hitec City Store',     '2026-09-01', 8000.00),
(9,  'Hitec City Store',     '2026-09-02', 11000.00),
(10, 'Hitec City Store',     '2026-09-03', 13000.00),
(11, 'Hitec City Store',     '2026-09-04', 17000.00),
(12, 'Hitec City Store',     '2026-09-05', 16000.00);

-- ==========================================================
-- 1. Cumulative Running Total
-- ==========================================================

-- Running revenue total by branch over time
SELECT 
    branch_name,
    sale_date,
    revenue,
    SUM(revenue) OVER (
        PARTITION BY branch_name 
        ORDER BY sale_date ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue
FROM daily_branch_revenue
ORDER BY branch_name, sale_date;

-- ==========================================================
-- 2. 3-Day Trailing Moving Average (Smoothing)
-- ==========================================================

-- Computes average of the current day and the previous 2 days
SELECT 
    branch_name,
    sale_date,
    revenue,
    ROUND(
        AVG(revenue) OVER (
            PARTITION BY branch_name 
            ORDER BY sale_date ASC
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ), 2
    ) AS rolling_3day_avg
FROM daily_branch_revenue
ORDER BY branch_name, sale_date;

-- ==========================================================
-- 3. Centered Moving Window (1 Preceding, 1 Following)
-- ==========================================================

SELECT 
    branch_name,
    sale_date,
    revenue,
    ROUND(
        AVG(revenue) OVER (
            PARTITION BY branch_name 
            ORDER BY sale_date ASC
            ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
        ), 2
    ) AS centered_3day_avg
FROM daily_branch_revenue
ORDER BY branch_name, sale_date;

-- ==========================================================
-- 4. Rolling Maximum & Minimum
-- ==========================================================

-- Track peak daily revenue in a rolling 3-day window
SELECT 
    branch_name,
    sale_date,
    revenue,
    MAX(revenue) OVER (
        PARTITION BY branch_name 
        ORDER BY sale_date ASC
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS max_revenue_last_3days,
    MIN(revenue) OVER (
        PARTITION BY branch_name 
        ORDER BY sale_date ASC
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS min_revenue_last_3days
FROM daily_branch_revenue
ORDER BY branch_name, sale_date;

-- ==========================================================
-- 5. Partition Benchmark Comparison
-- ==========================================================

-- Compare individual day revenue against total branch revenue
SELECT 
    branch_name,
    sale_date,
    revenue,
    SUM(revenue) OVER (PARTITION BY branch_name) AS total_branch_revenue,
    ROUND(
        (revenue / SUM(revenue) OVER (PARTITION BY branch_name)) * 100, 
        2
    ) AS pct_of_total_branch_revenue
FROM daily_branch_revenue
ORDER BY branch_name, sale_date;
