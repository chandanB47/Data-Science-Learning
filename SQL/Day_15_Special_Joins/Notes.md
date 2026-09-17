# Day 15: Special Joins (CROSS JOIN & SELF JOIN)

## 🎯 Key Learning Objectives
* Master the mechanics, performance trade-offs, and use cases of `CROSS JOIN`.
* Construct complete reporting matrices (e.g., all products $\times$ all months) to ensure zero-sale intervals are not dropped in aggregations.
* Understand self-referencing foreign keys and how to traverse them using `SELF JOIN`.
* Implement organizational reporting lines (Employee $\longleftrightarrow$ Manager).
* Write non-equi self joins to detect duplicates or calculate pairwise differences.

---

## 1. What is a `CROSS JOIN`?

A **`CROSS JOIN`** produces a **Cartesian product** of two tables. Every row from Table A is paired with every row from Table B.

* If Table A has $M$ rows and Table B has $N$ rows, the resulting relation contains $M \times N$ rows.
* A `CROSS JOIN` does **not** take an `ON` clause because it has no match condition.

```text
Table A (Sizes: 2 rows)     Table B (Colors: 3 rows)
+------+                    +-------+
| size |                    | color |
+------+                    +-------+
| S    |                    | Red   |
| M    |                    | Blue  |
+------+                    | Green |
                            +-------+
```
```text
CROSS JOIN Result (2 x 3 = 6 rows):
+------+-------+
| size | color |
+------+-------+
| S    | Red   |
| S    | Blue  |
| S    | Green |
| M    | Red   |
| M    | Blue  |
| M    | Green |
+------+-------+

```

Real-World Use Case: Reporting SkeletonsWhen aggregating sales by month and department,
departments with zero sales in a given month normally disappear from the result.
Crossing a distinct list of departments with a list of all calendar months creates a template grid that can then be left-joined to actual sales.


### 2. What is a SELF JOIN?
#### A SELF JOIN is a regular join (INNER or LEFT) where a table is joined with itself.
- It requires distinct table aliases to allow the SQL engine to treat the single physical table as two separate virtual instances.
- Most commonly used when a table contains a self-referencing foreign key (e.g., manager_id referencing employee_id within the same table).Plaintextemployees Table:

```text
+----+---------+------------+
| id | name    | manager_id |
+----+---------+------------+
| 1  | Aarav   | NULL       |  <-- CEO / Top-level Manager
| 2  | Neha    | 1          |  <-- Reports to Aarav
| 3  | Vikram  | 1          |  <-- Reports to Aarav
+----+---------+------------+

```

```sql
SELF JOIN Query:
SELECT 
    e.name AS employee_name,
    COALESCE(m.name, 'Top Level') AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

```


### 3. Pairwise Non-Equi Self Joins
Self joins are not limited to equality matches (=). Non-equi joins (< or >) allow comparing rows within the same table without producing mirror duplicates:

```SQL

-- Find all pairs of employees working in the same department
-- Using 'e1.id < e2.id' prevents comparing an employee to themselves 
-- and avoids duplicate reciprocal pairs like (A, B) and (B, A).
SELECT 
    e1.name AS employee_one,
    e2.name AS employee_two,
    e1.department_id
FROM employees e1
INNER JOIN employees e2 
    ON e1.department_id = e2.department_id 
   AND e1.id < e2.id;
```

### 4. Summary & Best PracticesBeware of Cartesian explosions:

  - A CROSS JOIN between two tables of 10,000 rows generates $100,000,000$ rows, which can exhaust memory.
  
  - Always alias meaningfully in Self Joins: Use descriptive aliases like emp and mgr, or curr and prev, rather than generic t1 and t2.
  
  - Use LEFT JOIN for top-level entities: Using an INNER JOIN on a manager hierarchy will silently drop the CEO or business owner whose manager_id is NULL.
