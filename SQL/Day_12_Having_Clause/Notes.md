```markdown
# Day 12: Filtering Aggregations (`HAVING` vs `WHERE`)

## 🎯 Key Learning Objectives
* Understand why `WHERE` cannot filter on aggregate results like `COUNT(*)` or `AVG()`.
* Use `HAVING` to discard grouped rows that fail summary metric criteria.
* Trace the logical query execution pipeline to understand execution priority.
* Avoid the common performance anti-pattern of putting scalar filters into `HAVING`.

---

## 1. Why Do We Need `HAVING`?

The `WHERE` clause evaluates individual records **before** `GROUP BY` aggregates them. Consequently, standard SQL prevents the use of aggregate functions inside `WHERE`:

```sql
-- ❌ SYNTAX ERROR: Aggregate functions are not allowed in WHERE
SELECT department_id, AVG(salary)
FROM employees
WHERE AVG(salary) > 75000
GROUP BY department_id;

-- ✅ CORRECT: Use HAVING to filter groups after aggregation
SELECT department_id, AVG(salary)
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 75000;
