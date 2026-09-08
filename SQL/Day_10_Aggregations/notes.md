# Day 10: Aggregate Functions & NULL Handling

## 🎯 Key Learning Objectives
* Understand what makes a function an aggregate function (many-to-one reduction).
* Master the five core aggregate operations: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
* Analyze how `NULL` values affect aggregations and learn how to prevent skew in `AVG()`.
* Use `DISTINCT` inside aggregate calls to summarize unique observations.
* Write conditional aggregations using `COUNT(CASE WHEN ...)` and `SUM(CASE WHEN ...)`.

---

## 1. What are Aggregate Functions?
An **Aggregate Function** performs a calculation on a set of values across multiple rows and returns a single summarized value.

Unlike scalar functions (which evaluate row-by-row and maintain the original row count), aggregate functions condense entire row sets into scalar metrics.

---

## 2. The Big 5 Aggregate Functions

| Function | Purpose | Input Types Supported | Ignores `NULL`? |
| :--- | :--- | :--- | :---: |
| **`COUNT(expr)`** | Returns the count of non-null evaluated values | Any data type | ✅ Yes |
| **`SUM(col)`** | Returns the arithmetic sum | Numeric only | ✅ Yes |
| **`AVG(col)`** | Returns the arithmetic mean | Numeric only | ✅ Yes |
| **`MIN(col)`** | Returns the minimum value | Numeric, Date, String | ✅ Yes |
| **`MAX(col)`** | Returns the maximum value | Numeric, Date, String | ✅ Yes |

---

## 3. The Nuances of `COUNT()`

* **`COUNT(*)`**: Counts every row returned by the query, including rows that contain entirely `NULL` columns.
* **`COUNT(column_name)`**: Counts only rows where `column_name` is **NOT NULL**.
* **`COUNT(DISTINCT column_name)`**: Evaluates unique, non-null values only.

```sql
-- Total rows in table
SELECT COUNT(*) FROM employees;

-- Total employees who receive a commission (skips NULLs)
SELECT COUNT(commission_pct) FROM employees;

-- Total distinct departments represented
SELECT COUNT(DISTINCT department_id) FROM employees;
```


### 4. How NULL Values Impact Calculations
All aggregate functions (except COUNT(*)) ignore NULLs automatically.
The AVG() Caveat
Because AVG(col) divides the sum of non-null values by the count of non-null values, it can distort metrics if missing values should semantically count as zero.
$$\text{Standard } AVG = \frac{\sum \text{non-null values}}{\text{Count of non-null values}}$$

```SQL
-- Scenario: 4 employees with bonuses: 1000, 2000, NULL, NULL
-- Standard AVG ignores NULLs: (1000 + 2000) / 2 = 1500
SELECT AVG(bonus) FROM employees;

-- Normalized AVG treating NULL as 0: (1000 + 2000 + 0 + 0) / 4 = 750
SELECT AVG(COALESCE(bonus, 0)) FROM employees;
```

### 5. Conditional Aggregation Pattern
 By embedding CASE WHEN expressions inside aggregate functions, you can calculate multiple filtered metrics in a single pass without writing multiple queries or subqueries:
 
 ```SQL
SELECT 
    COUNT(*) AS total_employees,
    COUNT(CASE WHEN department = 'Engineering' THEN 1 END) AS eng_headcount,
    SUM(CASE WHEN department = 'Engineering' THEN salary ELSE 0 END) AS eng_payroll,
    COUNT(CASE WHEN salary >= 100000 THEN 1 END) AS high_earners_count
FROM employees;
```
