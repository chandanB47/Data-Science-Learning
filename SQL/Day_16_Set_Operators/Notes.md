# Day 16: Set Operators (UNION, UNION ALL, INTERSECT, EXCEPT)

## 🎯 Key Learning Objectives
* Distinguish between horizontal combinations (`JOIN`) and vertical combinations (`SET OPERATORS`).
* Choose appropriately between `UNION` and `UNION ALL` based on deduplication needs and query performance.
* Find common elements between two query projections with `INTERSECT`.
* Find unique elements belonging to one query but not another with `EXCEPT`.
* Adhere strictly to SQL schema compatibility requirements for set queries.

---

## 1. Joins vs. Set Operators

* **Joins (Horizontal)**: Combine columns from two tables side-by-side based on a related key condition (`ON`).
* **Set Operators (Vertical)**: Stack rows from two or more query outputs on top of each other.

---

## 2. Strict Structural Rules for Set Operations

For any set operation to execute successfully, all participating queries must satisfy two requirements:

1. **Equal Column Count**: Every `SELECT` query must return the exact same number of columns.
2. **Compatible Data Types**: Corresponding columns in each query must share compatible data types (e.g., column 1 must be integer-compatible in both queries; column 2 must be text-compatible).

> 💡 **Column Names Rule**: The column names in the final result set are determined exclusively by the aliases defined in the **first** `SELECT` query.

---

## 3. Core Set Operators

### A. `UNION`
Combines results from multiple queries and **removes duplicate rows** across the combined set.

* Incurs a performance overhead because the engine performs an internal sorting/hash-deduplication pass.

### B. `UNION ALL`
Combines results from multiple queries and **retains all duplicates**.

* **Significantly faster** than `UNION` because no sorting or deduplication pass is executed.
* Standard choice when you know the input sets are disjoint or when duplicates must be preserved for metric totals.

### C. `INTERSECT`
Returns only rows that exist in **both** query result sets (the set intersection).

* *Dialect Support*: PostgreSQL, SQL Server, Oracle, and MySQL 8.0.31+.

### D. `EXCEPT` (or `MINUS`)
Returns rows that appear in the first query result set but **do not appear** in the second query result set (set difference: $A - B$).

* *Dialect Support*: Called `EXCEPT` in PostgreSQL, SQLite, and MySQL 8.0.31+; called `MINUS` in Oracle.

---

## 4. Summary Matrix

| Operator | Action | Keeps Duplicates? | Performance |
| :--- | :--- | :---: | :--- |
| **`UNION`** | Combines rows $A \cup B$ | ❌ No | Moderate (Sorting overhead) |
| **`UNION ALL`** | Combines rows $A \cup B$ | ✅ Yes | Fastest (Direct concatenation) |
| **`INTERSECT`** | Shared rows $A \cap B$ | ❌ No | Moderate |
| **`EXCEPT` / `MINUS`** | Difference $A \setminus B$ | ❌ No | Moderate |

---

## 5. Sorting Combined Sets (`ORDER BY`)

An `ORDER BY` clause can only appear once, at the very end of the entire set operation query:

```sql
SELECT employee_name, city FROM retail_staff
UNION ALL
SELECT contractor_name, city FROM delivery_partners
ORDER BY city ASC;
