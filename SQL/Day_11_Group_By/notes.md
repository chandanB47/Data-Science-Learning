```markdown
# Day 11: Grouping Data (`GROUP BY`)

## 🎯 Key Learning Objectives
* Understand how `GROUP BY` partitions tabular data into logical subsets.
* Apply aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) across grouped partitions.
* Construct multi-column groups to analyze sub-segments.
* Avoid the common "column must appear in the GROUP BY clause or be used in an aggregate function" SQL error.
* Group on scalar transformations and temporal fields.

---

## 1. What is `GROUP BY`?
The `GROUP BY` clause collapses multiple rows that share identical values in specified columns into summary rows.

Instead of computing one global aggregate metric across the whole table (like calculating the company-wide average salary), `GROUP BY` computes that metric **independently for each distinct group or category**.

---

## 2. Query Execution Lifecycle Revisited

Notice where `GROUP BY` fits into the engine's execution pipeline:

1. `FROM`: Identify source tables and joins.
2. `WHERE`: Filter individual base records (**runs BEFORE grouping**).
3. `GROUP BY`: Form distinct row groups.
4. `HAVING`: Filter grouped subsets (**runs AFTER grouping**).
5. `SELECT`: Evaluate projections, expressions, and aggregate functions.
6. `DISTINCT`: Eliminate identical output rows.
7. `ORDER BY`: Sort the grouped result set.
8. `LIMIT` / `OFFSET`: Restrict returned output rows.

---

## 3. The Golden Rule of `GROUP BY` (Single-Value Rule)

> ⚠️ **The Golden Rule**: Every non-aggregated column listed in your `SELECT` clause **MUST** be explicitly included in the `GROUP BY` clause.

### Why?
If a table has 10 employees in the "Engineering" department, each with a different name, the query engine cannot decide *which* individual name to display alongside a single summarized metric:

```sql
-- ❌ SYNTAX ERROR in standard SQL:
SELECT department_id, employee_name, AVG(salary)
FROM employees
GROUP BY department_id;

-- ✅ CORRECT: Only group-level attributes or aggregated fields
SELECT department_id, AVG(salary)
FROM employees
GROUP BY department_id;

-- ✅ CORRECT: Grouping by both columns to get combinations
SELECT department_id, employee_name, AVG(salary)
FROM employees
GROUP BY department_id, employee_name;

## 4. Multi-Column Grouping
Grouping by multiple columns produces a distinct output row for every unique combination of those values.

SQL
-- Analyzes payroll by region and department
SELECT 
    region,
    department,
    COUNT(*) AS headcount,
    ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY region, department
ORDER BY region, department;


## 5. Grouping by Expressions & Dates
You can group rows by the output of scalar functions (e.g., truncating dates to months or extracting parts of text):

SQL
-- Monthly order volume
SELECT 
    DATE_TRUNC('month', order_date)::DATE AS sales_month,
    COUNT(order_id) AS total_orders,
    SUM(order_total) AS total_revenue
FROM customer_orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY sales_month;
6. WHERE vs GROUP BY
WHERE evaluates records before groups are formed. It permanently discards non-matching rows from the grouping calculation.

Use WHERE to limit the dataset early to improve query performance.
