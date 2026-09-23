# Day 19: Common Table Expressions (CTEs & `WITH` Clause)

## 🎯 Key Learning Objectives
* Master the `WITH` keyword to define named, temporary result sets.
* Understand the query execution lifecycle and temporary scope of CTEs.
* Chain multiple CTE definitions in a logical, top-down narrative.
* Compare CTEs with subqueries, views, and temporary tables.
* Understand optimizer materialization behavior in modern RDBMS (PostgreSQL, MySQL 8.0+).

---

## 1. What is a Common Table Expression (CTE)?

A **Common Table Expression (CTE)** is a named, temporary result set defined at the beginning of an SQL query using the `WITH` clause.

It exists **only for the duration of the execution** of the single statement that defines it (`SELECT`, `INSERT`, `UPDATE`, or `DELETE`).

```sql
WITH regional_sales AS (
    SELECT region, SUM(amount) AS total_revenue
    FROM orders
    GROUP BY region
)
SELECT region, total_revenue
FROM regional_sales
WHERE total_revenue > 100000;
```

### 2. Why Use CTEs Instead of Subqueries?
Top-Down Readability: Subqueries are written inside-out; you must read from the innermost nesting outward. CTEs read top-to-bottom like modular code functions.

Reusability within Single Query: A CTE can be referenced multiple times within the same downstream query without repeating the subquery code.

Easier Debugging: You can test each CTE independently before combining them into the final SELECT.

Plaintext
Nested Subquery (Hard to read):
```sql
SELECT * FROM (
    SELECT * FROM (
        SELECT * FROM base_table WHERE ...
    ) AS step1 WHERE ...
) AS step2;

CTE (Clean & Linear):
WITH step1 AS (
    SELECT * FROM base_table WHERE ...
),
step2 AS (
    SELECT * FROM step1 WHERE ...
)
SELECT * FROM step2;
```


### 3. Chaining Multiple CTEs
You can declare multiple CTEs under a single WITH keyword by separating each CTE block with a comma:

```SQL
WITH customer_spending AS (
    SELECT customer_id, SUM(order_amount) AS total_spend
    FROM customer_orders
    GROUP BY customer_id
),
spending_thresholds AS (
    SELECT AVG(total_spend) AS avg_customer_spend
    FROM customer_spending
)
SELECT 
    cs.customer_id, 
    cs.total_spend,
    st.avg_customer_spend
FROM customer_spending cs
CROSS JOIN spending_thresholds st
WHERE cs.total_spend > st.avg_customer_spend;
