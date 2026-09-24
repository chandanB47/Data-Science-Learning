```sql
-- ==========================================================
-- Day 20: Recursive CTEs Hands-On Practice
-- Compatible with PostgreSQL and MySQL 8.0+
-- ==========================================================

-- 1. Setup Multi-Level Hierarchy Schema
DROP TABLE IF EXISTS corporate_tree;

CREATE TABLE corporate_tree (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    job_title VARCHAR(50) NOT NULL,
    manager_id INT -- Self-referential key
);

INSERT INTO corporate_tree (emp_id, emp_name, job_title, manager_id) VALUES
(1, 'Aarav Sharma', 'Chief Executive Officer', NULL),
(2, 'Neha Patel', 'VP of Engineering', 1),
(3, 'Priya Nair', 'VP of Product', 1),
(4, 'Rohan Verma', 'Engineering Manager', 2),
(5, 'Vikram Singh', 'Staff Data Engineer', 2),
(6, 'Ananya Sen', 'Senior Frontend Engineer', 4),
(7, 'Amit Kumar', 'Junior Backend Engineer', 4),
(8, 'Kavya Rao', 'Senior Product Manager', 3),
(9, 'Rahul Joshi', 'Associate Product Manager', 8);

-- ==========================================================
-- 2. Generating a Number Sequence
-- ==========================================================

-- Generate numbers from 1 to 5
WITH RECURSIVE number_seq AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1
    FROM number_seq
    WHERE n < 5
)
SELECT * FROM number_seq;

-- ==========================================================
-- 3. Generating a Complete Date Range (Calendar Grid)
-- ==========================================================

-- Generates every calendar day for a given sprint/week
WITH RECURSIVE sprint_calendar AS (
    SELECT CAST('2026-09-01' AS DATE) AS sprint_date
    UNION ALL
    SELECT CAST(sprint_date + INTERVAL '1 day' AS DATE)
    FROM sprint_calendar
    WHERE sprint_date < '2026-09-07'
)
SELECT 
    sprint_date,
    TO_CHAR(sprint_date, 'Day') AS day_name
FROM sprint_calendar;

-- ==========================================================
-- 4. Full Org-Chart Traversal (Top-Down with Levels & Paths)
-- ==========================================================

WITH RECURSIVE org_hierarchy AS (
    -- Anchor Member: Start at the root level (CEO)
    SELECT 
        emp_id,
        emp_name,
        job_title,
        manager_id,
        1 AS org_level,
        CAST(emp_name AS VARCHAR(500)) AS reporting_chain
    FROM corporate_tree
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive Member: Join subordinate records to parents
    SELECT 
        e.emp_id,
        e.emp_name,
        e.job_title,
        e.manager_id,
        h.org_level + 1,
        CAST(CONCAT(h.reporting_chain, ' -> ', e.emp_name) AS VARCHAR(500))
    FROM corporate_tree e
    INNER JOIN org_hierarchy h ON e.manager_id = h.emp_id
)
SELECT 
    org_level,
    emp_name,
    job_title,
    reporting_chain
FROM org_hierarchy
ORDER BY org_level, emp_id;

-- ==========================================================
-- 5. Bottom-Up Lineage: Find Direct Management Chain
-- ==========================================================

-- Trace upward from Junior Engineer Amit Kumar (emp_id = 7) all the way to the CEO
WITH RECURSIVE upward_chain AS (
    -- Anchor: Target individual
    SELECT 
        emp_id,
        emp_name,
        job_title,
        manager_id,
        1 AS chain_step
    FROM corporate_tree
    WHERE emp_id = 7

    UNION ALL

    -- Recursive Step: Trace the manager upward
    SELECT 
        p.emp_id,
        p.emp_name,
        p.job_title,
        p.manager_id,
        u.chain_step + 1
    FROM corporate_tree p
    INNER JOIN upward_chain u ON p.emp_id = u.manager_id
)
SELECT 
    chain_step,
    emp_name,
    job_title
FROM upward_chain
ORDER BY chain_step ASC;
