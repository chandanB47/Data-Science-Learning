# Day 13: Inner Joins & Relational Mapping

## 🎯 Key Learning Objectives
* Understand how relational joins combine rows from two or more tables based on a related column.
* Master the mechanics of `INNER JOIN`: returning only rows where a match exists in both datasets.
* Avoid Cartesian products caused by missing or incorrect join conditions.
* Use table aliasing for clean readability and to resolve ambiguous column names.
* Chain multiple `INNER JOIN` clauses to traverse normalized database schemas.

---

## 1. What is an `INNER JOIN`?

An **`INNER JOIN`** creates a new result table by combining column values of two tables ($A$ and $B$) based upon a predicate (the `ON` clause).

* It evaluates each row of table $A$ against every row of table $B$.
* **Intersection Only**: Only rows satisfying the join condition appear in the result set. If a row in Table $A$ has no match in Table $B$, that row is dropped from the output.

```text
Table A (Employees)        Table B (Departments)
+----+---------+--------+  +----+-------------+
| id | name    | dept_id|  | id | dept_name   |
+----+---------+--------+  +----+-------------+
| 1  | Aarav   | 10     |  | 10 | Engineering |
| 2  | Neha    | 20     |  | 20 | Analytics   |
| 3  | Vikram  | 99     |  +----+-------------+
+----+---------+--------+

INNER JOIN Output (Only matches where dept_id = id):
+----+-------+-------------+
| id | name  | dept_name   |
+----+-------+-------------+
| 1  | Aarav | Engineering |
| 2  | Neha  | Analytics   |
+----+-------+-------------+
(Vikram is omitted because dept_id 99 does not exist in Departments)
```

### 2. ANSI SQL Join Syntax vs Legacy JoinsModern Explicit Join (Standard Best Practice)

```SQL
SELECT 
    e.first_name, 
    d.department_name
FROM employees AS e
INNER JOIN departments AS d 
    ON e.department_id = d.department_id;
```

#### Legacy Implicit Join (Anti-Pattern)
SQL-- Avoid this syntax: omits clear join separation and risks accidental Cartesian products

```sql
SELECT 
    e.first_name, 
    d.department_name
FROM employees e, departments d
WHERE e.department_id = d.department_id;
```

### 3. Resolving Ambiguous Column NamesWhen two tables share a column name (such as id or created_at), 
referencing that column without qualifying which table it belongs to triggers an SQL error:
- Error: column reference "id" is ambiguous
- Fix: Prefix the column with the table name or table alias: e.id or d.id.


### 4. Multi-Table Joins (Traversing Schemas)
Real-world queries often traverse bridge tables or intermediate relations.
For example, connecting Customers to Products via an Orders bridge table:

$$\text{Customers} \longleftrightarrow \text{Orders} \longleftrightarrow \text{Products}$$

```SQL
SELECT 
    c.customer_name,
    o.order_id,
    p.product_name,
    p.unit_price
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
INNER JOIN products p 
    ON o.product_id = p.product_id;
```
