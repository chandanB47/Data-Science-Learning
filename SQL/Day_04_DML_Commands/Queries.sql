```sql
-- ==========================================================
-- Day 04: DML (Data Manipulation Language) Hands-On Practice
-- ==========================================================

-- 1. Setup Sandbox Environment
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS customer_orders;
DROP TABLE IF EXISTS accounts;

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    holder_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    balance DECIMAL(12, 2) DEFAULT 0.00,
    status VARCHAR(20) DEFAULT 'ACTIVE'
);

CREATE TABLE inventory (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    stock_qty INT NOT NULL CHECK (stock_qty >= 0),
    unit_price DECIMAL(10, 2) NOT NULL
);

-- ==========================================================
-- 2. INSERT Operations
-- ==========================================================

-- Single row insert specifying explicit columns
INSERT INTO accounts (account_id, holder_name, email, balance, status)
VALUES (1, 'Chandan Kumar', 'chandan@example.com', 25000.00, 'ACTIVE');

-- Multi-row insert
INSERT INTO accounts (account_id, holder_name, email, balance, status)
VALUES 
    (2, 'Priya Nair', 'priya@example.com', 42000.50, 'ACTIVE'),
    (3, 'Vikram Singh', 'vikram@example.com', 1500.00, 'DORMANT'),
    (4, 'Ananya Sen', 'ananya@example.com', 8500.00, 'SUSPENDED');

-- Bulk load inventory items
INSERT INTO inventory (product_id, product_name, stock_qty, unit_price)
VALUES 
    (101, 'Mechanical Keyboard', 45, 3499.00),
    (102, 'Wireless Mouse', 80, 1299.00),
    (103, 'USB-C Hub', 15, 2199.00),
    (104, 'Monitor Stand', 0, 899.00);

-- View initial state
SELECT * FROM accounts;
SELECT * FROM inventory;

-- ==========================================================
-- 3. UPDATE Operations
-- ==========================================================

-- Single row value update
UPDATE accounts
SET balance = balance + 5000.00
WHERE account_id = 1;

-- Multi-column update based on conditional filter
UPDATE accounts
SET 
    status = 'ACTIVE',
    balance = balance + 500.00
WHERE status = 'DORMANT';

-- Update with mathematical calculation on multiple records
UPDATE inventory
SET unit_price = unit_price * 1.05
WHERE stock_qty > 20;

-- Verify updates
SELECT * FROM accounts;
SELECT * FROM inventory;

-- ==========================================================
-- 4. DELETE Operations
-- ==========================================================

-- Target delete of a specific record
DELETE FROM accounts
WHERE account_id = 4;

-- Delete records based on column state
DELETE FROM inventory
WHERE stock_qty = 0;

-- Verify remaining records
SELECT * FROM accounts;
SELECT * FROM inventory;

-- ==========================================================
-- 5. Safe Transaction Practice Pattern
-- ==========================================================

-- Demonstrate safe atomic testing (PostgreSQL / standard SQL)
BEGIN;

UPDATE accounts
SET balance = balance - 1000.00
WHERE account_id = 1;

-- Verify changes within the active transaction scope
SELECT * FROM accounts WHERE account_id = 1;

-- Discard the test change safely
ROLLBACK;

-- Verify the balance reverted to original state
SELECT * FROM accounts WHERE account_id = 1;
