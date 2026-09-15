```sql
-- ==========================================================
-- Day 13: Inner Joins & Relational Mapping Hands-On Practice
-- ==========================================================

-- 1. Setup Normalized Sandbox Schema
DROP TABLE IF EXISTS order_details;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id) 
        REFERENCES customers(customer_id)
);

CREATE TABLE order_details (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    CONSTRAINT fk_details_order
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
    CONSTRAINT fk_details_product
        FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Seed Sample Records
INSERT INTO customers (customer_id, full_name, city)
VALUES 
    (1, 'Aarav Sharma', 'Bengaluru'),
    (2, 'Neha Patel', 'Mumbai'),
    (3, 'Rohan Verma', 'Delhi'),
    (4, 'Priya Nair', 'Hyderabad'); -- Has no orders

INSERT INTO products (product_id, product_name, category, price)
VALUES 
    (101, 'Ergonomic Desk Chair', 'Furniture', 12500.00),
    (102, 'Mechanical Keyboard', 'Electronics', 4500.00),
    (103, 'Ultra-wide Monitor', 'Electronics', 28000.00),
    (104, 'Noise Cancelling Headphones', 'Electronics', 15000.00);

INSERT INTO orders (order_id, customer_id, order_date)
VALUES 
    (501, 1, '2026-08-01'),
    (502, 1, '2026-08-15'),
    (503, 2, '2026-08-20'),
    (504, 3, '2026-09-02');

INSERT INTO order_details (order_id, product_id, quantity)
VALUES 
    (501, 101, 1),
    (501, 102, 1),
    (502, 103, 2),
    (503, 102, 2),
    (504, 104, 1);

-- ==========================================================
-- 2. Basic Two-Table INNER JOIN
-- ==========================================================

-- Match customers with orders (Notice Priya Nair is omitted: no orders placed)
SELECT 
    c.customer_id,
    c.full_name,
    c.city,
    o.order_id,
    o.order_date
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
ORDER BY o.order_date;

-- ==========================================================
-- 3. Multi-Table Join (Joining Across 4 Tables)
-- ==========================================================

-- Line-item invoice breakdown connecting Customer -> Orders -> Details -> Products
SELECT 
    o.order_id,
    c.full_name AS customer_name,
    p.product_name,
    p.category,
    p.price AS unit_price,
    od.quantity,
    (p.price * od.quantity) AS line_item_total
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
INNER JOIN order_details od 
    ON o.order_id = od.order_id
INNER JOIN products p 
    ON od.product_id = p.product_id
ORDER BY o.order_id, line_item_total DESC;

-- ==========================================================
-- 4. Combining INNER JOIN with Aggregation (GROUP BY)
-- ==========================================================

-- Calculate total spend and order count per customer
SELECT 
    c.customer_id,
    c.full_name,
    c.city,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(p.price * od.quantity) AS total_lifetime_spend
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
INNER JOIN order_details od 
    ON o.order_id = od.order_id
INNER JOIN products p 
    ON od.product_id = p.product_id
GROUP BY c.customer_id, c.full_name, c.city
HAVING SUM(p.price * od.quantity) > 10000.00
ORDER BY total_lifetime_spend DESC;
