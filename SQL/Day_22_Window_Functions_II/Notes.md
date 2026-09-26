# Day 22: Window Functions II (Value Functions)
---
## 🎯 Key Learning Objectives
* Use positional value functions to reference other rows relative to the current row.
* Compute delta metrics, percentage growth, and period-over-period variance.
* Use `LEAD()` and `LAG()` with optional offset steps and default substitute parameters.
* Avoid the common frame pitfall when using `LAST_VALUE()`.
* Retrieve boundary elements with `FIRST_VALUE()`.

---
  
### 1. What are Value Functions?

Value Functions are specialized window functions that return values from specific rows relative to the current row position or relative to the window frame boundaries.

They replace clumsy, computationally heavy self-joins when analyzing sequential, chronological, or ordered data.



### 2. Core Positional Value Functions

| Function | Signature | Purpose |
| :--- | :---: | :---: |
| LAG() | LAG(col, [offset], [default]) | Pulls value from $N$ rows prior to current row |
| LEAD() | LEAD(col, [offset], [default]) | Pulls value from $N$ rows after current row | 
| FIRST_VALUE() | FIRST_VALUE(col) | Returns the value from the first row of the window frame | 
| LAST_VALUE() | LAST_VALUE(col) | Returns the value from the last row of the window frame | 



### 3. Syntax & Common Patterns

#### A.Period-over-Period Delta with LAG
```SQL
LAG(revenue, 1, 0.00) OVER (PARTITION BY region ORDER BY sale_month ASC)
```
* Arg 1 (revenue): Column to pull.
* Arg 2 (1): Offset distance (defaults to 1 row back).
* Arg 3 (0.00): Fallback value if no preceding row exists (replaces default NULL).

$$\text{Delta} = \text{Current Value} - \text{Lagged Value}$$

$$\text{MoM Growth \%} = \left(\frac{\text{Current Value} - \text{Lagged Value}}{\text{Lagged Value}}\right) \times 100$$

#### B. Future Lookahead with LEAD

SQL-- Calculate days between consecutive logins
```sql
SELECT 
    user_id,
    login_date,
    LEAD(login_date) OVER (PARTITION BY user_id ORDER BY login_date ASC) AS next_login_date
FROM logins;
```

#### C. The LAST_VALUE() Framing Trap
A very common bug in SQL queries happens when using LAST_VALUE() with ORDER BY:

```SQL-- ⚠️ UNEXPECTED RESULT: Returns the current row, NOT the last row of the partition!
LAST_VALUE(salary) OVER (PARTITION BY dept ORDER BY salary ASC)
```

#### Why does this happen?
* When ORDER BY is provided inside OVER(), standard SQL introduces a default window frame:RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW.
* Because the frame ends at the current row, LAST_VALUE() simply returns the current row's value.



#### The Fix:
Explicitly extend the frame to the end of the partition:

```SQLLAST_VALUE(salary) OVER (
    PARTITION BY dept 
    ORDER BY salary ASC
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
)
```
### 4. Best Practices
1.Always provide an explicit ORDER BY inside OVER() when using positional functions (LEAD, LAG, FIRST_VALUE), as relative row ordering is undefined without it.

2.Defend against division-by-zero errors during MoM percentage calculations using NULLIF(lag_value, 0).
