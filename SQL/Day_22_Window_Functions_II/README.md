# 📅 Day 22: Window Functions II (Value Functions: LEAD, LAG, FIRST_VALUE, LAST_VALUE)
---
## 📌 Overview

Day 22 covers SQL value window functions. 
You will learn how to access data from preceding or succeeding rows without performing expensive self-joins, 
compute period-over-period differences, detect trend variations, and locate boundary records within window partitions.

---
### 🎯 Key Learning Objectives

- [x] Access preceding rows using LAG() to compute Month-over-Month (MoM) and Year-over-Year (YoY) growth.
- [x] Access following rows using LEAD() to forecast gaps, identify churn risk, and calculate lead times.
- [x] Configure fallback default values inside LEAD() and LAG() to prevent null arithmetic errors.
- [x] Extract partition boundaries with FIRST_VALUE() and LAST_VALUE().
- [x] Understand default frame specifications (RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) and how they affect LAST_VALUE().
- [x] Calculate differences between consecutive events to measure elapsed times.

---

📂 Folder Structure

| File | Purpose | 
| --- | --- | 
| **`Notes.md`** |Comprehensive reference for positional value functions, offset syntax, null replacements, and framing defaults.
| **`queries.sql`** | Executable script containing time-series revenue trends, MoM variance calculations, and user session intervals.
