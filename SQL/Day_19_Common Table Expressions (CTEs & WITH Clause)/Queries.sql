```sql
-- ==========================================================
-- Day 19: Common Table Expressions (CTEs) Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Data
DROP TABLE IF EXISTS deal_records;
DROP TABLE IF EXISTS sales_agents;

CREATE TABLE sales_agents (
    agent_id INT PRIMARY KEY,
    agent_name VARCHAR(50) NOT NULL,
    territory VARCHAR(50) NOT NULL
);

CREATE TABLE deal_records (
    deal_id INT PRIMARY KEY,
    agent_id INT NOT NULL,
    product_line VARCHAR(50) NOT NULL,
    deal_value DECIMAL(10, 2) NOT NULL,
    close_date DATE NOT NULL,
    CONSTRAINT fk_deal_agent FOREIGN KEY (agent_id) REFERENCES sales_agents(agent_id)
);

INSERT INTO sales_agents (agent_id, agent_name, territory) VALUES
(1, 'Aarav Sharma', 'South'),
(2, 'Neha Patel', 'West'),
(3, 'Rohan Verma', 'North'),
(4, 'Priya Nair', 'South'),
(5, 'Vikram Singh', 'West');

INSERT INTO deal_records (deal_id, agent_id, product_line, deal_value, close_date) VALUES
(101, 1, 'Enterprise Cloud', 85000.00, '2026-07-10'),
(102, 1, 'Analytics Suite', 45000.00, '2026-07-22'),
(103, 2, 'Enterprise Cloud', 120000.00, '2026-08-05'),
(104, 3, 'Security Shield', 35000.00, '2026-08-12'),
(105, 4, 'Enterprise Cloud', 95000.00, '2026-08-15'),
(106, 4, 'Analytics Suite', 65000.00, '2026-08-28'),
(107, 5, 'Security Shield', 40000.00, '2026-09-01'),
(108, 2, 'Analytics Suite', 80000.00, '2026-09-05'),
(109, 3, 'Enterprise Cloud', 50000.00, '2026-09-10');

-- ==========================================================
-- 2. Basic Single CTE: Agent Total Performance
-- ==========================================================

-- Summarize each agent's total deal value and filter top closers
WITH agent_performance AS (
    SELECT 
        agent_id,
        COUNT(deal_id) AS total_deals,
        SUM(deal_value) AS total_revenue
    FROM deal_records
    GROUP BY agent_id
)
SELECT 
    sa.agent_name,
    sa.territory,
    ap.total_deals,
    ap.total_revenue
FROM agent_performance ap
INNER JOIN sales_agents sa ON ap.agent_id = sa.agent_id
WHERE ap.total_revenue >= 100000.00
ORDER BY ap.total_revenue DESC;

-- ==========================================================
-- 3. Chaining Multiple CTEs: Territory & Benchmark Pipeline
-- ==========================================================

-- Pipeline:
-- 1. Aggregate revenue by agent
-- 2. Calculate average agent revenue benchmark across company
-- 3. Compare agents against the company benchmark
WITH agent_totals AS (
    SELECT 
        agent_id,
        SUM(deal_value) AS agent_revenue
    FROM deal_records
    GROUP BY agent_id
),
benchmark_metric AS (
    SELECT 
        ROUND(AVG(agent_revenue), 2) AS avg_company_revenue
    FROM agent_totals
)
SELECT 
    sa.agent_name,
    sa.territory,
    at.agent_revenue,
    bm.avg_company_revenue,
    ROUND(at.agent_revenue - bm.avg_company_revenue, 2) AS revenue_delta,
    CASE 
        WHEN at.agent_revenue >= bm.avg_company_revenue THEN 'Above Benchmark'
        ELSE 'Below Benchmark'
    END AS performance_bracket
FROM agent_totals at
INNER JOIN sales_agents sa ON at.agent_id = sa.agent_id
CROSS JOIN benchmark_metric bm
ORDER BY at.agent_revenue DESC;

-- ==========================================================
-- 4. Multi-Stage Transformation: Product Line Market Share
-- ==========================================================

-- 1. Calculate sales per product line
-- 2. Calculate global sales
-- 3. Compute percentage contribution of each product line
WITH product_sales AS (
    SELECT 
        product_line,
        SUM(deal_value) AS product_revenue
    FROM deal_records
    GROUP BY product_line
),
total_sales AS (
    SELECT SUM(deal_value) AS overall_revenue
    FROM deal_records
)
SELECT 
    ps.product_line,
    ps.product_revenue,
    ROUND((ps.product_revenue / ts.overall_revenue) * 100, 2) AS revenue_share_pct
FROM product_sales ps
CROSS JOIN total_sales ts
ORDER BY revenue_share_pct DESC;
