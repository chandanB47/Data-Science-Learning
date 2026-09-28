-- ==========================================================
-- Day 24: Views & Materialized Views (MySQL 8.0+ Compatible)
-- ==========================================================

USE retail_analytics;

-- 1. Setup Base Schema & Data
DROP VIEW IF EXISTS v_executive_payroll;
DROP VIEW IF EXISTS v_active_south_customers;
DROP VIEW IF EXISTS v_product_sales_summary;
DROP TABLE IF EXISTS employee_records;

CREATE TABLE employee_records (
    emp_id INT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    base_salary DECIMAL(10, 2) NOT NULL,
    bank_account_no VARCHAR(30) NOT NULL,
    city VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

INSERT INTO employee_records (emp_id, full_name, department, base_salary, bank_account_no, city, is_active) VALUES
(1, 'Aarav Sharma', 'Engineering', 95000.00, 'SBIN00012345678', 'Bengaluru', TRUE),
(2, 'Neha Patel',   'Engineering', 92000.00, 'HDFC00098765432', 'Bengaluru', TRUE),
(3, 'Rohan Verma',  'Analytics',   78000.00, 'ICIC00045678901', 'Hyderabad', TRUE),
(4, 'Priya Nair',   'Analytics',   88000.00, 'KKBK00011223344', 'Bengaluru', TRUE),
(5, 'Vikram Singh', 'Marketing',   65000.00, 'AXIS00099887766', 'Mumbai', FALSE);

-- ==========================================================
-- 2. Security Masking View (Hide PII & Restrict Columns)
-- ==========================================================

-- Standard view concealing sensitive bank details and masked compensation
CREATE OR REPLACE VIEW v_public_directory AS
SELECT 
    emp_id,
    full_name,
    department,
    city,
    CONCAT('******', RIGHT(bank_account_no, 4)) AS masked_bank_ref
FROM employee_records
WHERE is_active = TRUE;

-- Query the abstract layer
SELECT * FROM v_public_directory;

-- ==========================================================
-- 3. Complex Reporting View (Pre-packaged Business Metrics)
-- ==========================================================

CREATE OR REPLACE VIEW v_dept_compensation_summary AS
SELECT 
    department,
    COUNT(emp_id) AS total_headcount,
    ROUND(AVG(base_salary), 2) AS avg_department_salary,
    SUM(base_salary) AS total_payroll
FROM employee_records
WHERE is_active = TRUE
GROUP BY department;

SELECT * FROM v_dept_compensation_summary;

-- ==========================================================
-- 4. Updatable View with WITH CHECK OPTION
-- ==========================================================

CREATE OR REPLACE VIEW v_bengaluru_staff AS
SELECT 
    emp_id,
    full_name,
    department,
    base_salary,
    city
FROM employee_records
WHERE city = 'Bengaluru'
WITH CHECK OPTION;

-- Successful update within view scope
UPDATE v_bengaluru_staff
SET base_salary = base_salary + 2000.00
WHERE emp_id = 1;

-- Verify the update propagated to the underlying table
SELECT emp_id, full_name, base_salary, city 
FROM employee_records 
WHERE emp_id = 1;

-- ==========================================================
-- 5. Emulating Materialized Views in MySQL
-- ==========================================================

-- In MySQL, heavy analytical views are often materialized into a summary table 
-- and refreshed periodically via scheduled procedures/events
DROP TABLE IF EXISTS mv_dept_summary_cache;

-- Initial materialization pass
CREATE TABLE mv_dept_summary_cache AS
SELECT 
    department,
    COUNT(emp_id) AS headcount,
    SUM(base_salary) AS total_spend,
    CURRENT_TIMESTAMP AS last_refreshed_at
FROM employee_records
WHERE is_active = TRUE
GROUP BY department;

SELECT * FROM mv_dept_summary_cache;

-- Manual refresh procedure emulation
TRUNCATE TABLE mv_dept_summary_cache;

INSERT INTO mv_dept_summary_cache
SELECT 
    department,
    COUNT(emp_id) AS headcount,
    SUM(base_salary) AS total_spend,
    CURRENT_TIMESTAMP AS last_refreshed_at
FROM employee_records
WHERE is_active = TRUE
GROUP BY department;

SELECT * FROM mv_dept_summary_cache;
