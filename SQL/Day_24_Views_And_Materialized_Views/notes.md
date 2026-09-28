# Day 24: Views & Materialized Views

---

## 🎯 Key Learning Objectives
* Understand what a view is (a saved SQL query stored as a schema object).
* Decouple application code from complex underlying database schemas.
* Restrict data visibility using column projections and row-level filters.
* Identify the strict conditions required for an updatable view.
* Distinguish standard virtual views from materialized (physically persisted) views.

---

### 1. What is a View?
A Standard View is a virtual table defined by an underlying query.

It does not store data physically on disk (except for its metadata definition in the data dictionary).

Every time a query references a standard view, the database engine runs the underlying view query dynamically.

```SQL
CREATE OR REPLACE VIEW v_active_customers AS
SELECT customer_id, full_name, email, city
FROM customers
WHERE signup_date >= '2026-01-01';
```

### 2. Why Use Views?
Security & Data Masking: Expose only non-sensitive columns to specific users (e.g., hiding base salary or social security numbers).

Complexity Abstraction: Hide 4-table joins and complex window calculations behind a clean SELECT * FROM v_monthly_sales_summary.

Schema Stability (Indirection): If underlying physical table structures change, updating the view definition prevents breaking downstream client applications or reporting dashboards.

### 3. Updatable Views & WITH CHECK OPTION
Some simple views permit DML operations (INSERT, UPDATE, DELETE) directly against the view, which propagate to the underlying base table.

#### Rules for Updatable Views:
- The view must reference exactly one base table.

- Cannot contain DISTINCT, GROUP BY, HAVING, LIMIT, window functions, or aggregate functions.

- Cannot use UNION or UNION ALL.

#### The WITH CHECK OPTION Guardrail
Prevents updates or inserts that would produce rows the view itself cannot select:

```SQL
CREATE OR REPLACE VIEW v_bengaluru_staff AS
SELECT emp_id, emp_name, city, salary
FROM employees
WHERE city = 'Bengaluru'
WITH CHECK OPTION;

-- ❌ FAILS: The CHECK OPTION rejects this insert because city != 'Bengaluru'
INSERT INTO v_bengaluru_staff (emp_id, emp_name, city, salary)
VALUES (99, 'Kunal Rao', 'Mumbai', 75000.00);
```
