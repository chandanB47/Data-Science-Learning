```sql
-- ==========================================================
-- Day 09: Date & Time Operations Hands-On Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Sample Records
DROP TABLE IF EXISTS subscriptions;
DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_timestamp TIMESTAMP NOT NULL,
    shipped_timestamp TIMESTAMP,
    delivered_timestamp TIMESTAMP
);

CREATE TABLE subscriptions (
    sub_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    plan_name VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    duration_months INT NOT NULL,
    cancellation_date DATE
);

INSERT INTO orders (order_id, customer_id, order_timestamp, shipped_timestamp, delivered_timestamp)
VALUES 
    (101, 1, '2026-08-01 10:15:30', '2026-08-01 16:00:00', '2026-08-03 14:20:00'),
    (102, 2, '2026-08-15 14:45:00', '2026-08-16 09:30:00', '2026-08-18 11:10:00'),
    (103, 3, '2026-08-28 20:05:10', '2026-08-29 11:00:00', NULL),
    (104, 1, '2026-09-01 08:30:00', '2026-09-01 12:00:00', '2026-09-02 18:45:00'),
    (105, 4, '2026-09-05 18:22:15', NULL, NULL);

INSERT INTO subscriptions (sub_id, user_id, plan_name, start_date, duration_months, cancellation_date)
VALUES 
    (1, 1001, 'Annual Pro', '2025-09-01', 12, NULL),
    (2, 1002, 'Monthly Basic', '2026-07-15', 1, '2026-08-14'),
    (3, 1003, 'Quarterly Plus', '2026-06-01', 3, NULL),
    (4, 1004, 'Annual Pro', '2026-01-10', 12, NULL);

-- ==========================================================
-- 2. Extracting Parts & Analytical Fields (EXTRACT)
-- ==========================================================

SELECT 
    order_id,
    order_timestamp,
    EXTRACT(YEAR FROM order_timestamp) AS order_year,
    EXTRACT(MONTH FROM order_timestamp) AS order_month,
    EXTRACT(DAY FROM order_timestamp) AS order_day,
    EXTRACT(HOUR FROM order_timestamp) AS order_hour,
    -- Day of week: 0 = Sunday, 6 = Saturday in PostgreSQL
    EXTRACT(DOW FROM order_timestamp) AS day_of_week
FROM orders;

-- ==========================================================
-- 3. Date Arithmetic: Durations & Fulfillment SLAs
-- ==========================================================

SELECT 
    order_id,
    order_timestamp,
    delivered_timestamp,
    -- Time taken to fulfill order in days and hours
    (delivered_timestamp - order_timestamp) AS total_fulfillment_time,
    -- Check if delivery SLA (within 48 hours) was met
    CASE 
        WHEN delivered_timestamp IS NULL THEN 'In Transit / Pending'
        WHEN delivered_timestamp <= order_timestamp + INTERVAL '48 hours' THEN 'Within SLA'
        ELSE 'SLA Breached'
    END AS sla_status
FROM orders;

-- ==========================================================
-- 4. Subscription Renewal Dates & Active Status
-- ==========================================================

SELECT 
    sub_id,
    user_id,
    plan_name,
    start_date,
    duration_months,
    -- Calculate expiration date using INTERVAL
    (start_date + (duration_months || ' months')::INTERVAL)::DATE AS renewal_due_date,
    -- Active status based on CURRENT_DATE
    CASE 
        WHEN cancellation_date IS NOT NULL THEN 'Cancelled'
        WHEN CURRENT_DATE > (start_date + (duration_months || ' months')::INTERVAL)::DATE THEN 'Expired'
        ELSE 'Active'
    END AS subscription_status
FROM subscriptions;

-- ==========================================================
-- 5. Time-Series Aggregation using DATE_TRUNC
-- ==========================================================

-- Aggregate orders by month
SELECT 
    DATE_TRUNC('month', order_timestamp)::DATE AS order_month,
    COUNT(order_id) AS orders_count
FROM orders
GROUP BY DATE_TRUNC('month', order_timestamp)
ORDER BY order_month;

-- Format dates cleanly for business reporting (PostgreSQL TO_CHAR)
SELECT 
    order_id,
    TO_CHAR(order_timestamp, 'FMMonth DD, YYYY - HH12:MI AM') AS formatted_order_time
FROM orders;
