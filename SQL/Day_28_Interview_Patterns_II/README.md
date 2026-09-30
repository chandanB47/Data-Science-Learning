# 📅 Day 28: Interview Patterns II (Retention Cohorts, Rolling Averages, YoY Growth)



## 📌 Overview
Day 28 tackles advanced, metrics-driven SQL interview questions common in analytics and data science rounds.
This day focuses on user retention cohort matrices, multi-period trailing moving averages, and period-over-period financial growth (YoY and MoM) with defensive divide-by-zero handling.


---

### 🎯 Key Learning Objectives

- [x] Construct month-by-month User Retention Cohorts using CTEs and date truncation.
- [x] Calculate dynamic Rolling/Moving Averages using frame specifications (ROWS BETWEEN n PRECEDING AND CURRENT ROW).
- [x] Compute Year-over-Year (YoY) and Month-over-Month (MoM) growth rates using LAG().
- [x] Protect percentage growth calculations against division-by-zero errors using NULLIF().
- [x] Solve the "Gaps and Islands" problem to detect consecutive activity streaks.
- [x] Build cumulative customer acquisition curves using running counts.


---

### 📂 Folder Structure

| File | Purpose | 
| :--- | :--- | 
| **`Notes.md`** | In-depth theory on cohort analysis architecture, moving average frame windows, YoY mathematical foundations, and the Gaps & Islands pattern.| 
| **`queries.sql`** | Executable scripts containing practical test cases for monthly cohort retention, 7-day smoothed revenue, YoY growth, and user login streaks. |
