```sql
-- ==========================================================
-- Day 15: Special Joins (CROSS JOIN & SELF JOIN) Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Data
DROP TABLE IF EXISTS product_skus;
DROP TABLE IF EXISTS colors;
DROP TABLE IF EXISTS sizes;
DROP TABLE IF EXISTS staff_hierarchy;

-- Tables for CROSS JOIN demonstration
CREATE TABLE sizes (
    size_code VARCHAR(10) PRIMARY KEY
);

CREATE TABLE colors (
    color_name VARCHAR(20) PRIMARY KEY
);

INSERT INTO sizes (size_code) VALUES ('Small'), ('Medium'), ('Large');
INSERT INTO colors (color_name) VALUES ('Midnight Black'), ('Ocean Blue'), ('Slate Grey');

-- Table for SELF JOIN demonstration (Self-referencing Foreign Key)
CREATE TABLE staff_hierarchy (
    emp_id INT PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL,
    job_title VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    manager_id INT,
    CONSTRAINT fk_manager 
        FOREIGN KEY (manager_id) 
        REFERENCES staff_hierarchy(emp_id)
);

INSERT INTO staff_hierarchy (emp_id, full_name, job_title, department, salary, manager_id)
VALUES 
    (1, 'Aarav Sharma', 'Director of Engineering', 'Engineering', 180000.00, NULL),
    (2, 'Neha Patel', 'Engineering Manager', 'Engineering', 130000.00, 1),
    (3, 'Rohan Verma', 'Senior Backend Engineer', 'Engineering', 95000.00, 2),
    (4, 'Priya Nair', 'Data Science Manager', 'Data Science', 135000.00, 1),
    (5, 'Vikram Singh', 'Senior ML Engineer', 'Data Science', 110000.00, 4),
    (6, 'Ananya Sen', 'Junior Data Scientist', 'Data Science', 72000.00, 4),
    (7, 'Amit Kumar', 'Backend Engineer', 'Engineering', 82000.00, 2);

-- ==========================================================
-- 2. CROSS JOIN: Generating Complete Variant Matrices
-- ==========================================================

-- Generate all available SKU combinations (3 sizes x 3 colors = 9 variants)
SELECT 
    s.size_code,
    c.color_name,
    CONCAT('TSHIRT-', UPPER(s.size_code), '-', UPPER(REPLACE(c.color_name, ' ', ''))) AS generated_sku
FROM sizes s
CROSS JOIN colors c
ORDER BY s.size_code, c.color_name;

-- ==========================================================
-- 3. SELF JOIN: Organizational Hierarchy
-- ==========================================================

-- Map each employee to their immediate line manager
-- Note: LEFT JOIN is crucial here to retain Aarav Sharma (manager_id IS NULL)
SELECT 
    e.emp_id AS employee_id,
    e.full_name AS employee_name,
    e.job_title AS employee_role,
    COALESCE(m.full_name, 'TOP EXECUTIVE / NO MANAGER') AS reports_to,
    m.job_title AS manager_role
FROM staff_hierarchy e
LEFT JOIN staff_hierarchy m 
    ON e.manager_id = m.emp_id
ORDER BY e.emp_id;

-- ==========================================================
-- 4. SELF JOIN with Aggregation: Direct Reports Count
-- ==========================================================

-- Identify how many direct reports each manager oversees
SELECT 
    m.emp_id AS manager_id,
    m.full_name AS manager_name,
    m.job_title,
    COUNT(e.emp_id) AS direct_reports_count
FROM staff_hierarchy m
INNER JOIN staff_hierarchy e 
    ON m.emp_id = e.manager_id
GROUP BY m.emp_id, m.full_name, m.job_title
ORDER BY direct_reports_count DESC;

-- ==========================================================
-- 5. Non-Equi SELF JOIN: Salary Comparison & Peer Matching
-- ==========================================================

-- Find employees who earn more than their direct manager
SELECT 
    e.full_name AS employee_name,
    e.salary AS employee_salary,
    m.full_name AS manager_name,
    m.salary AS manager_salary,
    (e.salary - m.salary) AS salary_difference
FROM staff_hierarchy e
INNER JOIN staff_hierarchy m 
    ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;

-- Pair peers in the same department without duplicates or self-pairs (e1.emp_id < e2.emp_id)
SELECT 
    e1.department,
    e1.full_name AS colleague_a,
    e2.full_name AS colleague_b
FROM staff_hierarchy e1
INNER JOIN staff_hierarchy e2 
    ON e1.department = e2.department 
   AND e1.emp_id < e2.emp_id
ORDER BY e1.department, colleague_a;
