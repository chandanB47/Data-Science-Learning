-- ==========================================================
-- Day 27: Interview Patterns I Practice (MySQL 8.0+)
-- ==========================================================

USE retail_analytics;

-- 1. Setup Sample Interview Schemas
DROP TABLE IF EXISTS consecutive_events;
DROP TABLE IF EXISTS candidate_records;
DROP TABLE IF EXISTS compensation_records;

CREATE TABLE compensation_records (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    department_id INT NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);

CREATE TABLE candidate_records (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    applied_role VARCHAR(50) NOT NULL
);

CREATE TABLE consecutive_events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    event_val INT NOT NULL
);

-- Seed Data
INSERT INTO compensation_records (emp_id, emp_name, department_id, salary) VALUES
(1, 'Aarav Sharma', 101, 95000.00),
(2, 'Neha Patel',   101, 95000.00), -- Tied top salary in Dept 101
(3, 'Rohan Verma',  101, 82000.00),
(4, 'Priya Nair',   101, 74000.00),
(5, 'Vikram Singh', 102, 110000.00),
(6, 'Ananya Sen',   102, 98000.00),
(7, 'Amit Kumar',   102, 98000.00), -- Tied 2nd salary in Dept 102
(8, 'Kavya Rao',    102, 60000.00);

INSERT INTO candidate_records (full_name, email, applied_role) VALUES
('Suresh Kumar', 'suresh@gmail.com', 'Data Analyst'),
('Suresh Kumar', 'suresh@gmail.com', 'Data Analyst'), -- Exact duplicate
('Aditi Sen',    'aditi@gmail.com',  'ML Engineer'),
('Rahul Verma',  'rahul@outlook.com','Data Analyst'),
('Aditi Sen',    'aditi@gmail.com',  'ML Engineer'), -- Exact duplicate
('Vikram Joshi', 'vikram@yahoo.com', 'BI Developer');

INSERT INTO consecutive_events (event_val) VALUES
(1), (1), (1), (2), (1), (2), (2), (2), (3);

-- ==========================================================
-- 2. Global Nth Highest Salary (Finding 2nd Highest)
-- ==========================================================

-- Method A: DENSE_RANK with NULL guarantee via MAX()
WITH ranked_comp AS (
    SELECT 
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM compensation_records
)
SELECT MAX(salary) AS SecondHighestSalary
FROM ranked_comp
WHERE rnk = 2;

-- Method B: Subquery with LIMIT / OFFSET and IFNULL
SELECT (
    SELECT DISTINCT salary 
    FROM compensation_records 
    ORDER BY salary DESC 
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;

-- ==========================================================
-- 3. Top 2 Earners per Department (Department-Wise)
-- ==========================================================

WITH dept_ranked AS (
    SELECT 
        department_id,
        emp_name,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY department_id 
            ORDER BY salary DESC
        ) AS rank_in_dept
    FROM compensation_records
)
SELECT 
    department_id,
    rank_in_dept,
    emp_name,
    salary
FROM dept_ranked
WHERE rank_in_dept <= 2
ORDER BY department_id, rank_in_dept;

-- ==========================================================
-- 4. Duplicate Detection & Deterministic Deletion
-- ==========================================================

-- View duplicates and their frequency
SELECT email, applied_role, COUNT(*) AS duplicate_count
FROM candidate_records
GROUP BY email, applied_role
HAVING COUNT(*) > 1;

-- Delete duplicate candidate rows, preserving the record with the lowest record_id
DELETE c1
FROM candidate_records c1
INNER JOIN candidate_records c2 
    ON c1.email = c2.email 
   AND c1.applied_role = c2.applied_role 
   AND c1.record_id > c2.record_id;

-- Confirm deduplication
SELECT * FROM candidate_records;

-- ==========================================================
-- 5. Consecutive Value Detection (At Least 3 in a Row)
-- ==========================================================

WITH sequence_window AS (
    SELECT 
        event_val,
        LAG(event_val, 1) OVER (ORDER BY id) AS prev_1,
        LAG(event_val, 2) OVER (ORDER BY id) AS prev_2
    FROM consecutive_events
)
SELECT DISTINCT event_val AS ConsecutiveNums
FROM sequence_window
WHERE event_val = prev_1 AND event_val = prev_2;
