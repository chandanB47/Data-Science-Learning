# 📅 Day 24: Views & Materialized Views

---

## 📌 Overview
Day 24 focuses on database abstraction using standard Views and Materialized Views. 
You will learn how to encapsulate complex queries, implement column-level data security masking, 
manage updatable views with check options, and cache compute-heavy analytical aggregations for fast retrieval.

---

### 🎯 Key Learning Objectives

[x] Create, modify, and drop standard views using CREATE OR REPLACE VIEW.
[x] Simplify complex multi-table joins and window functions behind clean virtual abstractions.
[x] Implement row- and column-level security masks for sensitive data (PII, compensation).
[x] Understand updatable view criteria and the WITH CHECK OPTION clause.
[x] Contrast Standard Views (virtual/on-the-fly) vs. Materialized Views (persisted cache).
[x] Implement materialized refresh patterns in PostgreSQL and emulate them in MySQL.

---
#### 📂 Folder Structure

| File | Purpose | 
| :--- | :--- |
| **`Notes.md`** | Theoretical foundations, storage lifecycle, security abstraction, updatable rules, and refresh mechanisms. |
| **`queries.sql`** | Executable scripts featuring analytical views, security masks, WITH CHECK OPTION, and view performance patterns. |
