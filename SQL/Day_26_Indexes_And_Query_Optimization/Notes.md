# Day 26: Indexes & Query Optimization

---

## 🎯 Key Learning Objectives
* Understand internal B-Tree storage and node traversal.
* Read and interpret `EXPLAIN` and `EXPLAIN ANALYZE` output.
* Design efficient composite indexes following the Leftmost Prefix Rule.
* Write SARGable (Search Argument Able) predicates to preserve index utility.
* Understand the write cost of indexes on DML throughput.

---

### 1. What is an Index?
An Index is an auxiliary data structure—most commonly a self-balancing B-Tree (Balanced Tree)—that the storage engine maintains to accelerate search operations.

* Full Table Scan (type: ALL): The engine reads every data page on disk sequentially ($O(N)$ time complexity).
* B-Tree Index Lookup (type: ref / range): The engine navigates root, branch, and leaf nodes in $O(\log N)$ steps to find exact record pointers.


### 2. Reading EXPLAIN in MySQL
Prepend EXPLAIN or EXPLAIN ANALYZE to your query to inspect the optimizer's execution plan.

Key Output Columns:
* type: The access method used. Ranked from fastest to slowest:
  1. const / system: Primary key or unique index lookup (returns 1 row directly).
  2. eq_ref: 1-to-1 match during an indexed join.
  3. ref: Non-unique index lookup (matches all rows with a given value).
  4. range: Index range scan (used for <, >, BETWEEN, IN).
  5. index: Full index scan (scans the entire index tree without reading table rows).
  6. ALL: Full Table Scan (reads every physical table row from disk).

* possible_keys: All candidate indexes considered by the optimizer.
* key: The specific index chosen.
* rows: Estimated number of rows the engine must inspect.
* Extra:
  1. Using index: Covering Index (all requested columns exist inside the index tree; no disk table lookups required).
  2. Using filesort: The engine must perform an additional sorting pass in memory or on temporary disk.
  3. Using temporary: An internal temporary table had to be created to resolve the query.


### 3. The Leftmost Prefix Rule
When an index covers multiple columns:

```SQL
CREATE INDEX idx_orders_cust_date ON orders(customer_id, order_date);
```

The optimizer can use the index only if query filters include the columns starting from the leftmost side:

* WHERE customer_id = 5 AND order_date >= '2026-01-01' ➔ ✅ Uses full composite index
* WHERE customer_id = 5 ➔ ✅ Uses composite index (leading column present)
* WHERE order_date >= '2026-01-01' ➔ ❌ Cannot use index (leading column missing; causes full table scan)


### 4. Writing SARGable Queries (Preserving Indexes)
A query is SARGable (Search Argument Able) when the database engine can traverse the index tree directly instead of scanning every row.

Anti-Pattern 1: Wrapping Indexed Columns in Functions

```SQL
-- ❌ Non-SARGable: Engine must evaluate YEAR() on every row (type: ALL)
SELECT * FROM orders WHERE YEAR(order_date) = 2026;

-- ✅ SARGable: Uses range scan on order_date index
SELECT * FROM orders 
WHERE order_date >= '2026-01-01' AND order_date < '2027-01-01';
```

Anti-Pattern 2: Leading Wildcards in LIKE

```SQL
-- ❌ Non-SARGable: Leading '%' forces a full scan
SELECT * FROM customers WHERE email LIKE '%@gmail.com';

-- ✅ SARGable: Trailing wildcard leverages index seeks
SELECT * FROM customers WHERE email LIKE 'aarav%';
```

### 5. The Write Cost of Over-Indexing
While indexes speed up SELECT statements:

* Every INSERT, UPDATE, and DELETE must update both the base table and every associated B-Tree index.
* Too many redundant indexes increase disk consumption and slow down batch ingestion pipelines.
