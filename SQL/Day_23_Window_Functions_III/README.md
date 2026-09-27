# 📅 Day 23: Window Functions III (Aggregate Frames & Moving Averages)

---

## 📌 Overview
Day 23 covers aggregate window functions and physical/logical framing clauses (`ROWS` and `RANGE`). 
You will learn how to calculate running totals, moving averages, rolling metrics, and frame bounds without collapsing row-level data.

---

### 🎯 Key Learning Objectives

- [x] Apply aggregate functions (SUM, AVG, COUNT, MIN, MAX) as window functions using OVER().
- [x] Calculate running totals and cumulative sums.
- [x] Master window frame specifications: ROWS BETWEEN ... AND ....
- [x] Understand frame boundary keywords: UNBOUNDED PRECEDING, CURRENT ROW, n PRECEDING, n FOLLOWING, and UNBOUNDED FOLLOWING.
- [x] Build rolling metrics (3-day moving averages, 7-day trailing revenue).
- [x] Contrast ROWS (physical row count) vs. RANGE (value-based peer groups).
  
 --- 

### 📂 Folder Structure

| File | Purpose |
| :--- | :--- |
| **`Notes.md`** | Comprehensive reference on frame bounds, rolling window definitions, and performance implications. |
| **`queries.sql`** | Practical scripts for cumulative spend, moving averages, year-to-date tracking, and moving boundaries. |
