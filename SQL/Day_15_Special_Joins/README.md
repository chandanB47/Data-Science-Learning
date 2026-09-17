# 📅 Day 15: Special Joins (CROSS JOIN & SELF JOIN)

## 📌 Overview
Day 15 explores two specialized join mechanics: `CROSS JOIN` (generating Cartesian products for grid matrices, scenario modeling, and dates/dimensions) and `SELF JOIN` (joining a table with itself to model hierarchies, reporting trees, and sequential row comparisons).

---

## 🎯 Key Learning Objectives
- [x] Understand the mathematical definition and output volume of Cartesian products ($M \times N$).
- [x] Use `CROSS JOIN` to construct permutations, combinations, and master reporting grids.
- [x] Master `SELF JOIN` by aliasing the same table multiple times (`employees AS emp`, `employees AS mgr`).
- [x] Model recursive organizational charts and direct-manager hierarchies.
- [x] Solve pairwise comparison problems (e.g., finding peers sharing the same city or salary band).
- [x] Avoid accidental Cartesian products caused by omitted `ON` clauses.

---

## 📂 Folder Structure

| File | Purpose |
| :--- | :--- |
| **`Notes.md`** | Detailed theory on Cartesian products, grid generation, self-referential foreign keys, and self join patterns. |
| **`queries.sql`** | Practical scripts: reporting grids, size/color variant matrices, manager hierarchies, and peer matching. |

---
