```sql
-- ==========================================================
-- Day 07: Sorting & Pagination Hands-On Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Records
DROP TABLE IF EXISTS store_inventory;

CREATE TABLE store_inventory (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    rating DECIMAL(2, 1), -- Nullable column
    sales_count INT NOT NULL
);

INSERT INTO store_inventory (item_id, item_name, category, price, rating, sales_count)
VALUES 
    (1, 'Mechanical Keyboard Pro', 'Electronics', 4999.00, 4.8, 1200),
    (2, 'Ergonomic Desk Chair', 'Furniture', 12500.00, 4.6, 450),
    (3, 'Wireless Gaming Mouse', 'Electronics', 2499.00, 4.5, 3100),
    (4, 'USB-C Multi-port Adapter', 'Electronics', 1899.00, NULL, 800),
    (5, '4K IPS Monitor 27"', 'Electronics', 22999.00, 4.9, 620),
    (6, 'Adjustable Footrest', 'Furniture', 1499.00, 4.1, 350),
    (7, 'Ultra-wide Mousepad', 'Accessories', 799.00, 4.7, 5000),
    (8, 'LED Desk Lamp', 'Accessories', 1299.00, NULL, 150),
    (9, 'Dual Monitor Arm Stand', 'Furniture', 3499.00, 4.4, 890),
    (10, 'Noise Cancelling Headphones', 'Electronics', 14999.00, 4.7, 2100),
    (11, 'Bluetooth Numeric Keypad', 'Electronics', 1199.00, 3.9, 95),
    (12, 'Cable Management Sleeve', 'Accessories', 399.00, 4.3, 4200);

-- ==========================================================
-- 2. Basic & Multi-Column Sorting
-- ==========================================================

-- Top items by price (highest to lowest)
SELECT item_id, item_name, category, price
FROM store_inventory
ORDER BY price DESC;

-- Multi-column sorting: Grouped by category (A-Z), highest sales count within category
SELECT item_id, item_name, category, sales_count
FROM store_inventory
ORDER BY category ASC, sales_count DESC;

-- ==========================================================
-- 3. Explicit NULL Handling in Sorting
-- ==========================================================

-- Highest rated items, placing unrated items (NULL) at the very end
SELECT item_id, item_name, rating
FROM store_inventory
ORDER BY rating DESC NULLS LAST;

-- Lowest rated items, keeping NULL ratings at the top
SELECT item_id, item_name, rating
FROM store_inventory
ORDER BY rating ASC NULLS FIRST;

-- ==========================================================
-- 4. Pagination using LIMIT & OFFSET
-- ==========================================================

-- Page 1: Items 1 to 4 sorted by popularity (sales_count)
SELECT item_id, item_name, sales_count, price
FROM store_inventory
ORDER BY sales_count DESC
LIMIT 4 OFFSET 0;

-- Page 2: Items 5 to 8
SELECT item_id, item_name, sales_count, price
FROM store_inventory
ORDER BY sales_count DESC
LIMIT 4 OFFSET 4;

-- Page 3: Items 9 to 12
SELECT item_id, item_name, sales_count, price
FROM store_inventory
ORDER BY sales_count DESC
LIMIT 4 OFFSET 8;

-- ==========================================================
-- 5. ANSI SQL Standard Pagination (OFFSET ... FETCH)
-- ==========================================================

-- Fetch top 3 most expensive electronics using standard ANSI syntax
SELECT item_id, item_name, category, price
FROM store_inventory
WHERE category = 'Electronics'
ORDER BY price DESC
OFFSET 0 ROWS
FETCH NEXT 3 ROWS ONLY;
```
