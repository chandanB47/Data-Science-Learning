# Day 09: Date & Time Operations

## 🎯 Key Learning Objectives
* Distinguish between dates, timestamps, and timezone-aware timestamps.
* Extract components (year, quarter, month, day, hour, day of week) using ANSI SQL standard `EXTRACT()`.
* Calculate elapsed duration and aging between two timestamps.
* Truncate temporal values to specific granularities using `DATE_TRUNC()`.
* Navigate cross-engine differences between PostgreSQL, MySQL, and SQL Server.

---

## 1. Temporal Data Types

| Data Type | Storage Contents | Example |
| :--- | :--- | :--- |
| `DATE` | Year, month, and day only | `2026-09-07` |
| `TIME` | Hour, minute, second, and fractional seconds | `14:30:00` |
| `TIMESTAMP` | Date and time (without timezone) | `2026-09-07 14:30:00` |
| `TIMESTAMPTZ` | Timestamp with timezone offset (best practice for global apps) | `2026-09-07 14:30:00+05:30` |
| `INTERVAL` | A span of time (days, hours, minutes) | `'30 days'`, `'2 months'` |

---

## 2. Core Temporal Functions

### A. Current Timestamps
* `CURRENT_DATE`: Returns the current date according to the session.
* `CURRENT_TIMESTAMP` / `NOW()`: Returns current date and time with timezone.

### B. Extracting Date Parts (`EXTRACT`)
The ANSI-standard way to pull specific date parts:

```sql
SELECT 
    EXTRACT(YEAR FROM order_date) AS order_year,
    EXTRACT(QUARTER FROM order_date) AS order_quarter,
    EXTRACT(MONTH FROM order_date) AS order_month,
    EXTRACT(DAY FROM order_date) AS order_day,
    EXTRACT(DOW FROM order_date) AS day_of_week -- 0 = Sunday in Postgres
FROM orders;
```

### 3. Date Arithmetic & Intervals   PostgreSQL / ANSI Standard:

```SQL
-- Adding and subtracting intervals
SELECT CURRENT_DATE + INTERVAL '7 days' AS next_week;
SELECT CURRENT_DATE + INTERVAL '3 months' AS next_quarter;
SELECT CURRENT_DATE - INTERVAL '1 year' AS last_year;

-- Difference between timestamps (returns INTERVAL or days)
SELECT (delivery_date - order_date) AS delivery_days FROM orders;
```

### 4. Analytical Grouping: DATE_TRUNC()
DATE_TRUNC() rounds a timestamp down to the beginning of a specified unit (day, week, month, quarter, year). 
It is the backbone of time-series aggregation.

```sql
-- Groups all timestamps in September 2026 to '2026-09-01 00:00:00'
SELECT 
    DATE_TRUNC('month', order_date) AS sales_month,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY sales_month;
```
