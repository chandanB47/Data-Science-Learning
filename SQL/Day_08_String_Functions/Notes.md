# Day 08: String & Scalar Functions

## 🎯 Key Learning Objectives
* Understand what makes a function "scalar" (operates row-by-row, returning one value per row).
* Master essential string transformation, cleaning, and extraction functions.
* Handle common dialect variations across PostgreSQL, MySQL, and SQL Server.
* Apply scalar mathematical functions for reporting precision.
* Clean dirty real-world text data (stripping whitespaces, standardizing email domains, extracting prefixes).

---

## 1. What are Scalar Functions?
A **Scalar Function** operates on single input values row-by-row and returns a single modified value for every row evaluated.

Unlike **Aggregate Functions** (which summarize multiple rows into one output, like `SUM` or `COUNT`), scalar functions preserve the original row count of your query.

---

## 2. Core String Functions Reference

| Function | Purpose | Example | Result |
| :--- | :--- | :--- | :--- |
| `CONCAT(a, b)` | Merges strings together | `CONCAT('Data', ' ', 'Science')` | `'Data Science'` |
| `a \|\| b` | ANSI standard concat operator | `'SQL' \|\| ' ' \|\| 'Pro'` | `'SQL Pro'` |
| `UPPER(str)` / `LOWER(str)` | Converts text to uppercase / lowercase | `UPPER('bengaluru')` | `'BENGALURU'` |
| `LENGTH(str)` | Returns number of characters | `LENGTH('Database')` | `8` |
| `TRIM(str)` | Strips leading and trailing spaces | `TRIM('  clean  ')` | `'clean'` |
| `SUBSTRING(str, pos, len)` | Extracts characters from a position | `SUBSTRING('DataScience', 5, 7)` | `'Science'` |
| `REPLACE(str, from, to)` | Substitutes target substring | `REPLACE('v1.0', '1', '2')` | `'v2.0'` |
| `POSITION(sub IN str)` / `INSTR()` | Returns index of substring | `POSITION('@' IN 'user@mail.com')`| `5` |
| `LPAD(str, len, pad)` | Left-pads string to target length | `LPAD('42', 5, '0')` | `'00042'` |

---

## 3. Practical Patterns & Dialect Differences

### A. Concatenation & Safe Merging
Using the standard `||` operator returns `NULL` if any operand is `NULL` in standard SQL. Use `CONCAT()` or `CONCAT_WS()` (Concat With Separator) to ignore `NULL` entries:

```sql
-- Returns 'Aarav Sharma' even if middle_name is NULL
SELECT CONCAT_WS(' ', first_name, middle_name, last_name) AS full_name
FROM users;
```

### B. Substring Extraction
SQL uses 1-based indexing (the first character is at index 1, not 0):

```SQL
-- Extract Domain from Email
SELECT 
    email,
    SUBSTRING(email FROM POSITION('@' IN email) + 1) AS domain_name
FROM users;
```

### C. Masking Sensitive Information

```SQL
-- Mask email: 'a***@domain.com'
SELECT 
    CONCAT(
        LEFT(email, 1),
        '***@',
        SUBSTRING(email FROM POSITION('@' IN email) + 1)
    ) AS masked_email
FROM users;
```
