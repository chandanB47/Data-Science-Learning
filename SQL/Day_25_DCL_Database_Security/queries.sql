-- ==========================================================
-- Day 25: DCL & Database Security Practice (MySQL 8.0+)
-- Run using root or an account with administrative GRANT OPTION
-- ==========================================================

USE retail_analytics;

-- ==========================================================
-- 1. Create Dedicated Test Users
-- ==========================================================

DROP USER IF EXISTS 'junior_analyst'@'localhost';
DROP USER IF EXISTS 'bi_developer'@'localhost';

CREATE USER 'junior_analyst'@'localhost' 
    IDENTIFIED BY 'Analyst#Secure2026';

CREATE USER 'bi_developer'@'localhost' 
    IDENTIFIED BY 'Dev#Secure2026';

-- Lock an account or expire password for rotation compliance
ALTER USER 'junior_analyst'@'localhost' PASSWORD EXPIRE INTERVAL 90 DAY;

-- ==========================================================
-- 2. Direct Object-Level GRANT & REVOKE
-- ==========================================================

-- Grant read-only access to customer and order tables only
GRANT SELECT ON retail_analytics.customers TO 'junior_analyst'@'localhost';
GRANT SELECT ON retail_analytics.orders TO 'junior_analyst'@'localhost';

-- Grant column-level privilege (Allow seeing names and cities, but hide emails/phones)
GRANT SELECT (customer_id, full_name, city) 
ON retail_analytics.customers 
TO 'junior_analyst'@'localhost';

-- Inspect assigned permissions
SHOW GRANTS FOR 'junior_analyst'@'localhost';

-- Revoke orders table access
REVOKE SELECT ON retail_analytics.orders FROM 'junior_analyst'@'localhost';

-- Verify revocation
SHOW GRANTS FOR 'junior_analyst'@'localhost';

-- ==========================================================
-- 3. Role-Based Access Control (RBAC) Pattern
-- ==========================================================

-- Drop roles if they exist
DROP ROLE IF EXISTS 'app_read_only';
DROP ROLE IF EXISTS 'app_data_engineer';

-- 1. Create custom roles
CREATE ROLE 'app_read_only', 'app_data_engineer';

-- 2. Grant permissions to the roles
GRANT SELECT, SHOW VIEW 
ON retail_analytics.* 
TO 'app_read_only';

GRANT SELECT, INSERT, UPDATE, DELETE, CREATE VIEW 
ON retail_analytics.* 
TO 'app_data_engineer';

-- 3. Assign roles to user accounts
GRANT 'app_read_only' TO 'junior_analyst'@'localhost';
GRANT 'app_data_engineer' TO 'bi_developer'@'localhost';

-- 4. Enable roles automatically upon user connection
SET DEFAULT ROLE ALL TO 'junior_analyst'@'localhost';
SET DEFAULT ROLE ALL TO 'bi_developer'@'localhost';

-- Inspect role grants
SHOW GRANTS FOR 'junior_analyst'@'localhost' USING 'app_read_only';
SHOW GRANTS FOR 'bi_developer'@'localhost' USING 'app_data_engineer';

-- ==========================================================
-- 4. Cleanup Sandbox Accounts & Roles
-- ==========================================================

-- DROP USER IF EXISTS 'junior_analyst'@'localhost';
-- DROP USER IF EXISTS 'bi_developer'@'localhost';
-- DROP ROLE IF EXISTS 'app_read_only', 'app_data_engineer';
