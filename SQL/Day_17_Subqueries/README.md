# 📅 Day 17: Subqueries (Scalar, Multi-Row, and Nested)

## 📌 Overview
Day 17 focuses on nested SQL queries (subqueries or inner queries). You will learn how to write queries that depend on the results of another query across different clauses (`WHERE`, `SELECT`, and `FROM`), distinguish between scalar and multi-row subqueries, and use operators like `IN`, `ANY`, and `ALL`.

---

## 🎯 Key Learning Objectives
- [x] Understand what a subquery is and how the database engine executes it from inside out.
- [x] Write **Scalar Subqueries** (returning a single value) in `SELECT` and `WHERE` clauses.
- [x] Write **Multi-Row Subqueries** using `IN`, `NOT IN`, `ANY` / `SOME`, and `ALL`.
- [x] Use subqueries in the `FROM` clause as **Derived Tables** (inline views) with mandatory aliasing.
- [x] Compare subqueries vs. joins in terms of readability, intent, and performance.
- [x] Avoid common pitfalls with `NOT IN` when `NULL` values are present.

---

## 📂 Folder Structure

| File | Purpose |
| :--- | :--- |
| **`Notes.md`** | Complete theoretical breakdown of subquery types, execution order, comparison operators, and NULL traps. |
| **`queries.sql`** | Executable script containing practical scenarios: above-average salaries, department-level thresholds, derived tables, and ANY/ALL comparisons. |

---
