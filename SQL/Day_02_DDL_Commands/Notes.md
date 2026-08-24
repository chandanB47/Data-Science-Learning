# Day 02: Data Definition Language (DDL)

## 🎯 Key Learning Objectives
* Create databases, schemas, and relational tables using `CREATE`.
* Modify existing schemas (add, rename, drop, modify columns) using `ALTER`.
* Rename database objects safely with `RENAME`.
* Clear data instantly while preserving schema structure using `TRUNCATE`.
* Completely eliminate database objects using `DROP`.
* Understand the core differences between `DELETE`, `TRUNCATE`, and `DROP`.

---

## 1. What is DDL?
**Data Definition Language (DDL)** consists of SQL statements used to define, alter, manage, and delete the structure (schema) of database objects such as databases, tables, schemas, views, and indexes.

* **Target**: Modifies database metadata (structural definitions) rather than individual data rows.
* **Auto-Commit Behavior**: In most relational database engines (e.g., MySQL, Oracle), DDL commands execute with an implicit commit, making them immediate and permanent.

---

## 2. DDL Commands Breakdown

### A. `CREATE` (Building Database Objects)
Used to initialize new databases, schemas, and relational tables with defined columns, data types, and integrity constraints.

```sql
-- 1. Create a database
CREATE DATABASE company_db;

-- 2. Create a relational table with constraints
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    department_id INT,
    joining_date DATE DEFAULT CURRENT_DATE
);
```

### B. ALTER (Modifying Existing Schemas)
Modifies the schema of an existing table without deleting or recreating the table.

```sql
-- 1. Add a new column
ALTER TABLE employees 
ADD COLUMN phone_number VARCHAR(15);

-- 2. Drop an existing column
ALTER TABLE employees 
DROP COLUMN phone_number;

-- 3. Modify column data type or size
-- MySQL syntax:
ALTER TABLE employees 
MODIFY COLUMN email VARCHAR(150);

-- PostgreSQL syntax:
ALTER TABLE employees 
ALTER COLUMN email TYPE VARCHAR(150);

-- 4. Add a constraint
ALTER TABLE employees 
ADD CONSTRAINT chk_salary_min CHECK (salary >= 10000);

-- 5. Drop a constraint
ALTER TABLE employees 
DROP CONSTRAINT chk_salary_min;

-- 6. Set or drop a default value
ALTER TABLE employees 
ALTER COLUMN joining_date SET DEFAULT CURRENT_DATE;
```

### C. RENAME (Renaming Database Objects Safely)
Used to rename existing tables or individual columns.

```sql
-- Rename a column within a table
ALTER TABLE employees 
RENAME COLUMN email TO corporate_email;

-- Rename a table (PostgreSQL / MySQL)
ALTER TABLE employees 
RENAME TO staff_members;

-- Alternative MySQL syntax:
RENAME TABLE employees TO staff_members;
```

### D. TRUNCATE (Instant Data Clearing)
Removes all records from a table quickly by deallocating data pages instead of scanning rows one by one.

 Retains table structure, column definitions, and constraints.
 Resets auto-increment/identity sequences back to the initial seed value in most database engines.

```sql
TRUNCATE TABLE staff_members;
```

### E. DROP (Completely Eliminating Objects)
Permanently destroys a database object from the data catalog along with all its data, indexes, permissions, and constraints.

```sql
-- Drop table safely to avoid runtime errors
DROP TABLE IF EXISTS staff_members;

-- Drop table and remove dependent foreign keys (PostgreSQL)
DROP TABLE IF EXISTS departments CASCADE;

-- Drop an entire database
DROP DATABASE IF EXISTS company_db;
```
