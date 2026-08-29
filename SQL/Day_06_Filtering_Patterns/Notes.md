# Day 06: Filtering & Pattern Matching

## 🎯 Key Learning Objectives
* Master the `WHERE` clause execution flow and predicate filtering.
* Understand Boolean operator precedence (`NOT` > `AND` > `OR`) and defensive grouping with parentheses.
* Apply range filters with `BETWEEN` and set inclusion filters with `IN`.
* Implement pattern search strategies with `LIKE` and wildcard tokens (`%`, `_`).
* Learn Three-Valued Logic (3VL: True, False, Unknown) and how `NULL` comparisons behave.

---

## 1. The `WHERE` Clause & Comparison Operators

The `WHERE` clause filters rows returned by the `FROM` clause *before* any grouping or projection takes place.

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| `=` | Equal to | `WHERE status = 'ACTIVE'` |
| `!=` or `<>` | Not equal to | `WHERE department_id <> 10` |
| `>`, `<` | Greater than / Less than | `WHERE salary > 50000` |
| `>=`, `<=` | Greater than or equal / Less than or equal | `WHERE age >= 21` |

---

## 2. Logical Operators & Precedence

* **`AND`**: True if all conditions are true.
* **`OR`**: True if any condition is true.
* **`NOT`**: Reverses the truth value of a condition.

### Operator Precedence Rule
SQL evaluates logical operators in this order:
1. `NOT`
2. `AND`
3. `OR`

> ⚠️ **Best Practice**: Always use explicit parentheses `(...)` to force evaluation order and make business logic unambiguous.

```sql
-- Without parentheses (evaluates AND first, likely giving incorrect results):
SELECT * FROM products WHERE category = 'Electronics' OR category = 'Furniture' AND price > 10000;

-- Correct logic with parentheses:
SELECT * FROM products WHERE (category = 'Electronics' OR category = 'Furniture') AND price > 10000;
```

### 3. Range & Set FilteringA. BETWEEN ... ANDTests whether a value falls within an inclusive range (equivalent to val >= low AND val <= high).

```SQL
SELECT product_name, price 
FROM products 
WHERE price BETWEEN 1000.00 AND 5000.00;
```
B. IN and NOT INChecks if a column value matches any value in a discrete list.

```SQL-- Set inclusion
SELECT full_name, city 
FROM customers 
WHERE city IN ('Bengaluru', 'Hyderabad', 'Pune');

-- Set exclusion
SELECT full_name, status 
FROM accounts 
WHERE status NOT IN ('SUSPENDED', 'CLOSED');
```

### 4. Handling NULL (Three-Valued Logic)In SQL, NULL represents missing or unknown data. 
A direct comparison like column = NULL or column != NULL results in UNKNOWN (which evaluates as false for filtering).
Always use IS NULL to find missing values.Always use IS NOT NULL to find populated values.

```SQL-- Correct
SELECT * FROM leads WHERE phone_number IS NULL;
SELECT * FROM leads WHERE phone_number IS NOT NULL;

-- WRONG (Will return 0 rows):
-- SELECT * FROM leads WHERE phone_number = NULL;
```
