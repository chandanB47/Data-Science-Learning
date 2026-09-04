```sql
-- ==========================================================
-- Day 08: String & Scalar Functions Hands-On Practice
-- ==========================================================

-- 1. Setup Sandbox Schema & Raw Dirty Data
DROP TABLE IF EXISTS raw_customers;

CREATE TABLE raw_customers (
    customer_id INT PRIMARY KEY,
    raw_first_name VARCHAR(50),
    raw_last_name VARCHAR(50),
    raw_email VARCHAR(100),
    phone_raw VARCHAR(30),
    account_code VARCHAR(20),
    account_balance DECIMAL(10, 4)
);

INSERT INTO raw_customers (customer_id, raw_first_name, raw_last_name, raw_email, phone_raw, account_code, account_balance)
VALUES 
    (1, '  aarav  ', 'sharma', 'AARAV.SHARMA@GMAIL.COM  ', '+91-9876543210', '984', 15420.7865),
    (2, 'neha', '  PATEL ', 'neha.patel@techcorp.in', '9876501234', '12', 45000.1234),
    (3, 'rohan', 'verma', 'rohan_verma@OUTLOOK.COM', '+91 9123456780', '5421', 820.5000),
    (4, 'priya', '  nair ', 'priya.nair@techcorp.in', '080-23456789', '7', 95340.9990);

-- ==========================================================
-- 2. Cleaning & Standardizing Strings (TRIM, UPPER, LOWER)
-- ==========================================================

SELECT 
    customer_id,
    -- Strip whitespace and title-case/standardize names
    CONCAT(
        UPPER(SUBSTRING(TRIM(raw_first_name), 1, 1)),
        LOWER(SUBSTRING(TRIM(raw_first_name), 2)),
        ' ',
        UPPER(SUBSTRING(TRIM(raw_last_name), 1, 1)),
        LOWER(SUBSTRING(TRIM(raw_last_name), 2))
    ) AS formatted_name,
    -- Normalize email to lowercase and remove spaces
    LOWER(TRIM(raw_email)) AS clean_email
FROM raw_customers;

-- ==========================================================
-- 3. Substring Extraction & Domain Parsing
-- ==========================================================

-- Extract username and email domain separately
SELECT 
    LOWER(TRIM(raw_email)) AS clean_email,
    SUBSTRING(LOWER(TRIM(raw_email)), 1, POSITION('@' IN LOWER(TRIM(raw_email))) - 1) AS email_username,
    SUBSTRING(LOWER(TRIM(raw_email)) FROM POSITION('@' IN LOWER(TRIM(raw_email))) + 1) AS domain_provider
FROM raw_customers;

-- ==========================================================
-- 4. Text Replacement, Padding & Masking
-- ==========================================================

SELECT 
    customer_id,
    -- Standardize fixed-width account numbers (e.g., '00012', '00984')
    LPAD(account_code, 6, '0') AS padded_account_id,
    -- Clean phone number format by stripping dashes and spaces
    REPLACE(REPLACE(REPLACE(phone_raw, '-', ''), ' ', ''), '+91', '') AS normalized_phone,
    -- Data Privacy: Mask email to first char + *** + domain
    CONCAT(
        LEFT(LOWER(TRIM(raw_email)), 1),
        '***@',
        SUBSTRING(LOWER(TRIM(raw_email)) FROM POSITION('@' IN LOWER(TRIM(raw_email))) + 1)
    ) AS masked_email
FROM raw_customers;

-- ==========================================================
-- 5. Scalar Numeric Functions (ROUND, CEIL, FLOOR)
-- ==========================================================

SELECT 
    customer_id,
    account_balance AS original_balance,
    ROUND(account_balance, 2) AS rounded_currency,
    CEIL(account_balance) AS ceiling_value,
    FLOOR(account_balance) AS floor_value
FROM raw_customers;
