-- ==========================================================
-- Day 28: Interview Patterns II Practice (MySQL 8.0+)
-- ==========================================================

USE retail_analytics;

DROP TABLE IF EXISTS user_logins;
DROP TABLE IF EXISTS financial_snapshots;

CREATE TABLE financial_snapshots (
    snapshot_id INT PRIMARY KEY AUTO_INCREMENT,
    calendar_year INT NOT NULL,
    calendar_month INT NOT NULL,
    gross_revenue DECIMAL(12, 2) NOT NULL
);

CREATE TABLE user_logins (
    login_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    login_date DATE NOT NULL
);

-- Seed Financial Data (2025 to 2026 for YoY comparison)
INSERT INTO financial_snapshots (calendar_year, calendar_month, gross_revenue) VALUES
(2025, 1, 100000.00), (2025, 2, 110000.00), (2025, 3, 125000.00),
(2025, 4, 120000.00), (2025, 5, 140000.00), (2025, 6, 150000.00),
(2026, 1, 130000.00), (2026, 2, 145000.00), (2026, 3, 160000.00),
(2026, 4, 155000.00), (2026, 5, 190000.00), (2026, 6, 210000.00);

-- Seed Login Dates (Includes streaks for Gaps & Islands)
INSERT INTO user_logins (user_id, login_date) VALUES
(101, '2026-09-01'),
(101, '2026-09-02'),
(101, '2026-09-03'), -- Streak of 3 days
(101, '2026-09-05'), -- Gap on Sept 4
(101, '2026-09-06'),
(102, '2026-09-01'),
(102, '2026-09-03'),
(102, '2026-09-04');

-- ==========================================================
-- 1. Year-over-Year (YoY) & Month-over-Month (MoM) Growth
-- ==========================================================

WITH revenue_stream AS (
    SELECT 
        calendar_year,
        calendar_month,
        gross_revenue,
        -- Prior month revenue (Lag by 1 row)
        LAG(gross_revenue, 1) OVER (
            ORDER BY calendar_year, calendar_month
        ) AS prev_month_rev,
        -- Prior year same-month revenue (Lag by 12 rows or partition by month)
        LAG(gross_revenue, 1) OVER (
            PARTITION BY calendar_month 
            ORDER BY calendar_year
        ) AS same_month_prev_year_rev
    FROM financial_snapshots
)
SELECT 
    calendar_year,
    calendar_month,
    gross_revenue,
    ROUND(
        (gross_revenue - prev_month_rev) / NULLIF(prev_month_rev, 0) * 100, 
        2
    ) AS mom_growth_pct,
    ROUND(
        (gross_revenue - same_month_prev_year_rev) / NULLIF(same_month_prev_year_rev, 0) * 100, 
        2
    ) AS yoy_growth_pct
FROM revenue_stream
ORDER BY calendar_year, calendar_month;

-- ==========================================================
-- 2. 3-Month Trailing Moving Average
-- ==========================================================

SELECT 
    calendar_year,
    calendar_month,
    gross_revenue,
    ROUND(
        AVG(gross_revenue) OVER (
            ORDER BY calendar_year, calendar_month
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ), 2
    ) AS trailing_3month_avg
FROM financial_snapshots;

-- ==========================================================
-- 3. Customer Retention Cohorts (Using orders from retail schema)
-- ==========================================================

WITH user_first_order AS (
    -- Step 1: Assign each customer their cohort based on first purchase
    SELECT 
        customer_id,
        DATE_FORMAT(MIN(order_date), '%Y-%m-01') AS cohort_month
    FROM orders
    GROUP BY customer_id
),
activity_periods AS (
    -- Step 2: Determine month offset for every order
    SELECT 
        o.customer_id,
        ufo.cohort_month,
        TIMESTAMPDIFF(MONTH, ufo.cohort_month, DATE_FORMAT(o.order_date, '%Y-%m-01')) AS month_number
    FROM orders o
    INNER JOIN user_first_order ufo ON o.customer_id = ufo.customer_id
)
-- Step 3: Count retained customers across offset intervals
SELECT 
    cohort_month,
    COUNT(DISTINCT customer_id) AS total_cohort_users,
    COUNT(DISTINCT CASE WHEN month_number = 0 THEN customer_id END) AS month_0_retained,
    COUNT(DISTINCT CASE WHEN month_number = 1 THEN customer_id END) AS month_1_retained,
    COUNT(DISTINCT CASE WHEN month_number = 2 THEN customer_id END) AS month_2_retained
FROM activity_periods
GROUP BY cohort_month
ORDER BY cohort_month;

-- ==========================================================
-- 4. Gaps and Islands: Detecting Consecutive Login Streaks
-- ==========================================================

WITH distinct_logins AS (
    SELECT DISTINCT user_id, login_date
    FROM user_logins
),
numbered_logins AS (
    SELECT 
        user_id,
        login_date,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) AS rn
    FROM distinct_logins
),
grouped_islands AS (
    -- Subtracting row number days from date produces an invariant group key
    SELECT 
        user_id,
        login_date,
        DATE_SUB(login_date, INTERVAL rn DAY) AS streak_group
    FROM numbered_logins
)
SELECT 
    user_id,
    MIN(login_date) AS streak_start_date,
    MAX(login_date) AS streak_end_date,
    COUNT(*) AS consecutive_active_days
FROM grouped_islands
GROUP BY user_id, streak_group
HAVING COUNT(*) >= 3
ORDER BY user_id, streak_start_date;
