```sql
-- ==========================================================
-- Day 29: Project 1 - E-Commerce Analytics & RFM Model (MySQL 8.0+)
-- ==========================================================

DROP DATABASE IF EXISTS ecommerce_analytics;
CREATE DATABASE ecommerce_analytics;
USE ecommerce_analytics;

-- ==========================================================
-- 1. Schema Definition
-- ==========================================================

CREATE TABLE dim_customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    country VARCHAR(50) NOT NULL,
    registration_date DATE NOT NULL
);

CREATE TABLE dim_products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    cost_price DECIMAL(10, 2) NOT NULL,
    retail_price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE fct_orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    order_status VARCHAR(20) NOT NULL CHECK (order_status IN ('COMPLETED', 'CANCELLED', 'REFUNDED')),
    payment_method VARCHAR(30) NOT NULL,
    CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id)
);

CREATE TABLE fct_order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    discount_pct DECIMAL(4, 2) DEFAULT 0.00,
    CONSTRAINT fk_items_order FOREIGN KEY (order_id) REFERENCES fct_orders(order_id),
    CONSTRAINT fk_items_product FOREIGN KEY (product_id) REFERENCES dim_products(product_id)
);

-- ==========================================================
-- 2. Seed Data
-- ==========================================================

INSERT INTO dim_customers (customer_name, email, country, registration_date) VALUES
('Aarav Sharma', 'aarav@domain.com', 'India', '2025-01-10'),
('Neha Patel',   'neha@domain.com',  'India', '2025-03-15'),
('Vikram Singh', 'vikram@domain.com','India', '2025-05-20'),
('Priya Nair',   'priya@domain.com', 'India', '2025-07-01'),
('Rohan Verma',  'rohan@domain.com', 'India', '2025-08-11'),
('Ananya Sen',   'ananya@domain.com','India', '2026-01-05');

INSERT INTO dim_products (product_name, category, cost_price, retail_price) VALUES
('Noise-Cancelling Headphones', 'Electronics', 6000.00, 12000.00),
('Mechanical Keyboard',        'Electronics', 2500.00,  5000.00),
('Ergonomic Office Chair',     'Furniture',   8000.00, 16000.00),
('Standing Desk Mat',          'Furniture',   1000.00,  2500.00),
('Ceramic Coffee Mug',         'Lifestyle',    150.00,   500.00);

INSERT INTO fct_orders (order_id, customer_id, order_date, order_status, payment_method) VALUES
(1001, 1, '2026-09-15', 'COMPLETED', 'UPI'),
(1002, 1, '2026-09-20', 'COMPLETED', 'Credit Card'),
(1003, 1, '2026-09-28', 'COMPLETED', 'UPI'),
(1004, 2, '2026-06-10', 'COMPLETED', 'Debit Card'),
(1005, 2, '2026-07-15', 'COMPLETED', 'UPI'),
(1006, 3, '2026-01-20', 'COMPLETED', 'Net Banking'),
(1007, 4, '2026-08-01', 'COMPLETED', 'Credit Card'),
(1008, 4, '2026-09-25', 'COMPLETED', 'UPI'),
(1009, 5, '2026-02-14', 'REFUNDED',  'Credit Card'),
(1010, 6, '2026-09-26', 'COMPLETED', 'UPI');

INSERT INTO fct_order_items (order_id, product_id, quantity, unit_price, discount_pct) VALUES
(1001, 1, 1, 12000.00, 0.05),
(1001, 2, 1,  5000.00, 0.00),
(1002, 3, 1, 16000.00, 0.10),
(1003, 5, 2,   500.00, 0.00),
(1004, 2, 1,  5000.00, 0.00),
(1005, 4, 1,  2500.00, 0.00),
(1006, 1, 1, 12000.00, 0.00),
(1007, 3, 1, 16000.00, 0.05),
(1008, 2, 2,  5000.00, 0.00),
(1009, 1, 1, 12000.00, 0.00),
(1010, 5, 4,   500.00, 0.00);

-- ==========================================================
-- 3. Sales Breakdown: Category Performance & Margins
-- ==========================================================

SELECT 
    p.category,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.quantity) AS total_units_sold,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_pct)), 2) AS net_revenue,
    ROUND(SUM(oi.quantity * (oi.unit_price * (1 - oi.discount_pct) - p.cost_price)), 2) AS gross_profit,
    ROUND(
        (SUM(oi.quantity * (oi.unit_price * (1 - oi.discount_pct) - p.cost_price)) / 
         SUM(oi.quantity * oi.unit_price * (1 - oi.discount_pct))) * 100, 2
    ) AS margin_pct
FROM fct_order_items oi
INNER JOIN fct_orders o ON oi.order_id = o.order_id
INNER JOIN dim_products p ON oi.product_id = p.product_id
WHERE o.order_status = 'COMPLETED'
GROUP BY p.category
ORDER BY net_revenue DESC;

-- ==========================================================
-- 4. End-to-End RFM Customer Segmentation Model
-- ==========================================================

WITH customer_spend AS (
    -- Step 1: Calculate raw line-item revenue
    SELECT 
        o.customer_id,
        o.order_id,
        o.order_date,
        SUM(oi.quantity * oi.unit_price * (1 - oi.discount_pct)) AS order_val
    FROM fct_orders o
    INNER JOIN fct_order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'COMPLETED'
    GROUP BY o.customer_id, o.order_id, o.order_date
),
rfm_metrics AS (
    -- Step 2: Compute Recency, Frequency, and Monetary scores (Snapshot: 2026-09-30)
    SELECT 
        c.customer_id,
        c.customer_name,
        DATEDIFF('2026-09-30', MAX(cs.order_date)) AS recency_days,
        COUNT(DISTINCT cs.order_id) AS frequency,
        ROUND(COALESCE(SUM(cs.order_val), 0), 2) AS monetary
    FROM dim_customers c
    LEFT JOIN customer_spend cs ON c.customer_id = cs.customer_id
    GROUP BY c.customer_id, c.customer_name
),
rfm_tiers AS (
    -- Step 3: Assign Quartile Scores (1 to 4) using NTILE
    SELECT 
        customer_id,
        customer_name,
        recency_days,
        frequency,
        monetary,
        -- Higher recency days = worse score, so invert order
        NTILE(4) OVER (ORDER BY recency_days DESC) AS r_score,
        NTILE(4) OVER (ORDER BY frequency ASC)   AS f_score,
        NTILE(4) OVER (ORDER BY monetary ASC)    AS m_score
    FROM rfm_metrics
)
-- Step 4: Map Persona Tiers
SELECT 
    customer_id,
    customer_name,
    recency_days,
    frequency,
    monetary,
    CONCAT(r_score, f_score, m_score) AS rfm_combined,
    CASE 
        WHEN r_score >= 3 AND f_score >= 3 AND m_score >= 3 THEN 'Champions'
        WHEN r_score >= 3 AND f_score >= 2 THEN 'Loyal Customers'
        WHEN r_score <= 2 AND f_score >= 3 THEN 'At Risk / High Value'
        WHEN r_score >= 3 AND f_score = 1 THEN 'Recent New Customers'
        ELSE 'Hibernating / Lost'
    END AS customer_segment
FROM rfm_tiers
ORDER BY monetary DESC;
