-- ==========================================================
-- Day 21: Window Functions I (Ranking & Numbering)
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Data
DROP TABLE IF EXISTS sales_records;

CREATE TABLE sales_records (
    sale_id INT PRIMARY KEY,
    sales_rep VARCHAR(50) NOT NULL,
    region VARCHAR(50) NOT NULL,
    quarter_name VARCHAR(10) NOT NULL,
    revenue DECIMAL(10, 2) NOT NULL
);

INSERT INTO sales_records (sale_id, sales_rep, region, quarter_name, revenue) VALUES
(101, 'Aarav Sharma', 'South', 'Q1', 45000.00),
(102, 'Priya Nair', 'South', 'Q1', 52000.00),
(103, 'Kavya Rao', 'South', 'Q1', 52000.00), -- Tie with Priya
(104, 'Ananya Sen', 'South', 'Q1', 31000.00),
(105, 'Neha Patel', 'West', 'Q1', 75000.00),
(106, 'Vikram Singh', 'West', 'Q1', 75000.00), -- Tie with Neha
(107, 'Rohan Verma', 'West', 'Q1', 60000.00),
(108, 'Amit Kumar', 'West', 'Q1', 42000.00);

-- ==========================================================
-- 2. Side-by-Side Comparison: ROW_NUMBER, RANK, DENSE_RANK
-- ==========================================================

-- Observe how ties are resolved in each region
SELECT 
    sales_rep,
    region,
    revenue,
    ROW_NUMBER() OVER (PARTITION BY region ORDER BY revenue DESC) AS row_num,
    RANK() OVER (PARTITION BY region ORDER BY revenue DESC) AS rank_with_gaps,
    DENSE_RANK() OVER (PARTITION BY region ORDER BY revenue DESC) AS rank_continuous
FROM sales_records
ORDER BY region, revenue DESC;

-- ==========================================================
-- 3. Top-N Analysis per Group using CTE
-- ==========================================================

-- Extract the top 2 revenue generators for each region
-- DENSE_RANK ensures tied top performers are both captured
WITH regional_rankings AS (
    SELECT 
        sales_rep,
        region,
        revenue,
        DENSE_RANK() OVER (PARTITION BY region ORDER BY revenue DESC) AS performance_tier
    FROM sales_records
)
SELECT 
    region,
    performance_tier,
    sales_rep,
    revenue
FROM regional_rankings
WHERE performance_tier <= 2
ORDER BY region, performance_tier;

-- ==========================================================
-- 4. Statistical Binning with NTILE
-- ==========================================================

-- Split reps into 2 equal performance tiers (Tier 1: Top 50%, Tier 2: Bottom 50%)
SELECT 
    sales_rep,
    region,
    revenue,
    NTILE(2) OVER (ORDER BY revenue DESC) AS performance_half
FROM sales_records
ORDER BY performance_half, revenue DESC;

-- ==========================================================
-- 5. Deduplication Pattern using ROW_NUMBER
-- ==========================================================

-- Pattern: If duplicate events or logs occur, assign ROW_NUMBER and delete/filter where rn > 1
WITH ranked_transactions AS (
    SELECT 
        sale_id,
        sales_rep,
        revenue,
        ROW_NUMBER() OVER (PARTITION BY sales_rep, revenue ORDER BY sale_id ASC) AS occurrence_rank
    FROM sales_records
)
SELECT 
    sale_id,
    sales_rep,
    revenue
FROM ranked_transactions
WHERE occurrence_rank = 1;
