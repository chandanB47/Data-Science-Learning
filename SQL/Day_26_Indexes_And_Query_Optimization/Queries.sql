-- ==========================================================
-- Day 26: Indexes & Query Optimization Practice (MySQL 8.0+)
-- ==========================================================

USE retail_analytics;

DROP TABLE IF EXISTS audit_activity;

CREATE TABLE audit_activity (
    activity_id INT PRIMARY KEY AUTO_INCREMENT,
    user_email VARCHAR(120) NOT NULL,
    service_module VARCHAR(50) NOT NULL,
    action_type VARCHAR(30) NOT NULL,
    latency_ms DECIMAL(8, 2) NOT NULL,
    created_at DATETIME NOT NULL
);

-- Seed records
INSERT INTO audit_activity (user_email, service_module, action_type, latency_ms, created_at) VALUES
('aarav@retail.in',  'Billing',   'CHECKOUT', 120.50, '2026-08-01 10:14:00'),
('neha@retail.in',   'Inventory', 'RESTOCK',   45.20, '2026-08-01 11:30:10'),
('rohan@retail.in',  'Billing',   'CHECKOUT', 310.00, '2026-08-02 09:15:22'),
('priya@retail.in',  'Auth',      'LOGIN',     12.00, '2026-08-02 09:20:00'),
('vikram@retail.in', 'Inventory', 'AUDIT',    850.40, '2026-08-03 14:00:00'),
('aarav@retail.in',  'Auth',      'LOGOUT',    10.50, '2026-08-03 18:00:00'),
('neha@retail.in',   'Billing',   'REFUND',   240.10, '2026-08-04 12:10:05'),
('ananya@retail.in', 'Analytics', 'EXPORT',  1420.00, '2026-08-05 16:45:00');

-- ==========================================================
-- 1. Baseline Full Table Scan Check
-- ==========================================================

-- Expected: type = ALL, key = NULL
EXPLAIN 
SELECT * FROM audit_activity 
WHERE user_email = 'aarav@retail.in';

-- ==========================================================
-- 2. Creating Single & Composite Indexes
-- ==========================================================

-- Single-column index
CREATE INDEX idx_audit_user_email ON audit_activity(user_email);

-- Verify index lookup (type changes to 'ref')
EXPLAIN 
SELECT * FROM audit_activity 
WHERE user_email = 'aarav@retail.in';

-- Composite index
CREATE INDEX idx_audit_module_action ON audit_activity(service_module, action_type);

-- ==========================================================
-- 3. Leftmost Prefix Rule Validation
-- ==========================================================

-- A. Uses full composite index (both columns present)
EXPLAIN 
SELECT * FROM audit_activity 
WHERE service_module = 'Billing' AND action_type = 'CHECKOUT';

-- B. Still uses composite index (leading column service_module present)
EXPLAIN 
SELECT * FROM audit_activity 
WHERE service_module = 'Billing';

-- C. Cannot use index (action_type without service_module -> type: ALL)
EXPLAIN 
SELECT * FROM audit_activity 
WHERE action_type = 'CHECKOUT';

-- ==========================================================
-- 4. SARGable vs Non-SARGable Queries
-- ==========================================================

CREATE INDEX idx_audit_created ON audit_activity(created_at);

-- Non-SARGable: Wrapping indexed column in DATE() triggers full table scan (ALL)
EXPLAIN 
SELECT * FROM audit_activity 
WHERE DATE(created_at) = '2026-08-01';

-- SARGable: Range query leverages index seek (type: range)
EXPLAIN 
SELECT * FROM audit_activity 
WHERE created_at >= '2026-08-01 00:00:00' 
  AND created_at <  '2026-08-02 00:00:00';

-- ==========================================================
-- 5. Covering Index Optimization (Extra: Using index)
-- ==========================================================

-- All selected columns exist directly within the composite index tree,
-- avoiding additional table reads
EXPLAIN 
SELECT service_module, action_type 
FROM audit_activity 
WHERE service_module = 'Billing';

-- MySQL 8.0+ EXPLAIN ANALYZE (Profiles exact execution duration and actual rows)
EXPLAIN ANALYZE 
SELECT service_module, action_type 
FROM audit_activity 
WHERE service_module = 'Billing';
