# Day 04: Data Manipulation Language (DML)

## 🎯 Key Learning Objectives
* Insert single, multiple, and derived records using `INSERT INTO`.
* Modify existing row values accurately using `UPDATE`.
* Remove specific rows while maintaining referential integrity using `DELETE`.
* Understand the critical safety rules regarding `WHERE` clauses during modifications.
* Explore upsert mechanics (`INSERT ... ON CONFLICT` / `REPLACE INTO`).

---

## 1. What is DML?
**Data Manipulation Language (DML)** comprises SQL commands used for managing, modifying, and manipulating data stored within existing relational database tables.

Unlike DDL (which defines structures and auto-commits in many engines), DML operations:
* Target **row-level data**, not schema objects.
* Are **fully transactional** (can be committed or rolled back using TCL).
* Generate row-by-row transaction log entries.

---

## 2. Core DML Commands

| Command | Purpose | Transactional? | Requires `WHERE` for Safety? |
| :--- | :--- | :---: | :---: |
| **`INSERT`** | Adds one or more new rows into a table. | ✅ Yes | ❌ No |
| **`UPDATE`** | Modifies existing column values in one or more rows. | ✅ Yes | ⚠️ Yes (otherwise updates entire table) |
| **`DELETE`** | Removes one or more rows based on a condition. | ✅ Yes | ⚠️ Yes (otherwise wipes all rows) |

---

## 3. Deep Dive into Syntax & Patterns

### A. `INSERT INTO`
Adds records to a table. Specifying column lists is a best practice to avoid errors when table schemas change.

```sql
-- Standard Single-Row Insert
INSERT INTO customers (customer_id, full_name, email, city)
VALUES (1, 'Aarav Sharma', 'aarav@example.com', 'Bengaluru');

-- Multi-Row Insert (Bulk Insert)
INSERT INTO customers (customer_id, full_name, email, city)
VALUES 
    (2, 'Neha Patel', 'neha@example.com', 'Mumbai'),
    (3, 'Rohan Verma', 'rohan@example.com', 'Delhi');

-- Insert from Another Table (INSERT INTO ... SELECT)
INSERT INTO archived_customers (customer_id, full_name, email)
SELECT customer_id, full_name, email 
FROM customers 
WHERE is_active = FALSE;
```

### B. UPDATE
Changes values in specific columns for rows that meet a condition.

⚠️ Critical Rule: Always test your WHERE condition with a SELECT query first before running an UPDATE. Omitting WHERE will update every row in the table.

```SQL
-- Single Column Update
UPDATE customers
SET city = 'Hyderabad'
WHERE customer_id = 1;

-- Multiple Columns Update with Expressions
UPDATE employees
SET 
    salary = salary * 1.10,
    last_review_date = CURRENT_DATE
WHERE department_id = 101 AND performance_score >= 4;
```

### C. DELETE
Removes specific records from a table.

```SQL
-- Targeted Deletion
DELETE FROM customers
WHERE customer_id = 3;

-- Conditional Multi-Row Deletion
DELETE FROM orders
WHERE order_status = 'CANCELLED' 
  AND created_at < CURRENT_DATE - INTERVAL '90 days';
```

### D. Upsert Patterns (Insert or Update)
When inserting a record that might violate a PRIMARY KEY or UNIQUE constraint, upsert patterns handle the collision gracefully.

```SQL
-- PostgreSQL Syntax (ON CONFLICT)
INSERT INTO product_inventory (product_id, quantity)
VALUES (101, 50)
ON CONFLICT (product_id) 
DO UPDATE SET quantity = product_inventory.quantity + EXCLUDED.quantity;

-- MySQL Syntax (ON DUPLICATE KEY UPDATE)
INSERT INTO product_inventory (product_id, quantity)
VALUES (101, 50)
ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity);
```
