-- ==========================================================
-- Day 22: Window Functions II (Value Functions) Practice
-- ==========================================================

-- 1. Setup Monthly Revenue Dataset
DROP TABLE IF EXISTS monthly_sales;

CREATE TABLE monthly_sales (
    record_id INT PRIMARY KEY,
    sales_rep VARCHAR(50) NOT NULL,
    sales_month DATE NOT NULL,
    revenue DECIMAL(10, 2) NOT NULL
);

INSERT INTO monthly_sales (record_id, sales_rep, sales_month, revenue) VALUES
(1, 'Aarav Sharma', '2026-01-01', 40000.00),
(2, 'Aarav Sharma', '2026-02-01', 45000.00),
(3, 'Aarav Sharma', '2026-03-01', 42000.00),
(4, 'Aarav Sharma', '2026-04-01', 58000.00),
(5, 'Neha Patel',   '2026-01-01', 50000.00),
(6, 'Neha Patel',   '2026-02-01', 55000.00),
(7, 'Neha Patel',   '2026-03-01', 55000.00),
(8, 'Neha Patel',   '2026-04-01', 72000.00);

-- ==========================================================
-- 2. LAG: Month-over-Month (MoM) Growth Analysis
-- ==========================================================

-- Compare current month's revenue against previous month
SELECT 
    sales_rep,
    sales_month,
    revenue AS current_revenue,
    LAG(revenue, 1) OVER (
        PARTITION BY sales_rep 
        ORDER BY sales_month ASC
    ) AS prior_month_revenue,
    revenue - LAG(revenue, 1, revenue) OVER (
        PARTITION BY sales_rep 
        ORDER BY sales_month ASC
    ) AS revenue_variance,
    ROUND(
        (revenue - LAG(revenue, 1) OVER (PARTITION BY sales_rep ORDER BY sales_month ASC))
        / NULLIF(LAG(revenue, 1) OVER (PARTITION BY sales_rep ORDER BY sales_month ASC), 0) * 100,
        2
    ) AS mom_growth_pct
FROM monthly_sales
ORDER BY sales_rep, sales_month;

-- ==========================================================
-- 3. LEAD: Next Event Lookahead
-- ==========================================================

-- Peek ahead to next month's performance
SELECT 
    sales_rep,
    sales_month,
    revenue,
    LEAD(revenue, 1, 0.00) OVER (
        PARTITION BY sales_rep 
        ORDER BY sales_month ASC
    ) AS target_next_month_revenue
FROM monthly_sales
ORDER BY sales_rep, sales_month;

-- ==========================================================
-- 4. FIRST_VALUE & Baseline Comparisons
-- ==========================================================

-- Compare each month's performance directly against the Q1 starting baseline (Jan 2026)
SELECT 
    sales_rep,
    sales_month,
    revenue,
    FIRST_VALUE(revenue) OVER (
        PARTITION BY sales_rep 
        ORDER BY sales_month ASC
    ) AS base_january_revenue,
    revenue - FIRST_VALUE(revenue) OVER (
        PARTITION BY sales_rep 
        ORDER BY sales_month ASC
    ) AS growth_since_january
FROM monthly_sales
ORDER BY sales_rep, sales_month;

-- ==========================================================
-- 5. LAST_VALUE: Safe Frame Specification
-- ==========================================================

-- Pull the peak revenue month in partition using explicit frame extension
SELECT 
    sales_rep,
    sales_month,
    revenue,
    LAST_VALUE(revenue) OVER (
        PARTITION BY sales_rep 
        ORDER BY revenue ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS peak_revenue_achieved
FROM monthly_sales
ORDER BY sales_rep, sales_month;
