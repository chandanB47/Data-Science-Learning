# Day 18: Correlated Subqueries (`EXISTS` & `NOT EXISTS`)

## 🎯 Key Learning Objectives
* Differentiate between non-correlated subqueries (evaluated once globally) and correlated subqueries (evaluated once per candidate outer row).
* Reference outer table columns inside inner query filters (correlation condition).
* Implement `EXISTS` and `NOT EXISTS` for boolean set presence checks.
* Contrast the performance and behavior of `IN` vs. `EXISTS` and `NOT IN` vs. `NOT EXISTS`.
* Learn why `NOT EXISTS` is immune to the `NOT IN (NULL)` trap.

---

## 1. What is a Correlated Subquery?

A **Correlated Subquery** is an inner query that references one or more columns from the **outer query's candidate row**.

Because it depends on values from the outer query, it cannot be run independently as a standalone query. The database engine logically executes the subquery **repeatedly, once for each row processed by the outer query**.

```sql
-- The inner query references 'e.department_id' from the outer query row:
SELECT e.full_name, e.department_id, e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(sub.salary)
    FROM employees sub
    WHERE sub.department_id = e.department_id -- Correlation condition
);
