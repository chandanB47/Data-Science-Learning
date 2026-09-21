```sql
-- ==========================================================
-- Day 17: Subqueries (Scalar, Multi-Row, and Nested) Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Records
DROP TABLE IF EXISTS project_allocations;
DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS divisions;

CREATE TABLE divisions (
    division_id INT PRIMARY KEY,
    division_name VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL
);

CREATE TABLE staff (
    staff_id INT PRIMARY KEY,
    staff_name VARCHAR(50) NOT NULL,
    division_id INT,
    job_title VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    CONSTRAINT fk_staff_div FOREIGN KEY (division_id) REFERENCES divisions(division_id)
);

CREATE TABLE project_allocations (
    allocation_id INT PRIMARY KEY,
    staff_id INT NOT NULL,
    project_code VARCHAR(20) NOT NULL,
    hours_logged INT NOT NULL,
    CONSTRAINT fk_alloc_staff FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);

INSERT INTO divisions (division_id, division_name, city) VALUES
(1, 'Analytics & AI', 'Bengaluru'),
(2, 'Platform Engineering', 'Hyderabad'),
(3, 'Corporate Operations', 'Mumbai');

INSERT INTO staff (staff_id, staff_name, division_id, job_title, salary) VALUES
(101, 'Aarav Sharma', 1, 'Data Scientist', 95000.00),
(102, 'Neha Patel', 1, 'AI Researcher', 120000.00),
(103, 'Rohan Verma', 2, 'DevOps Engineer', 82000.00),
(104, 'Priya Nair', 1, 'BI Analyst', 70000.00),
(105, 'Vikram Singh', 2, 'Cloud Architect', 135000.00),
(106, 'Ananya Sen', 3, 'HR Specialist', 55000.00),
(107, 'Amit Kumar', 3, 'Operations Lead', 65000.00);

INSERT INTO project_allocations (allocation_id, staff_id, project_code, hours_logged) VALUES
(1, 101, 'PRJ-ALPHA', 120),
(2, 102, 'PRJ-ALPHA', 140),
(3, 103, 'PRJ-BETA', 90),
(4, 105, 'PRJ-BETA', 160);
-- Staff 104, 106, 107 have no project allocations

-- ==========================================================
-- 2. Scalar Subqueries
-- ==========================================================

-- A. In WHERE Clause: Staff earning strictly above the company average salary
SELECT 
    staff_id,
    staff_name,
    job_title,
    salary
FROM staff
WHERE salary > (SELECT AVG(salary) FROM staff)
ORDER BY salary DESC;

-- B. In SELECT Clause: Compare individual salary to company average and calculate variance
SELECT 
    staff_name,
    salary,
    (SELECT ROUND(AVG(salary), 2) FROM staff) AS overall_avg_salary,
    ROUND(salary - (SELECT AVG(salary) FROM staff), 2) AS salary_variance
FROM staff
ORDER BY salary DESC;

-- ==========================================================
-- 3. Multi-Row Subqueries (IN, NOT IN)
-- ==========================================================

-- Find staff members who are actively assigned to AT LEAST ONE project
SELECT staff_id, staff_name, job_title
FROM staff
WHERE staff_id IN (
    SELECT DISTINCT staff_id 
    FROM project_allocations
);

-- Find staff members who have ZERO project allocations (Safeguarded against NULLs)
SELECT staff_id, staff_name, job_title
FROM staff
WHERE staff_id NOT IN (
    SELECT staff_id 
    FROM project_allocations 
    WHERE staff_id IS NOT NULL
);

-- ==========================================================
-- 4. ANY and ALL Operators
-- ==========================================================

-- ANY: Staff in other divisions earning more than AT LEAST ONE person in Analytics (division 1)
SELECT staff_name, division_id, salary
FROM staff
WHERE division_id != 1
  AND salary > ANY (SELECT salary FROM staff WHERE division_id = 1);

-- ALL: Staff in other divisions earning more than EVERYONE in Analytics (division 1)
SELECT staff_name, division_id, salary
FROM staff
WHERE division_id != 1
  AND salary > ALL (SELECT salary FROM staff WHERE division_id = 1);

-- ==========================================================
-- 5. Derived Tables (Subqueries in FROM)
-- ==========================================================

-- Compute division payroll statistics, then find the average division payroll
SELECT 
    ROUND(AVG(total_payroll), 2) AS avg_division_spend,
    MAX(total_payroll) AS max_division_spend
FROM (
    SELECT 
        division_id,
        COUNT(staff_id) AS headcount,
        SUM(salary) AS total_payroll
    FROM staff
    GROUP BY division_id
) AS division_metrics;
