```sql
-- ==========================================================
-- Day 18: Correlated Subqueries & EXISTS Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Data
DROP TABLE IF EXISTS employee_bonuses;
DROP TABLE IF EXISTS worker_profiles;
DROP TABLE IF EXISTS branch_offices;

CREATE TABLE branch_offices (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL
);

CREATE TABLE worker_profiles (
    worker_id INT PRIMARY KEY,
    worker_name VARCHAR(100) NOT NULL,
    branch_id INT NOT NULL,
    role_name VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    performance_score DECIMAL(3, 1) NOT NULL,
    CONSTRAINT fk_worker_branch FOREIGN KEY (branch_id) REFERENCES branch_offices(branch_id)
);

CREATE TABLE employee_bonuses (
    bonus_id INT PRIMARY KEY,
    worker_id INT, -- Nullable to demonstrate NULL safety
    bonus_amount DECIMAL(10, 2) NOT NULL,
    payout_year INT NOT NULL,
    CONSTRAINT fk_bonus_worker FOREIGN KEY (worker_id) REFERENCES worker_profiles(worker_id)
);

INSERT INTO branch_offices (branch_id, branch_name, city) VALUES
(1, 'Bengaluru Tech Park', 'Bengaluru'),
(2, 'Cyberabad Hub', 'Hyderabad'),
(3, 'BKC Financial Center', 'Mumbai');

INSERT INTO worker_profiles (worker_id, worker_name, branch_id, role_name, salary, performance_score) VALUES
(101, 'Aarav Sharma', 1, 'Data Scientist', 95000.00, 4.8),
(102, 'Neha Patel', 1, 'Data Engineer', 92000.00, 4.5),
(103, 'Rohan Verma', 1, 'Junior Analyst', 58000.00, 3.8),
(104, 'Priya Nair', 2, 'Data Scientist', 110000.00, 4.9),
(105, 'Vikram Singh', 2, 'ML Engineer', 105000.00, 4.2),
(106, 'Ananya Sen', 2, 'Junior Analyst', 54000.00, 3.6),
(107, 'Amit Kumar', 3, 'BI Lead', 98000.00, 4.6),
(108, 'Kavya Rao', 3, 'Reports Analyst', 62000.00, 4.0);

INSERT INTO employee_bonuses (bonus_id, worker_id, bonus_amount, payout_year) VALUES
(1, 101, 15000.00, 2026),
(2, 102, 12000.00, 2026),
(3, 104, 20000.00, 2026),
(4, 107, 14000.00, 2026),
(5, NULL, 5000.00, 2026); -- Simulates orphan/unassigned bonus with NULL

-- ==========================================================
-- 2. Correlated Subquery: Group-Relative Comparison
-- ==========================================================

-- Find workers earning strictly more than their OWN branch's average salary
SELECT 
    w.worker_id,
    w.worker_name,
    w.branch_id,
    w.salary,
    ROUND((
        SELECT AVG(inner_w.salary) 
        FROM worker_profiles inner_w 
        WHERE inner_w.branch_id = w.branch_id
    ), 2) AS branch_avg_salary
FROM worker_profiles w
WHERE w.salary > (
    SELECT AVG(inner_w.salary) 
    FROM worker_profiles inner_w 
    WHERE inner_w.branch_id = w.branch_id
)
ORDER BY w.branch_id, w.salary DESC;

-- Find workers with the highest performance score in their respective branch
SELECT 
    w.worker_name,
    w.branch_id,
    w.role_name,
    w.performance_score
FROM worker_profiles w
WHERE w.performance_score = (
    SELECT MAX(sub.performance_score)
    FROM worker_profiles sub
    WHERE sub.branch_id = w.branch_id
);

-- ==========================================================
-- 3. EXISTS Operator (Short-Circuiting)
-- ==========================================================

-- Find branch offices that employ at least one worker with a performance score >= 4.8
SELECT 
    b.branch_id,
    b.branch_name,
    b.city
FROM branch_offices b
WHERE EXISTS (
    SELECT 1 
    FROM worker_profiles w 
    WHERE w.branch_id = b.branch_id 
      AND w.performance_score >= 4.8
);

-- Find workers who received a bonus in 2026
SELECT 
    w.worker_id,
    w.worker_name,
    w.role_name
FROM worker_profiles w
WHERE EXISTS (
    SELECT 1 
    FROM employee_bonuses b 
    WHERE b.worker_id = w.worker_id 
      AND b.payout_year = 2026
);

-- ==========================================================
-- 4. NOT EXISTS vs NOT IN (NULL Safety Proof)
-- ==========================================================

-- Demonstrating NOT IN vulnerability:
-- Because employee_bonuses has a record with worker_id IS NULL,
-- this query returns 0 rows:
SELECT worker_name 
FROM worker_profiles 
WHERE worker_id NOT IN (SELECT worker_id FROM employee_bonuses);

-- Safe and standard implementation using NOT EXISTS:
-- Correctly returns all workers who did not receive a bonus
SELECT 
    w.worker_id,
    w.worker_name,
    w.role_name
FROM worker_profiles w
WHERE NOT EXISTS (
    SELECT 1 
    FROM employee_bonuses b 
    WHERE b.worker_id = w.worker_id
);
