```markdown
# Day 17: Subqueries (Scalar, Multi-Row, and Nested)

## 🎯 Key Learning Objectives
* Understand subquery terminology: Outer Query (Main Query) vs. Inner Query (Subquery).
* Master the placement of subqueries in `WHERE`, `SELECT`, and `FROM` clauses.
* Classify subqueries by their output cardinality: Scalar, Multi-Row, and Multi-Column.
* Apply multi-row comparison operators: `IN`, `ANY`, and `ALL`.
* Identify the dangerous `NOT IN (NULL)` trap and how to safeguard against it.

---

## 1. What is a Subquery?
A **Subquery** (or nested query) is an SQL query enclosed in parentheses and embedded inside another SQL statement (`SELECT`, `INSERT`, `UPDATE`, or `DELETE`).

* **Execution Flow**: In non-correlated subqueries, the database engine evaluates the **inner query first**, computes its result, and feeds that result directly into the **outer query**.

```sql
-- The inner query runs first and returns a scalar value (e.g., 75000.00)
SELECT full_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
2. Classification by Output Shape
A. Scalar Subquery
Returns exactly one row and one column (a single cell value).

Can be used anywhere a literal constant or expression is valid (e.g., in SELECT, WHERE, HAVING).

If a scalar subquery returns more than 1 row or 1 column, the engine raises an error: subquery must return only one column / more than one row returned by a subquery.

SQL
-- Scalar subquery in SELECT: compares employee salary to company average
SELECT 
    full_name, 
    salary,
    (SELECT ROUND(AVG(salary), 2) FROM employees) AS company_avg_salary
FROM employees;
B. Multi-Row Subquery
Returns multiple rows but a single column (a list of values).

Cannot be used with standard equality operators (=, >, <).

Must be evaluated using list operators: IN, NOT IN, ANY, ALL.

ANY / SOME vs. ALL
> ANY (subquery): Greater than the minimum value returned by the subquery.

> ALL (subquery): Greater than the maximum value returned by the subquery.

< ALL (subquery): Less than the minimum value returned by the subquery.

SQL
-- Employees earning more than ANY engineer (earning more than the lowest-paid engineer)
SELECT full_name, salary
FROM employees
WHERE salary > ANY (
    SELECT salary FROM employees WHERE department = 'Engineering'
);

-- Employees earning more than ALL engineers (earning more than the highest-paid engineer)
SELECT full_name, salary
FROM employees
WHERE salary > ALL (
    SELECT salary FROM employees WHERE department = 'Engineering'
);
C. Derived Tables (Subquery in FROM)
When placed inside a FROM clause, a subquery acts as an inline temporary table.

Mandatory Rule: In almost all SQL engines (PostgreSQL, MySQL), derived tables must be given an alias.

SQL
-- Calculate the average of department totals
SELECT ROUND(AVG(dept_payroll), 2) AS avg_department_payroll
FROM (
    SELECT department, SUM(salary) AS dept_payroll
    FROM employees
    GROUP BY department
) AS dept_summaries;
3. The NOT IN and NULL Trap
If the result of a subquery passed to NOT IN contains even a single NULL value, the entire expression evaluates to UNKNOWN / FALSE, returning zero rows!

SQL
-- ⚠️ DANGER: If any manager_id is NULL, this query returns 0 rows!
SELECT full_name FROM employees 
WHERE emp_id NOT IN (SELECT manager_id FROM employees);

-- ✅ SAFE SOLUTION 1: Filter out NULL in subquery
SELECT full_name FROM employees 
WHERE emp_id NOT IN (SELECT manager_id FROM employees WHERE manager_id IS NOT NULL);

-- ✅ SAFE SOLUTION 2: Use NOT EXISTS (covered on Day 18)

4. Subqueries vs. Joins: When to Use Which?
Use Joins when you need attributes from both tables in the final output (SELECT),
or when processing large datasets where query optimizers create better execution plans with hash/merge joins.

Use Subqueries when calculating dynamic thresholds (e.g., higher than average, latest timestamp) or filtering without duplicating rows.
