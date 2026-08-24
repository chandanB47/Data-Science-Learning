-- ==========================================================
-- Day 01: DBMS vs RDBMS & SQL Fundamentals Hands-On Practice
-- ==========================================================

-- 1. Create a clean sandbox database / schema (if needed)
CREATE DATABASE day01_db;

-- 2. Create sample parent and child tables demonstrating relational integrity
-- Parent Table: Departments
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL,
    location VARCHAR(50) DEFAULT 'Remote'
);

-- Child Table: Employees (Relies on departments via Foreign Key)
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    department_id INT,
    hire_date DATE DEFAULT CURRENT_DATE,
    CONSTRAINT fk_department
        FOREIGN KEY (department_id) 
        REFERENCES departments(department_id)
        ON DELETE SET NULL
);

-- 3. Insert sample data (DML)
INSERT INTO departments (department_id, department_name, location)
VALUES 
    (101, 'Engineering', 'Bengaluru'),
    (102, 'Data Science', 'Hyderabad'),
    (103, 'Product', 'Remote');

INSERT INTO employees (employee_id, first_name, last_name, email, salary, department_id, hire_date)
VALUES 
    (1, 'Aarav', 'Sharma', 'aarav.sharma@example.com', 85000.00, 101, '2024-01-15'),
    (2, 'Neha', 'Patel', 'neha.patel@example.com', 92000.00, 102, '2024-03-01'),
    (3, 'Rohan', 'Verma', 'rohan.verma@example.com', 78000.00, 101, '2024-06-10');

-- 4. Query data to verify relationships (DQL)
SELECT 
    e.employee_id,
    e.first_name || ' ' || e.last_name AS full_name,
    e.email,
    e.salary,
    d.department_name,
    d.location
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;

