```sql
-- ==========================================================
-- Day 02: DDL (Data Definition Language) Hands-On Practice
-- ==========================================================

-- 1. Create a fresh testing schema/table
DROP TABLE IF EXISTS trainees;
DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- 2. ALTER Operations: Adding, modifying, and dropping columns
-- Add a new column
ALTER TABLE courses 
ADD COLUMN duration_weeks INT DEFAULT 6;

-- Add another column for track categorization
ALTER TABLE courses 
ADD COLUMN track VARCHAR(50);

-- Drop a column
ALTER TABLE courses 
DROP COLUMN track;

-- 3. RENAME Operations
-- Rename column
ALTER TABLE courses 
RENAME COLUMN course_name TO title;

-- 4. Insert dummy records to verify TRUNCATE vs DROP behavior
INSERT INTO courses (course_id, title, price, duration_weeks)
VALUES 
    (1, 'SQL for Data Science', 4999.00, 4),
    (2, 'Python Data Analytics', 5999.00, 6),
    (3, 'Applied Machine Learning', 8999.00, 8);

-- Verify records exist
SELECT * FROM courses;

-- 5. TRUNCATE Operation (Empties all rows, keeps schema intact)
TRUNCATE TABLE courses;

-- Table structure is still available, but empty (returns 0 rows)
SELECT * FROM courses;

-- 6. Clean Re-insertion after TRUNCATE
INSERT INTO courses (course_id, title, price, duration_weeks)
VALUES (1, 'Advanced Database Design', 6499.00, 5);

-- 7. DROP Operation (Deletes schema and data entirely)
DROP TABLE IF EXISTS courses;

-- The following query will now throw an error: table does not exist
-- SELECT * FROM courses;
