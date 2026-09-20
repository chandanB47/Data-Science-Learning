```sql
-- ==========================================================
-- Day 16: Set Operators (UNION, UNION ALL, INTERSECT, EXCEPT)
-- ==========================================================

-- 1. Setup Sandbox Schema
DROP TABLE IF EXISTS app_users;
DROP TABLE IF EXISTS store_customers;

CREATE TABLE store_customers (
    customer_id INT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL
);

CREATE TABLE app_users (
    user_id INT PRIMARY KEY,
    display_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL
);

-- Seed In-Store Customers
INSERT INTO store_customers (customer_id, full_name, email, city)
VALUES 
    (1, 'Aarav Sharma', 'aarav@example.com', 'Bengaluru'),
    (2, 'Neha Patel', 'neha@example.com', 'Mumbai'),
    (3, 'Rohan Verma', 'rohan@example.com', 'Delhi'),
    (4, 'Priya Nair', 'priya@example.com', 'Bengaluru');

-- Seed Mobile App Registered Users
INSERT INTO app_users (user_id, display_name, email, city)
VALUES 
    (101, 'Neha Patel', 'neha@example.com', 'Mumbai'),       -- Omnichannel user (Both)
    (102, 'Priya Nair', 'priya@example.com', 'Bengaluru'),    -- Omnichannel user (Both)
    (103, 'Vikram Singh', 'vikram@example.com', 'Hyderabad'), -- App only
    (104, 'Ananya Sen', 'ananya@example.com', 'Bengaluru');   -- App only

-- ==========================================================
-- 2. UNION: Distinct Combined Directory
-- ==========================================================

-- Deduplicates users present in both channels (Returns 6 distinct records)
SELECT full_name AS user_name, email, city, 'Physical Store' AS primary_channel
FROM store_customers
UNION
SELECT display_name AS user_name, email, city, 'Mobile App' AS primary_channel
FROM app_users
ORDER BY user_name;

-- ==========================================================
-- 3. UNION ALL: Full Transactional / Activity Log
-- ==========================================================

-- Keeps duplicate entries; faster execution (Returns all 8 records)
SELECT email, city 
FROM store_customers
UNION ALL
SELECT email, city 
FROM app_users;

-- ==========================================================
-- 4. INTERSECT: Omnichannel Users
-- ==========================================================

-- Identify users active on BOTH physical store and app platforms
-- (MySQL 8.0.31+ / PostgreSQL / SQL Server)
SELECT email 
FROM store_customers
INTERSECT
SELECT email 
FROM app_users;

-- ==========================================================
-- 5. EXCEPT: Channel-Specific Users
-- ==========================================================

-- In-store customers who have NEVER registered on the mobile app (Store - App)
SELECT email 
FROM store_customers
EXCEPT
SELECT email 
FROM app_users;

-- App-only users who have NEVER visited a physical store (App - Store)
SELECT email 
FROM app_users
EXCEPT
SELECT email 
FROM store_customers;
