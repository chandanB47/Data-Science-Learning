# Day 05: Data Query Language (DQL) & Basic Querying

## 🎯 Key Learning Objectives
* Understand the role of DQL in relational databases.
* Write robust `SELECT` statements using selective column projection.
* Filter duplicate data points with single-column and composite `DISTINCT`.
* Rename columns and simplify expressions using `AS` aliases.
* Apply arithmetic operators, string manipulation, and `COALESCE` directly in projections.
* Learn the fundamental difference between written SQL syntax and query execution order.

---

## 1. What is DQL?
**Data Query Language (DQL)** is the subset of SQL dedicated to retrieving data stored in relational database tables without altering the underlying data or schema.

* The primary command in DQL is **`SELECT`**.
* Queries return a virtual tabular result set (a relation) derived from one or more base tables or views.

---

## 2. Syntax Order vs. Logical Execution Order

While we write SQL queries in a specific human-readable layout, the SQL database engine evaluates clauses in a distinct logical order:

| Written Clause Order | Logical Execution Order | Description |
| :--- | :---: | :--- |
| `SELECT` | **4** | Specifies which columns, expressions, or aggregates to return |
| `DISTINCT` | **5** | Deduplicates rows in the final projected result set |
| `FROM` | **1** | Identifies source tables and establishes joins |
| `WHERE` | **2** | Filters rows based on boolean conditions |
| `GROUP BY` | **3** | Groups rows sharing common field values |
| `HAVING` | **3b**| Filters grouped rows |
| `ORDER BY` | **6** | Sorts the resulting rows |
| `LIMIT` / `OFFSET` | **7** | Restricts the number of output rows |

> ⚠️ **Key Takeaway**: Because `SELECT` executes *after* `FROM` and `WHERE`, column aliases created in `SELECT` cannot be referenced inside the `WHERE` clause in standard SQL.

---

## 3. Core DQL Concepts & Patterns

### A. Column Projection (`SELECT` vs `SELECT *`)
* `SELECT *`: Retrieves every column defined in the table. Convenient for quick exploration, but discouraged in production because it causes unnecessary I/O overhead and breaks applications if table columns change.
* **Explicit Projection**: Specifying required columns (`SELECT id, name`) minimizes network transfer, utilizes indexes efficiently, and clarifies intent.

```sql
-- Explicit projection
SELECT employee_id, first_name, last_name, salary 
FROM employees;
```

### B. Removing Duplicates (DISTINCT)
DISTINCT filters out identical rows across all requested projection fields.

```SQL
-- Unique departments
SELECT DISTINCT department_id 
FROM employees;

-- Unique combinations of department and job title
SELECT DISTINCT department_id, job_title 
FROM employees;
```

### C. Aliases (AS)
Aliases assign temporary names to columns or tables to improve output readability and make downstream joins concise.

```SQL
-- Column Aliasing
SELECT 
    first_name AS given_name,
    salary * 12 AS annual_compensation
FROM employees;

-- Table Aliasing
SELECT e.employee_id, e.first_name 
FROM employees AS e;
```

### D. Computed Columns & Null Handling
You can calculate values on the fly using standard arithmetic (+, -, *, /) and resolve NULL fields using COALESCE.

COALESCE(val1, val2, ...): Returns the first non-null expression in the argument list.

```SQL
SELECT 
    product_name,
    unit_price,
    discount_amount,
    (unit_price - COALESCE(discount_amount, 0.00)) AS final_price
FROM products;
```
