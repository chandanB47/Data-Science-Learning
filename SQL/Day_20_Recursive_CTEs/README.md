# 📅 Day 20: Recursive CTEs (Hierarchical Queries & Sequences)

## 📌 Overview
Day 20 covers Recursive Common Table Expressions (Recursive CTEs). You will learn how to write self-referential queries to traverse hierarchical structures (organizational trees, bill-of-materials), generate numeric/date sequences on the fly, and prevent infinite recursion loops.

---

## 🎯 Key Learning Objectives
- [x] Understand the structure of a recursive query: **Anchor Member**, **`UNION ALL`**, and **Recursive Member**.
- [x] Master the termination condition to prevent runaway queries and stack overflow crashes.
- [x] Generate custom number and date series without physical calendar tables.
- [x] Traverse top-down and bottom-up organizational reporting lines.
- [x] Calculate hierarchy depth levels and track breadcrumb audit paths (`Aarav -> Neha -> Rohan`).
- [x] Configure recursion depth safety limits using `MAXRECURSION` or engine session parameters.

---

## 📂 Folder Structure

| File | Purpose |
| :--- | :--- |
| **`Notes.md`** | In-depth theory on recursive query mechanics, anchor vs recursive execution phases, path tracking, and cycle prevention. |
| **`queries.sql`** | Hands-on SQL script covering synthetic date/number sequence generation, org chart level tracking, and breadcrumb path reconstruction. |

---
