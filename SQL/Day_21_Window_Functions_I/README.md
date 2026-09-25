# 📅 Day 21: Window Functions I (Ranking & Numbering)

---
## 📌 Overview
Day 21 introduces analytical window functions in SQL.
Unlike standard `GROUP BY` operations that collapse individual records, window functions evaluate subsets while preserving the original row granularity. 
This module focuses on the `OVER()` clause, data partitioning, and ranking functions.

---

### 🎯 Key Learning Objectives
----
- [x] Distinguish between standard aggregations (GROUP BY) and window functions (OVER()).
- [x] Understand the syntax and mechanics of the OVER(PARTITION BY ... ORDER BY ...) clause.
- [x] Compare ROW_NUMBER(), RANK(), and DENSE_RANK() side-by-side.
- [x] Split distributions into equal percentiles or buckets using NTILE(n).
- [x] Solve the "Top-N per group" problem cleanly by pairing window functions with CTEs.
- [x] Deduplicate data based on deterministic row assignment rules.

-----
#### 📂 Folder Structure

 | File | Purpose |
 | :--- | :--- |
 | **`Notes.md`** | Comprehensive theory on windowing concepts, partition mechanics, tie-breaking behavior, and ranking logic.| 
 | **`queries.sql`** | Hands-on script covering top-earner extraction per department, product tiering, tie handling, and NTILE quartiles. |

 ---
