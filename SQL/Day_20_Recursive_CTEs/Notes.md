
```markdown
# Day 20: Recursive Common Table Expressions (Recursive CTEs)

## 🎯 Key Learning Objectives
* Understand how recursive execution operates iteratively in relational engines.
* Identify the two required components: Anchor Member (base case) and Recursive Member (inductive step).
* Construct calendar and sequence generators dynamically.
* Traverse multi-level corporate hierarchies to determine seniority depth and management paths.
* Identify and avoid cyclic references and infinite recursion loops.

---

## 1. What is a Recursive CTE?

A **Recursive CTE** is a Common Table Expression that references itself. It executes iteratively to handle hierarchical, tree-structured, or sequential data of arbitrary depth.

In standard SQL (PostgreSQL, MySQL 8.0+, SQLite), recursive CTEs require the `WITH RECURSIVE` syntax (in SQL Server and Oracle, the `RECURSIVE` keyword is omitted):

```sql
WITH RECURSIVE cte_name AS (
    -- 1. ANCHOR MEMBER (Base Query)
    SELECT ...
    
    UNION ALL
    
    -- 2. RECURSIVE MEMBER (References cte_name, runs until it returns 0 rows)
    SELECT ...
    FROM cte_name
    WHERE [Termination Condition]
)
SELECT * FROM cte_name;
2. Execution Lifecycle: How the Engine Evaluates ItStep 1 (Anchor Evaluation):
The engine executes the Anchor Member query once to form the initial working table $R_0$.
Step 2 (Recursive Step): The engine executes the Recursive Member using $R_0$ as the input reference, producing intermediate result set $R_1$.
Step 3 (Iteration): Step 2 repeats: $R_1$ produces $R_2$, $R_2$ produces $R_3$, and so on.
Step 4 (Termination): When the recursive query yields an empty set (0 rows returned), recursion terminates.
Step 5 (Final Result): The engine takes the UNION ALL of all intermediate sets ($R_0 \cup R_1 \cup R_2 \dots$).

3. Classic PatternsPattern A: Sequence & Calendar GenerationCreate synthetic lists of numbers or contiguous date ranges without needing a physical table:

SQL-- Generate integers 1 to 10
WITH RECURSIVE numbers_series AS (
    SELECT 1 AS num             -- Anchor
    UNION ALL
    SELECT num + 1              -- Recursive step
    FROM numbers_series
    WHERE num < 10              -- Termination condition
)
SELECT * FROM numbers_series;
Pattern B: Organizational Hierarchy & Depth TrackingTraverse direct-report trees from top executives down to individual contributors,
computing the exact reporting level:SQLWITH RECURSIVE org_chart AS (
    -- Anchor: Root CEO / Director (manager_id is NULL)
    SELECT 
        emp_id, 
        full_name, 
        manager_id, 
        1 AS hierarchy_level,
        CAST(full_name AS VARCHAR(255)) AS management_path
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive Step: Find all direct reports of the previous level
    SELECT 
        e.emp_id, 
        e.full_name, 
        e.manager_id, 
        o.hierarchy_level + 1,
        CAST(CONCAT(o.management_path, ' -> ', e.full_name) AS VARCHAR(255))
    FROM employees e
    INNER JOIN org_chart o ON e.manager_id = o.emp_id
)
SELECT * FROM org_chart ORDER BY hierarchy_level, emp_id;

4. Guarding Against Runaway Queries & Infinite LoopsIf your data contains circular references
 (e.g., Employee A manages Employee B, and Employee B manages Employee A) or a missing termination filter,
the query loops indefinitely until it exhausts memory or hits the engine cap.Engine Safeguards:
PostgreSQL: Defaults to statement timeout; recursion stops when memory is exhausted or cancelled.
MySQL: Enforces cte_max_recursion_depth (default is 1000 iterations):SQLSET SESSION cte_max_recursion_depth = 50;
