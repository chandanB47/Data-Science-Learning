# Day 23: Window Functions III (Aggregate Frames & Moving Averages)

## 🎯 Key Learning Objectives
* Use standard aggregate functions within analytical window clauses.
* Understand running totals and cumulative metrics.
* Define precise window frames using `ROWS BETWEEN`.
* Calculate rolling averages (e.g., 3-day or 7-day smoothing).
* Differentiate between physical frames (`ROWS`) and logical frames (`RANGE`).

---

### 1. Aggregate Window Functions

Standard aggregate functions (SUM, AVG, MIN, MAX, COUNT) can be turned into window functions by adding an OVER() clause:

* Without ORDER BY: Evaluates across the entire partition simultaneously.

* With ORDER BY: Evaluates cumulatively from the start of the partition up to the current row.

```SQL
-- Global/Partition Total alongside individual rows
SELECT 
    emp_name, 
    salary,
    SUM(salary) OVER(PARTITION BY department) AS total_dept_salary
FROM employees;
```

### 2. Frame Specification: ROWS BETWEEN

A frame defines the specific subset of rows within the partition that the function evaluates for each individual row.

```Plaintext
               [ UNBOUNDED PRECEDING ]   <- Very first row of partition
                         :
                 [ 2 PRECEDING ]         <- 2 rows before current
                 [ 1 PRECEDING ]         <- 1 row before current
===>             [ CURRENT ROW ]         <=== The row being evaluated
                 [ 1 FOLLOWING ]         <- 1 row after current
                 [ 2 FOLLOWING ]         <- 2 rows after current
                         :
               [ UNBOUNDED FOLLOWING ]   <- Very last row of partition
```

Syntax

```SQL
AGG_FUNCTION(col) OVER (
    PARTITION BY partition_col
    ORDER BY order_col
    ROWS BETWEEN  AND 
)
```


### 3. Common Window Frames

#### A. Cumulative Running Total

```SQL
-- Evaluates from the start of the partition up to the current row
SUM(revenue) OVER (
    PARTITION BY region 
    ORDER BY sale_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

#### B. Rolling / Moving Average (Trailing 3 Periods)

A 3-period moving average incorporates the current row and the two preceding rows:

```SQL
AVG(daily_sales) OVER (
    ORDER BY sale_date
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
)
```

#### C. Centered Moving Average

Evaluates one row prior, the current row, and one row after:

```SQL
AVG(daily_sales) OVER (
    ORDER BY sale_date
    ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
)
```


### 4. ROWS vs. RANGE

* ROWS: Evaluates physical row offsets regardless of column values or duplicates.

* RANGE: Evaluates logical value ranges based on the value in the ORDER BY column. If two rows share identical values (ties), RANGE treats them as peers and groups them into the same frame.

    💡 Best Practice: In analytical queries, prefer explicit ROWS BETWEEN ... to avoid unexpected calculation spikes on duplicate values.
