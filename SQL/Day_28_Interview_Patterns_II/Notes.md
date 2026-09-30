# Day 28: Interview Patterns II (Cohorts, Rolling Metrics & YoY)

## 🎯 Key Learning Objectives
* Structure end-to-end customer cohort retention matrices.
* Calculate smoothed trends with moving averages to remove day-of-week seasonality.
* Formulate Year-over-Year (YoY) and Month-over-Month (MoM) growth metrics cleanly.
* Master the classic Gaps & Islands interview pattern using row number differences.

--- 

### 1. Retention Cohort Analysis   

Cohort Analysis groups users based on a shared initial event (such as their signup month) and tracks their activity over subsequent calendar periods.

#### Standard 3-Step Pipeline:

* Find Cohort Month: Extract each user's earliest activity timestamp (MIN(order_date)).
* Calculate Activity Offset: Find the difference in months between the activity date and the cohort date:
 
$$\text{Month Index} = (\text{Year}_{\text{activity}} - \text{Year}_{\text{cohort}}) \times 12 + (\text{Month}_{\text{activity}} - \text{Month}_{\text{cohort}})$$


  1. Pivot / Aggregate: Count distinct users active in each month index relative to the initial cohort size ($M_0$).

 
 
 ### 2. Trailing Moving Averages    
 
 Raw daily transaction metrics are often volatile due to weekend patterns. A 7-Day Trailing Moving Average smooths this volatility:
 
 ```SQL

AVG(daily_revenue) OVER (
    ORDER BY transaction_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
)
```

⚠️ Framing Detail: A 7-day window including today spans the current row plus the 6 preceding rows ($1 + 6 = 7$). 



### 3. Period-over-Period Growth (YoY / MoM)  

To compute growth between periods:

$$\text{Growth \%} = \left(\frac{\text{Metric}_{\text{current}} - \text{Metric}_{\text{prior}}}{\text{Metric}_{\text{prior}}}\right) \times 100$$

#### Defensive Division Rule:

Always wrap the denominator in NULLIF(prior_val, 0):

```SQL

ROUND(
    (current_rev - LAG(current_rev) OVER (ORDER BY period_date)) 
    / NULLIF(LAG(current_rev) OVER (ORDER BY period_date), 0) * 100.0, 
    2
) AS growth_pct
```

If LAG() returns 0 or NULL, the calculation evaluates safely to NULL rather than failing with Division by zero.


### 4. The Gaps and Islands Pattern

A classic interview test for data science and analytics roles. Used to identify consecutive sequences (e.g., users with 5+ consecutive active days):

* When you subtract a continuous sequence ROW_NUMBER() OVER (ORDER BY event_date) from the actual event_date, consecutive days yield the exact same anchor date (the "Island").
* When a gap occurs in the activity dates, the difference changes, starting a new group key!


```SQL

-- The difference produces a constant identifier for consecutive days
event_date - (ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_date) * INTERVAL '1 day')
```
