# 📅 Day 12: Filtering Aggregations (HAVING vs WHERE)

## 📌 Overview
Day 12 focuses on post-aggregation filtering using the `HAVING` clause, clarifying the fundamental architectural and execution-flow differences between `WHERE` and `HAVING`, and combining both within complex analytical queries.

---

## 🎯 Key Learning Objectives
- [x] Master the purpose and mechanics of the `HAVING` clause.
- [x] Filter aggregated data groups based on conditions like `COUNT()`, `SUM()`, and `AVG()`.
- [x] Understand the execution order distinction: `WHERE` (pre-grouping) vs. `HAVING` (post-grouping).
- [x] Combine `WHERE` and `HAVING` seamlessly in single query pipelines.
- [x] Optimize performance by pushing non-aggregate row filters down to `WHERE` instead of `HAVING`.

---

## 📂 Folder Structure

| File | Purpose |
| :--- | :--- |
| **`Notes.md`** | Detailed theory on aggregation filtering, lifecycle execution rules, optimization guidelines, and syntax traps. |
| **`queries.sql`** | Executable script containing practical scenarios: high-volume departments, high-spending customers, and combined WHERE/HAVING filters. |

---

