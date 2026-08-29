```sql
-- ==========================================================
-- Day 06: Filtering & Pattern Matching Hands-On Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Data
DROP TABLE IF EXISTS customer_profiles;

CREATE TABLE customer_profiles (
    customer_id INT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    city VARCHAR(50),
    annual_spend DECIMAL(10, 2) NOT NULL,
    tier VARCHAR(20) NOT NULL,
    referred_by INT -- Can be NULL
);

INSERT INTO customer_profiles (customer_id, full_name, email, city, annual_spend, tier, referred_by)
VALUES 
    (1, 'Aarav Sharma', 'aarav.sharma@gmail.com', 'Bengaluru', 85000.00, 'Platinum', NULL),
    (2, 'Neha Patel', 'neha.p@techcorp.in', 'Mumbai', 42000.00, 'Gold', 1),
    (3, 'Rohan Verma', 'rohan_v@outlook.com', 'Delhi', 15000.00, 'Silver', 1),
    (4, 'Ananya Sen', 'ananya.sen@gmail.com', 'Bengaluru', 62000.00, 'Gold', NULL),
    (5, 'Vikram Singh', 'v.singh@yahoo.com', 'Hyderabad', 9200.00, 'Bronze', 2),
    (6, 'Pooja Iyer', 'pooja.iyer@techcorp.in', 'Pune', 54000.00, 'Gold', NULL),
    (7, 'Amit Kumar', 'amit.k99@gmail.com', 'Bengaluru', 110000.00, 'Platinum', 1),
    (8, 'Divya Nair', 'divya_nair@outlook.com', 'Chennai', 31000.00, 'Silver', 4);

-- ==========================================================
-- 2. Basic Filtering & Logical Operators
-- ==========================================================

-- Filter by specific tier and spend threshold
SELECT customer_id, full_name, annual_spend, tier
FROM customer_profiles
WHERE tier = 'Gold' AND annual_spend >= 50000.00;

-- Demonstrate Boolean Precedence with Parentheses
-- Find Platinum or Gold users located specifically in Bengaluru
SELECT customer_id, full_name, city, tier, annual_spend
FROM customer_profiles
WHERE (tier = 'Platinum' OR tier = 'Gold') AND city = 'Bengaluru';

-- ==========================================================
-- 3. Range & Set Filtering (BETWEEN, IN, NOT IN)
-- ==========================================================

-- Find customers within a spend bracket (inclusive)
SELECT customer_id, full_name, annual_spend
FROM customer_profiles
WHERE annual_spend BETWEEN 30000.00 AND 70000.00;

-- Find customers located in tier-1 tech hubs
SELECT customer_id, full_name, city
FROM customer_profiles
WHERE city IN ('Bengaluru', 'Hyderabad', 'Pune');

-- Exclude entry tiers
SELECT customer_id, full_name, tier
FROM customer_profiles
WHERE tier NOT IN ('Bronze', 'Silver');

-- ==========================================================
-- 4. Pattern Matching with LIKE & Wildcards
-- ==========================================================

-- Find all customers using corporate email '@techcorp.in'
SELECT customer_id, full_name, email
FROM customer_profiles
WHERE email LIKE '%@techcorp.in';

-- Find customers whose first name starts with 'A'
SELECT customer_id, full_name
FROM customer_profiles
WHERE full_name LIKE 'A%';

-- Find customers with underscore in email address
SELECT customer_id, full_name, email
FROM customer_profiles
WHERE email LIKE '%\_%' ESCAPE '\';

-- ==========================================================
-- 5. NULL Value Evaluations
-- ==========================================================

-- Find organic customers (who were NOT referred by another user)
SELECT customer_id, full_name, city, referred_by
FROM customer_profiles
WHERE referred_by IS NULL;

-- Find customers acquired via referral program
SELECT customer_id, full_name, referred_by
FROM customer_profiles
WHERE referred_by IS NOT NULL;
