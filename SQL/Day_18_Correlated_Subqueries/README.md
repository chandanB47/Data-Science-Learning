# 📅 Day 18: Correlated Subqueries & EXISTS / NOT EXISTS

## 📌 Overview
Day 18 focuses on correlated subqueries, where the inner query depends dynamically on values from the current candidate row of the outer query. This day covers row-by-row execution mechanics, group-relative comparisons, and boolean existence checks using `EXISTS` and `NOT EXISTS`.

---

## 🎯 Key Learning Objectives
- [x] Understand the difference between independent (non-correlated) and correlated subqueries.
- [x] Master the execution flow: outer query candidate row $\to$ inner query evaluation $\to$ filter resolution.
- [x] Compare rows to group-level aggregates (e.g., finding employees earning above their own department's average).
- [x] Master `EXISTS` and `NOT EXISTS` operators for high-performance existence validation.
- [x] Understand why `EXISTS` short-circuits (early exit) and handles `NULL` values safely compared to `IN` / `NOT IN`.
- [x] Formulate correlated subqueries inside `UPDATE` and `DELETE` statements.

---

## 📂 Folder Structure

| File | Purpose |
| :--- | :--- |
| **`Notes.md`** | Theoretical foundations of correlated execution, row-by-row lifecycle, EXISTS mechanics, and NULL handling differences. |
| **`queries.sql`** | Hands-on SQL script covering department-relative salary checks, active customer checks, unplaced orders, and correlated updates. |

---

