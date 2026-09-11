# 📅 Day 11: Grouping Data (GROUP BY)

## 📌 Overview
Day 11 covers row grouping mechanics using the `GROUP BY` clause. This day focuses on how individual observations are collapsed into categorized subsets, multi-level hierarchy grouping, and the strict column projection rules enforced by relational database engines.

---

## 🎯 Key Learning Objectives
- [x] Master the core execution behavior of the `GROUP BY` clause.
- [x] Group records by single categorical fields to calculate group-level statistics.
- [x] Implement multi-column grouping across hierarchical attributes (e.g., Department + Job Role).
- [x] Understand and adhere to the **Single-Value Rule** (every non-aggregated column in `SELECT` must appear in `GROUP BY`).
- [x] Group by calculated expressions and date intervals (`DATE_TRUNC`, `EXTRACT`).
- [x] Combine `WHERE` filtering with `GROUP BY` to control data prior to aggregation.

---

## 📂 Folder Structure

| File | Purpose |
| :--- | :--- |
| **`Notes.md`** | Theoretical foundations of data grouping, logical execution flow, grouping rules, and common errors. |
| **`queries.sql`** | Executable script containing practical scenarios: department rollups, regional sales breakdowns, and multi-column grouping. |

---


