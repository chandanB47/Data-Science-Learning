```sql
-- ==========================================================
-- Day 05: DQL & Basic Querying Hands-On Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Data
DROP TABLE IF EXISTS sales_reps;
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    unit_cost DECIMAL(10, 2) NOT NULL,
    retail_price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL
);

CREATE TABLE sales_reps (
    rep_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    region VARCHAR(50),
    base_salary DECIMAL(10, 2) NOT NULL,
    commission_pct DECIMAL(4, 2) -- Can be NULL
);

INSERT INTO products (product_id, product_name, category, unit_cost, retail_price, stock_quantity)
VALUES 
    (101, '4K Ultra Monitor', 'Electronics', 18000.00, 24999.00, 35),
    (102, 'Ergonomic Chair', 'Furniture', 7500.00, 12499.00, 20),
    (103, 'Mechanical Keyboard', 'Electronics', 2200.00, 4499.00, 100),
    (104, 'Desk Pad', 'Accessories', 350.00, 899.00, 250),
    (105, 'USB-C Dock', 'Electronics', 3200.00, 5999.00, 45),
    (106, 'Standing Desk', 'Furniture', 14000.00, 21999.00, 15);

INSERT INTO sales_reps (rep_id, first_name, last_name, region, base_salary, commission_pct)
VALUES 
    (1, 'Aarav', 'Sharma', 'South', 60000.00, 0.15),
    (2, 'Neha', 'Patel', 'West', 65000.00, 0.12),
    (3, 'Rohan', 'Verma', 'North', 55000.00, NULL),
    (4, 'Priya', 'Nair', 'South', 62000.00, 0.18),
    (5, 'Vikram', 'Singh', 'West', 58000.00, NULL);

-- ==========================================================
-- 2. Basic Projection & Aliasing
-- ==========================================================

-- Select specific columns with clean aliases
SELECT 
    first_name AS rep_first_name,
    last_name AS rep_last_name,
    region AS sales_territory
FROM sales_reps;

-- Concatenate full name and project clean table columns
SELECT 
    rep_id,
    first_name || ' ' || last_name AS full_name,
    base_salary
FROM sales_reps;

-- ==========================================================
-- 3. DISTINCT Usage
-- ==========================================================

-- Get unique product categories
SELECT DISTINCT category 
FROM products;

-- Get unique sales regions
SELECT DISTINCT region 
FROM sales_reps;

-- Get unique combinations of region and base salary
SELECT DISTINCT region, base_salary 
FROM sales_reps;

-- ==========================================================
-- 4. Computed Fields & Calculations
-- ==========================================================

-- Calculate profit margin per unit and total inventory value
SELECT 
    product_name,
    category,
    retail_price,
    unit_cost,
    (retail_price - unit_cost) AS profit_per_unit,
    ((retail_price - unit_cost) / retail_price) * 100 AS profit_margin_pct,
    (retail_price * stock_quantity) AS total_inventory_valuation
FROM products;

-- ==========================================================
-- 5. Handling NULL Values with COALESCE
-- ==========================================================

-- Calculate potential bonus safely when commission_pct contains NULL
SELECT 
    first_name || ' ' || last_name AS sales_rep,
    base_salary,
    COALESCE(commission_pct, 0.00) AS commission_rate,
    base_salary * COALESCE(commission_pct, 0.00) AS estimated_bonus,
    base_salary + (base_salary * COALESCE(commission_pct, 0.00)) AS total_projected_payout
FROM sales_reps;
