# Day 14: Outer Joins (LEFT, RIGHT, FULL OUTER)

## 🎯 Key Learning Objectives
* Understand how outer joins preserve unmatched records by substituting missing relational attributes with `NULL`.
* Master the mechanics and business use cases for `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN`.
* Implement the Anti-Join pattern to identify records that lack corresponding relationships.
* Avoid the classic outer join mistake: filtering the outer table in the `WHERE` clause instead of the `ON` clause.

---

## 1. Inner Joins vs. Outer Joins

* **`INNER JOIN`**: Returns **only matching rows** between Table A and Table B. Any row without a match in either table is excluded.
* **`OUTER JOIN`**: Preserves rows from one or both tables even when no match exists in the counterpart table, populating missing values with `NULL`.

---

## 2. The Three Outer Join Types

### A. `LEFT JOIN` (or `LEFT OUTER JOIN`)
Returns **all rows from the left table** (Table A), along with matched rows from the right table (Table B). If no match exists, columns from Table B return `NULL`.

```text
Table A (Users)               Table B (Orders)
+----+---------+              +----------+---------+--------+
| id | name    |              | order_id | user_id | amount |
+----+---------+              +----------+---------+--------+
| 1  | Aarav   |              | 101      | 1       | 500.00 |
| 2  | Neha    |              +----------+---------+--------+
| 3  | Vikram  |              
+----+---------+              

LEFT JOIN Result (Users LEFT JOIN Orders ON id = user_id):
+----+---------+----------+--------+
| id | name    | order_id | amount |
+----+---------+----------+--------+
| 1  | Aarav   | 101      | 500.00 |
| 2  | Neha    | NULL     | NULL   |
| 3  | Vikram  | NULL     | NULL   |
+----+---------+----------+--------+
```

### B. RIGHT JOIN (or RIGHT OUTER JOIN)
Returns all rows from the right table (Table B), along with matched rows from the left table (Table A).

💡 Industry Best Practice: Most production data teams standardize on LEFT JOIN exclusively. 
Any RIGHT JOIN can be rewritten as a LEFT JOIN simply by swapping table order, which keeps query readability consistent from left to right:

```SQL
-- A RIGHT JOIN B is identical to B LEFT JOIN A
SELECT * FROM orders o LEFT JOIN users u ON o.user_id = u.id;
```

### C. FULL OUTER JOIN
Returns all rows when there is a match in either the left or right table. 
Rows with no match on either side contain NULL for the missing side's attributes.

- Excellent for data audits, catalog reconciliations, and identifying disjoint sets.

- Engine Note: Supported in PostgreSQL, Oracle, and SQL Server.
MySQL does not natively support FULL OUTER JOIN (emulated via LEFT JOIN UNION ALL RIGHT JOIN).

### 3. The Anti-Join Pattern (Finding Orphans / Inactive Records)
An Anti-Join returns rows from the left table that have no corresponding records in the right table.
This is achieved by combining a LEFT JOIN with a WHERE ... IS NULL check on the right table's primary key:

```SQL
-- Find users who have NEVER placed an order
SELECT u.user_id, u.name
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE o.order_id IS NULL;
```

4. The Critical Trap: ON vs. WHERE in Outer Joins
Where you place a filter condition completely alters outer join behavior:

Filter in ON clause:
Filters the right table before the join happens. Unmatched left rows are still retained.

```SQL
-- Returns ALL users; order data appears ONLY if order was placed in 2026
SELECT u.name, o.order_id, o.order_date
FROM users u
LEFT JOIN orders o 
    ON u.user_id = o.user_id 
   AND o.order_date >= '2026-01-01';
```

Filter in WHERE clause:
Filters the dataset after the join. Any row where the right table produced NULL will be discarded, silently turning your LEFT JOIN into an INNER JOIN!

```SQL
-- ⚠️ TURNS INTO INNER JOIN: Drops all users who haven't placed an order!
SELECT u.name, o.order_id, o.order_date
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE o.order_date >= '2026-01-01';
```
