```sql
-- ==========================================================
-- Day 10: Aggregate Functions & NULL Handling Hands-On Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Records
DROP TABLE IF EXISTS company_sales;

CREATE TABLE company_sales (
    sale_id INT PRIMARY KEY,
    rep_name VARCHAR(50) NOT NULL,
    region VARCHAR(50) NOT NULL,
    deal_size DECIMAL(10, 2), -- Nullable to simulate pending/unvalued deals
    discount_pct DECIMAL(4, 2), -- Nullable
    deal_status VARCHAR(20) NOT NULL
);

INSERT INTO company_sales (sale_id, rep_name, region, deal_size, discount_pct, deal_status)
VALUES 
    (1, 'Aarav Sharma', 'South', 150000.00, 0.10, 'WON'),
    (2, 'Neha Patel', 'West', 280000.00, 0.15, 'WON'),
    (3, 'Rohan Verma', 'North', NULL, NULL, 'LOST'),
    (4, 'Priya Nair', 'South', 95000.00, 0.05, 'WON'),
    (5, 'Vikram Singh', 'West', 120000.00, NULL, 'WON'),
    (6, 'Aarav Sharma', 'South', 210000.00, 0.20, 'WON'),
    (7, 'Ananya Sen', 'East', 60000.00, 0.00, 'WON'),
    (8, 'Neha Patel', 'West', NULL, NULL, 'IN_PIPELINE'),
    (9, 'Rohan Verma', 'North', 175000.00, 0.08, 'WON'),
    (10, 'Priya Nair', 'South', 310000.00, 0.25, 'WON');

-- ==========================================================
-- 2. Basic Aggregate Statistics
-- ==========================================================

-- High-level summary of all closed and open business
SELECT 
    COUNT(*) AS total_pipeline_records,
    COUNT(deal_size) AS deals_with_values,
    SUM(deal_size) AS total_pipeline_value,
    ROUND(AVG(deal_size), 2) AS average_deal_value,
    MIN(deal_size) AS smallest_deal,
    MAX(deal_size) AS largest_deal
FROM company_sales;

-- ==========================================================
-- 3. The Difference Between COUNT Variants
-- ==========================================================

SELECT 
    COUNT(*) AS all_rows,
    COUNT(discount_pct) AS non_null_discounts,
    COUNT(DISTINCT rep_name) AS unique_sales_reps,
    COUNT(DISTINCT region) AS active_territories
FROM company_sales;

-- ==========================================================
-- 4. NULL Impact on Averages
-- ==========================================================

-- Standard AVG ignores rows where discount_pct is NULL
-- Coalesced AVG treats NULL as 0% discount
SELECT 
    ROUND(AVG(discount_pct) * 100, 2) AS avg_discount_given_to_discounted_deals,
    ROUND(AVG(COALESCE(discount_pct, 0.00)) * 100, 2) AS avg_discount_across_all_deals
FROM company_sales;

-- ==========================================================
-- 5. Conditional Aggregation (SUM/COUNT with CASE WHEN)
-- ==========================================================

-- Calculate pipeline metrics in a single query pass
SELECT 
    COUNT(*) AS total_deals,
    COUNT(CASE WHEN deal_status = 'WON' THEN 1 END) AS won_deals_count,
    COUNT(CASE WHEN deal_status = 'LOST' THEN 1 END) AS lost_deals_count,
    COUNT(CASE WHEN deal_status = 'IN_PIPELINE' THEN 1 END) AS pending_deals_count,
    SUM(CASE WHEN deal_status = 'WON' THEN deal_size ELSE 0 END) AS realized_revenue,
    ROUND(
        (COUNT(CASE WHEN deal_status = 'WON' THEN 1 END)::DECIMAL / COUNT(*)) * 100, 
        2
    ) AS win_rate_percentage
FROM company_sales;

