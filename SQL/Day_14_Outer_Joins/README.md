# 📅 Day 14: Outer Joins (LEFT, RIGHT, FULL OUTER)

## 📌 Overview
Day 14 focuses on outer join variants in SQL: `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN`. You will learn how to preserve unmatched rows from one or both tables, fill non-matching attributes with `NULL`, and perform orphan/exclusion analysis using anti-join patterns.

---

## 🎯 Key Learning Objectives
- [x] Understand how outer joins differ fundamentally from inner joins.
- [x] Master `LEFT JOIN` (LEFT OUTER JOIN) to preserve all left-side records.
- [x] Understand `RIGHT JOIN` and why industry convention favors rewriting it as `LEFT JOIN`.
- [x] Combine all records from both datasets using `FULL OUTER JOIN`.
- [x] Detect missing, inactive, or orphan records using the Anti-Join pattern (`WHERE right_table.id IS NULL`).
- [x] Learn the placement trap: filtering the preserved table in `ON` vs. `WHERE`.

---

## 📂 Folder Structure

| File | Purpose |
| :--- | :--- |
| **`Notes.md`** | Comprehensive theoretical reference on outer join mechanics, Venn diagram representations, anti-joins, and the `ON` vs `WHERE` filtering trap. |
| **`queries.sql`** | Executable script featuring customer churn analysis, zero-order user detection, full catalog reconciliations, and anti-joins. |

---
