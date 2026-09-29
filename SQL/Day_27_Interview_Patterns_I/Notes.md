# Day 27: Interview Patterns I (`N`th Highest Salary & Duplicates)

## 🎯 Key Learning Objectives

* Solve the `N`th highest salary problem across multiple SQL variations.
* Understand why `DENSE_RANK()` is preferred over `RANK()` and `ROW_NUMBER()` for salary tiers.
* Master group-wise deduplication patterns using `GROUP BY ... HAVING` and `ROW_NUMBER()`.
* Find sequences of `K` consecutive rows using self-joins and lead/lag functions.

---

### 1. Problem Pattern: `N`th Highest Salary

#### Approach 1: Window Function (`DENSE_RANK`) — Preferred

`DENSE_RANK()` ensures that duplicate salaries share the same rank without leaving gaps in the numerical sequence.

```sql
WITH ranked_salaries AS (
    SELECT 
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT MAX(salary) AS nth_highest_salary
FROM ranked_salaries
WHERE rnk = 2; -- Change to N
```

* Why MAX(salary)? If the $N^{\text{th}}$ rank does not exist (e.g., table has only 1 row), MAX() returns NULL rather than an empty set, satisfying common platform evaluation rules (LeetCode 176/177).

 
#### Approach 2: LIMIT and OFFSET (Single-dialects / Ad-hoc)

```SQL

SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1; -- For 2nd highest: OFFSET = N - 1
```

Caveat: Returns an empty set (0 rows) instead of NULL if no such row exists. Wrap in a subquery or IFNULL() to guarantee a NULL fallback.

#### Approach 3: Correlated Subquery (Engine-Agnostic / No Window Functions)Counts how many distinct salaries are strictly greater than the current candidate salary:

```SQL

SELECT DISTINCT e1.salary
FROM employees e1
WHERE (N - 1) = (
    SELECT COUNT(DISTINCT e2.salary)
    FROM employees e2
    WHERE e2.salary > e1.salary
);
```

### 2. Problem Pattern: Department-Wise Top $N$ EarnersFind the top 3 highest unique earners within each department:

```SQL
WITH ranked_dept_salaries AS (
    SELECT 
        department_id,
        emp_name,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY department_id 
            ORDER BY salary DESC
        ) AS dept_rnk
    FROM employees
)
SELECT department_id, emp_name, salary
FROM ranked_dept_salaries
WHERE dept_rnk <= 3
ORDER BY department_id, dept_rnk;
```

### 3. Problem Pattern: Duplicate Identification & Removal

Step 1: Identify Duplicates

```SQL

SELECT email, COUNT(*) AS occurrences
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

Step 2: Delete Duplicates While Retaining Smallest id

```SQL
-- Pattern: Delete rows where an identical record with a smaller ID exists
DELETE u1 
FROM users u1
INNER JOIN users u2 
    ON u1.email = u2.email 
   AND u1.id > u2.id;

```

### 4. Problem Pattern: Consecutive Sequences (3 Consecutive Days / Numbers)

Find numbers appearing at least three times consecutively in log records:

```SQL
WITH lagged_logs AS (
    SELECT 
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev_num,
        LAG(num, 2) OVER (ORDER BY id) AS prev_prev_num
    FROM logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM lagged_logs
WHERE num = prev_num AND num = prev_prev_num;
```
