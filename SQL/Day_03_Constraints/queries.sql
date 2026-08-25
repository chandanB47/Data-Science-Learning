```sql
-- ==========================================================
-- Day 03: Constraints & Data Integrity Hands-On Practice
-- ==========================================================

-- 1. Setup clean schema
DROP TABLE IF EXISTS employee_audit;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

-- 2. Create Parent Table with PRIMARY KEY, NOT NULL, and UNIQUE
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_code VARCHAR(10) UNIQUE NOT NULL,
    department_name VARCHAR(50) NOT NULL
);

-- 3. Create Child Table with CHECK, DEFAULT, NOT NULL, and FOREIGN KEY (CASCADE)
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT CHECK (age >= 18 AND age <= 65),
    salary DECIMAL(10, 2) CHECK (salary > 0),
    department_id INT,
    status VARCHAR(20) DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'ON_LEAVE', 'TERMINATED')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_dept_emp
        FOREIGN KEY (department_id) 
        REFERENCES departments(department_id)
        ON DELETE CASCADE
);

-- 4. Valid Inserts
INSERT INTO departments (department_id, department_code, department_name)
VALUES 
    (1, 'ENG', 'Engineering'),
    (2, 'DS', 'Data Science');

INSERT INTO employees (emp_id, full_name, email, age, salary, department_id)
VALUES 
    (101, 'Aarav Sharma', 'aarav.sharma@example.com', 26, 85000.00, 1),
    (102, 'Neha Patel', 'neha.patel@example.com', 29, 95000.00, 2);

-- Verify successfully inserted records
SELECT * FROM departments;
SELECT * FROM employees;

-- ==========================================================
-- 5. Testing Constraint Violations (Uncomment to test errors)
-- ==========================================================

-- Error 1: UNIQUE Violation (Duplicate email)
-- INSERT INTO employees (emp_id, full_name, email, age, salary, department_id)
-- VALUES (103, 'Aarav Duplicate', 'aarav.sharma@example.com', 30, 60000.00, 1);

-- Error 2: CHECK Constraint Violation (Age < 18)
-- INSERT INTO employees (emp_id, full_name, email, age, salary, department_id)
-- VALUES (104, 'Minor User', 'minor@example.com', 16, 40000.00, 1);

-- Error 3: FOREIGN KEY Violation (Department 99 does not exist)
-- INSERT INTO employees (emp_id, full_name, email, age, salary, department_id)
-- VALUES (105, 'Orphan User', 'orphan@example.com', 32, 70000.00, 99);

-- ==========================================================
-- 6. Testing ON DELETE CASCADE
-- ==========================================================

-- Deleting Department 1 will automatically remove employee 101
DELETE FROM departments WHERE department_id = 1;

-- Verify that employee 101 was removed automatically
SELECT * FROM employees;

-- ==========================================================
-- 7. Managing Constraints on Existing Tables
-- ==========================================================

-- Add a new check constraint
ALTER TABLE employees 
ADD CONSTRAINT chk_emp_salary_min CHECK (salary >= 20000);

-- Drop the check constraint
ALTER TABLE employees 
DROP CONSTRAINT chk_emp_salary_min;
