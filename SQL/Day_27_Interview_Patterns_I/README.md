# 📅 Day 27: Interview Patterns I (\(N^{\text{th}}\) Highest Salary & Duplicate Detection)

--- 

## 📌 Overview
Day 27 focuses on classic, high-frequency SQL interview problems. 
You will master standard patterns for finding the \(N^{\text{th}}\) highest salary (both globally and department-wise), detecting and deduplicating records safely, 
identifying consecutive log entries, and handling edge cases like ties and missing values.

--- 

### 🎯 Key Learning Objectives

- [x] Find the $N^{\text{th}}$ highest salary globally using LIMIT / OFFSET, correlated subqueries, and DENSE_RANK().
- [x] Find the top $N$ earners per department using CTEs and window ranking.
- [x] Identify duplicate records across single and multi-column combinations.
- [x] Delete duplicate rows safely while keeping the original record (deterministic deduplication).
- [x] Detect consecutive values (e.g., three consecutive active days or matching numbers).
- [x] Gracefully return NULL when an $N^{\text{th}}$ rank does not exist.

---

### 📂 Folder Structure
| File | Purpose | 
| :--- | :--- | 
| **`Notes.md`** | In-depth theory, interview trade-offs, edge-case checklists, and cross-dialect variations. |
| **`queries.sql`** | Executable scripts solving real interview test cases on employee payroll and audit logs. |
