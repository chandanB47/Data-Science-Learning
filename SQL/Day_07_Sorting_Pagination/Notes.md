# Day 07: Sorting & Pagination

## 🎯 Key Learning Objectives
* Understand why relational database tables have no default physical order.
* Use `ORDER BY` for single-column, multi-column, and expression-based sorting.
* Configure explicit `NULL` ordering with `NULLS FIRST` and `NULLS LAST`.
* Construct page-based queries using `LIMIT` and `OFFSET`.
* Apply the standard ANSI `FETCH FIRST / NEXT` syntax.
* Understand the keyset pagination (cursor-based) alternative for high-volume data.

---

## 1. Sorting Data with `ORDER BY`

In relational databases, tables are treated as unordered mathematical sets. Without an explicit `ORDER BY` clause, the database engine does **not** guarantee any specific return order.

* **Default Direction**: If omitted, `ORDER BY` defaults to ascending order (`ASC`).
* **Direction Keywords**:
  * `ASC`: Smallest to largest / A to Z / Oldest to newest.
  * `DESC`: Largest to smallest / Z to A / Newest to oldest.

```sql
-- Single column descending
SELECT * FROM employees ORDER BY salary DESC;

-- Multi-column sort (sorts by department first, then salary within each department)
SELECT * FROM employees ORDER BY department_id ASC, salary DESC;
```

### 2. Handling NULL Values in SortingEngines differ on where NULL values appear by default when sorting:PostgreSQL / Oracle: NULLS LAST for ASC, NULLS FIRST for DESC.
MySQL / SQL Server: Treats NULL as the lowest possible value.
To ensure consistent, deterministic behavior across engines, use explicit NULLS clauses (supported in PostgreSQL and Oracle):
SQL-- Place NULLs at the end regardless of sort direction

```sql
SELECT employee_id, full_name, commission_pct
FROM sales_reps
ORDER BY commission_pct DESC NULLS LAST;

-- Place NULLs at the very beginning
SELECT employee_id, full_name, commission_pct
FROM sales_reps
ORDER BY commission_pct ASC NULLS FIRST;
```

### 3. Pagination Mechanics (LIMIT & OFFSET)Pagination breaks large datasets into smaller, digestible pages for web pages, APIs, and data exploration.
- LIMIT n: Specifies the maximum number of rows to return.
- OFFSET m: Specifies the number of rows to skip before beginning to return records.
General Formula for Page $N$ with Page Size $S$:$$\text{OFFSET} = (N - 1) \times S$$$$\text{LIMIT} = S$$SQL-- Page 1 (Items 1 to 10)

```sql
SELECT * FROM products ORDER BY product_id ASC LIMIT 10 OFFSET 0;

-- Page 2 (Items 11 to 20)
SELECT * FROM products ORDER BY product_id ASC LIMIT 10 OFFSET 10;

-- Page 3 (Items 21 to 30)
SELECT * FROM products ORDER BY product_id ASC LIMIT 10 OFFSET 20;
```

### 4. ANSI SQL Standard: 
FETCH FIRSTWhile LIMIT and OFFSET are supported by PostgreSQL, MySQL, and SQLite, the official ANSI SQL standard uses OFFSET ... FETCH NEXT:

```SQL
SELECT product_id, product_name, price
FROM products
ORDER BY price DESC
OFFSET 10 ROWS
FETCH NEXT 10 ROWS ONLY;
```
