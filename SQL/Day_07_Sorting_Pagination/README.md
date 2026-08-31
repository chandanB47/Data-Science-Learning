# 📅 Day 07: Sorting & Pagination

## 📌 Overview
Day 07 focuses on ordering query results deterministically, handling `NULL` positions during sorting, and implementing data pagination using `ORDER BY`, `LIMIT`, `OFFSET`, and the ANSI SQL-standard `FETCH FIRST` clause.

---

## 🎯 Key Learning Objectives
- [x] Sort query result sets in ascending (`ASC`) and descending (`DESC`) order using `ORDER BY`.
- [x] Implement multi-column composite sorting for hierarchical ordering.
- [x] Control the placement of `NULL` values during sorting with `NULLS FIRST` and `NULLS LAST`.
- [x] Restrict row counts and implement page-based data fetching with `LIMIT` and `OFFSET`.
- [x] Understand the ANSI SQL standard `OFFSET ... FETCH NEXT ... ROWS ONLY` syntax.
- [x] Identify performance pitfalls of offset-based pagination on large datasets.

---

## 📂 Folder Structure

| File | Purpose |
| :--- | :--- |
| **`Notes.md`** | Theoretical foundations of sorting, null ordering rules, pagination mechanics, and optimization trade-offs. |
| **`queries.sql`** | Hands-on SQL script covering single/multi-column sorting, pagination equations, and standard ANSI fetch patterns. |

---

