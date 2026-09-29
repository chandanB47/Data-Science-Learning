
# 📅 Day 26: Indexes & Query Optimization

---


## 📌 Overview

Day 26 covers relational index structures and query performance tuning in MySQL. 
You will learn how B-Tree indexes speed up lookups, how to read execution plans with `EXPLAIN` and `EXPLAIN ANALYZE`, 
how the Leftmost Prefix Rule governs composite keys, and how to write SARGable queries that prevent full table scans.


---
### 🎯 Key Learning Objectives
- [x] Understand how B-Tree indexes transform $O(N)$ full table scans into $O(\log N)$ seeks.
- [x] Create single-column, composite, and unique indexes using standard DDL.
- [x] Apply the Leftmost Prefix Rule on composite indexes.
- [x] Profile queries using EXPLAIN and EXPLAIN ANALYZE to inspect join types and row counts.
- [x] Identify access types: const, eq_ref, ref, range, index, and ALL.
- [x] Detect and fix index-invalidation anti-patterns (wrapping columns in functions, leading wildcards).
- [x] Leverage Covering Indexes (Using index) to satisfy queries directly from RAM without table lookups.
  
---

### 📂 Folder Structure
| File | Purpose | 
| :--- | :--- | 
| **`Notes.md`** | In-depth theory on B-Tree internals, scan classifications, composite index rules, and execution plans. | 
| **`queries.sql`** | Executable scripts profiling query plans with EXPLAIN, benchmarking composite keys, and optimizing slow lookups.|



