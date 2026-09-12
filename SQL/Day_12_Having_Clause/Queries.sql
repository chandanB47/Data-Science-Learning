```sql
-- ==========================================================
-- Day 12: Filtering Aggregations (HAVING vs WHERE) Hands-On Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Records
DROP TABLE IF EXISTS customer_orders;

CREATE TABLE customer_orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    customer_name VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    order_amount DECIMAL(10, 2) NOT NULL,
    order_status VARCHAR(20) NOT NULL
);

INSERT INTO customer_orders (order_id, customer_id, customer_name, category, order_amount, order_status)
VALUES 
    (101, 1, 'Aarav Sharma', 'Electronics', 45000.00, 'COMPLETED'),
    (102, 2, 'Neha Patel', 'Furniture', 12000.00, 'COMPLETED'),
    (103, 1, 'Aarav Sharma', 'Electronics', 25000.00, 'COMPLETED'),
    (104, 3, 'Rohan Verma', 'Electronics', 3500.00, 'CANCELLED'),
    (105, 2, 'Neha Patel', 'Furniture', 18500.00, 'COMPLETED'),
    (106, 4, 'Priya Nair', 'Accessories', 2200.00, 'COMPLETED'),
    (107, 1, 'Aarav Sharma', 'Accessories', 1500.00, 'COMPLETED'),
    (108, 5, 'Vikram Singh', 'Electronics', 95000.00, 'COMPLETED'),
    (109, 2, 'Neha Patel', 'Electronics', 52000.00, 'COMPLETED'),
    (110, 4, 'Priya Nair', 'Accessories', 1800.00, 'COMPLETED'),
    (111, 4, 'Priya Nair', 'Accessories', 3100.00, 'COMPLETED');

-- ==========================================================
-- 2. Basic HAVING Filter on Groups
-- ==========================================================

-- Find customers who placed more than 2 completed orders
SELECT 
    customer_id,
    customer_name,
    COUNT(order_id) AS total_orders
FROM customer_orders
WHERE order_status = 'COMPLETED'
GROUP BY customer_id, customer_name
HAVING COUNT(order_id) > 2;

-- Find product categories generating over 50,000 in total sales
SELECT 
    category,
    COUNT(order_id) AS items_sold,
    SUM(order_amount) AS total_sales
FROM customer_orders
WHERE order_status = 'COMPLETED'
GROUP BY category
HAVING SUM(order_amount) > 50000.00
ORDER BY total_sales DESC;

-- ==========================================================
-- 3. Combining WHERE and HAVING in a Single Pipeline
-- ==========================================================

-- High-value customers: Consider ONLY 'COMPLETED' transactions (WHERE),
-- and select customers with an average spend greater than 20,000 (HAVING)
SELECT 
    customer_id,
    customer_name,
    COUNT(order_id) AS completed_orders_count,
    ROUND(AVG(order_amount), 2) AS avg_ticket_size,
    SUM(order_amount) AS total_spent
FROM customer_orders
WHERE order_status = 'COMPLETED'
GROUP BY customer_id, customer_name
HAVING AVG(order_amount) >= 20000.00
ORDER BY total_spent DESC;

-- ==========================================================
-- 4. Multiple Conditions in HAVING
-- ==========================================================

-- Find repeat customers (>= 2 orders) who spent more than 30,000 overall
SELECT 
    customer_name,
    COUNT(order_id) AS order_count,
    SUM(order_amount) AS total_value
FROM customer_orders
WHERE order_status = 'COMPLETED'
GROUP BY customer_name
HAVING COUNT(order_id) >= 2 
   AND SUM(order_amount) > 30000.00;
