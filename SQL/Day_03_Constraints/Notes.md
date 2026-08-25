# Day 03: SQL Constraints & Data Integrity

## 🎯 Key Learning Objectives
* Understand the role of database-level constraints in enforcing business rules and data consistency.
* Master column-level and table-level constraint declarations.
* Implement and configure `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`, `CHECK`, and `DEFAULT`.
* Understand cascading referential actions (`CASCADE`, `SET NULL`, `RESTRICT` / `NO ACTION`).
* Add, drop, and modify constraints dynamically on existing schemas.

---

## 1. What are SQL Constraints?
**Constraints** are rules enforced on data columns in a table. They prevent invalid data from being entered into the database, ensuring **Entity Integrity**, **Referential Integrity**, and **Domain Integrity**.

---

## 2. Core SQL Constraints Breakdown

| Constraint | Purpose | Multiple Allowed per Table? | Allows `NULL`? |
| :--- | :--- | :---: | :---: |
| **`PRIMARY KEY`** | Uniquely identifies each record in a table. | ❌ Only 1 | ❌ No |
| **`FOREIGN KEY`** | Enforces a link between columns in two tables (referential integrity). | ✅ Yes | ✅ Yes (unless `NOT NULL` added) |
| **`NOT NULL`** | Ensures a column cannot store `NULL` values. | ✅ Yes | ❌ No |
| **`UNIQUE`** | Ensures all values in a column or set of columns are distinct. | ✅ Yes | ✅ Yes (Engine dependent) |
| **`CHECK`** | Validates that all values in a column satisfy a boolean condition. | ✅ Yes | ✅ Yes |
| **`DEFAULT`** | Inserts a predefined default value if no value is explicitly passed. | ✅ Yes | ✅ Yes |

---

## 3. Detailed Constraints & Syntax

### A. `PRIMARY KEY`
A combination of `NOT NULL` and `UNIQUE`. A table can have only one primary key, which can consist of single or multiple columns (Composite Primary Key).

```sql
-- Single Column PK
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);

-- Composite PK (Table Level)
CREATE TABLE order_items (
    order_id INT,
    item_id INT,
    quantity INT,
    PRIMARY KEY (order_id, item_id)
);
```
### B. FOREIGN KEY & Cascading Actions
Prevents actions that would destroy links between tables and blocks invalid data insertion into foreign key columns.

ON DELETE CASCADE: Deleting parent row deletes all associated child rows automatically.

ON DELETE SET NULL: Deleting parent row sets the child's foreign key column to NULL.

ON DELETE RESTRICT / NO ACTION: Rejects deletion of parent row if matching child rows exist.

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE DEFAULT CURRENT_DATE,
    CONSTRAINT fk_user_order
        FOREIGN KEY (user_id) 
        REFERENCES users(user_id)
        ON DELETE CASCADE
);
```
### C. CHECK Constraint
Enforces domain validity by validating values against a specified predicate.
```sql
CREATE TABLE bank_accounts (
    account_id INT PRIMARY KEY,
    account_holder VARCHAR(100) NOT NULL,
    balance DECIMAL(12, 2) NOT NULL,
    account_type VARCHAR(20),
    CONSTRAINT chk_balance_positive CHECK (balance >= 0),
    CONSTRAINT chk_account_type CHECK (account_type IN ('SAVINGS', 'CURRENT', 'SALARY'))
);
```

### D. NOT NULL & DEFAULT

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
### Managing Constraints on Existing Tables

```sql
-- Add a CHECK constraint
ALTER TABLE products 
ADD CONSTRAINT chk_product_name_len CHECK (LENGTH(product_name) >= 3);

-- Add a UNIQUE constraint
ALTER TABLE users 
ADD CONSTRAINT uq_user_email UNIQUE (email);

-- Drop a constraint (PostgreSQL / MySQL 8.0+)
ALTER TABLE products 
DROP CONSTRAINT chk_product_name_len;

-- Drop Foreign Key (MySQL)
ALTER TABLE orders 
DROP FOREIGN KEY fk_user_order;
```
