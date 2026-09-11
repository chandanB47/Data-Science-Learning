```sql
-- ==========================================================
-- Day 11: Grouping Data (GROUP BY) Hands-On Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Records
DROP TABLE IF EXISTS company_employees;

CREATE TABLE company_employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL,
    job_title VARCHAR(50) NOT NULL,
    office_location VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    employment_status VARCHAR(20) NOT NULL
);

INSERT INTO company_employees (emp_id, emp_name, department, job_title, office_location, salary, employment_status)
VALUES 
    (1, 'Aarav Sharma', 'Engineering', 'Backend Engineer', 'Bengaluru', 85000.00, 'Full-Time'),
    (2, 'Neha Patel', 'Engineering', 'Data Engineer', 'Bengaluru', 92000.00, 'Full-Time'),
    (3, 'Rohan Verma', 'Engineering', 'Backend Engineer', 'Pune', 78000.00, 'Full-Time'),
    (4, 'Priya Nair', 'Data Science', 'Data Scientist', 'Bengaluru', 105000.00, 'Full-Time'),
    (5, 'Vikram Singh', 'Data Science', 'ML Engineer', 'Hyderabad', 115000.00, 'Full-Time'),
    (6, 'Ananya Sen', 'Marketing', 'Content Strategist', 'Mumbai', 48000.00, 'Contract'),
    (7, 'Amit Kumar', 'Marketing', 'Growth Manager', 'Mumbai', 72000.00, 'Full-Time'),
    (8, 'Kavya Rao', 'Engineering', 'Frontend Engineer', 'Bengaluru', 80000.00, 'Full-Time'),
    (9, 'Rahul Joshi', 'Data Science', 'Data Scientist', 'Hyderabad', 98000.00, 'Contract'),
    (10, 'Sneha Reddy', 'Marketing', 'SEO Specialist', 'Bengaluru', 52000.00, 'Full-Time');

-- ==========================================================
-- 2. Single-Column Grouping
-- ==========================================================

-- Headcount, total payroll, and average salary per department
SELECT 
    department,
    COUNT(*) AS total_employees,
    SUM(salary) AS total_payroll,
    ROUND(AVG(salary), 2) AS average_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM company_employees
GROUP BY department
ORDER BY total_payroll DESC;

-- Distribution of employees by office location
SELECT 
    office_location,
    COUNT(*) AS location_headcount,
    ROUND(AVG(salary), 2) AS location_avg_salary
FROM company_employees
GROUP BY office_location
ORDER BY location_headcount DESC;

-- ==========================================================
-- 3. Multi-Column Grouping (Hierarchy)
-- ==========================================================

-- Breakdown by department and office location
SELECT 
    department,
    office_location,
    COUNT(*) AS employees_count,
    ROUND(AVG(salary), 2) AS avg_comp
FROM company_employees
GROUP BY department, office_location
ORDER BY department, office_location;

-- Group by department and specific job title
SELECT 
    department,
    job_title,
    COUNT(*) AS role_headcount,
    MAX(salary) AS highest_paid_in_role
FROM company_employees
GROUP BY department, job_title
ORDER BY department, role_headcount DESC;

-- ==========================================================
-- 4. Combining WHERE Filtering with GROUP BY
-- ==========================================================

-- Analyze payroll metrics ONLY for Full-Time staff (skipping contractors early)
SELECT 
    department,
    COUNT(*) AS full_time_headcount,
    ROUND(AVG(salary), 2) AS full_time_avg_salary
FROM company_employees
WHERE employment_status = 'Full-Time'
GROUP BY department
ORDER BY full_time_avg_salary DESC;

-- Filter for high-compensation roles before grouping
SELECT 
    office_location,
    COUNT(*) AS high_earners_count
FROM company_employees
WHERE salary >= 80000.00
GROUP BY office_location
ORDER BY high_earners_count DESC;

-- ==========================================================
-- 5. Grouping by Expressions
-- ==========================================================

-- Categorize salary brackets and group employees into bands
SELECT 
    CASE 
        WHEN salary < 60000.00 THEN 'Entry Band (<60k)'
        WHEN salary BETWEEN 60000.00 AND 90000.00 THEN 'Mid Band (60k-90k)'
        ELSE 'Senior Band (>90k)'
    END AS compensation_tier,
    COUNT(*) AS staff_count,
    ROUND(AVG(salary), 2) AS band_avg_salary
FROM company_employees
GROUP BY 
    CASE 
        WHEN salary < 60000.00 THEN 'Entry Band (<60k)'
        WHEN salary BETWEEN 60000.00 AND 90000.00 THEN 'Mid Band (60k-90k)'
        ELSE 'Senior Band (>90k)'
    END
ORDER BY staff_count DESC;
