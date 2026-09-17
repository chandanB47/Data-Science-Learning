# 🛒 Milestone Project 01: Retail Store Operations & Analytics

## 📌 Project Overview
A comprehensive, end-to-end relational database project synthesizing concepts mastered in Days 01 through 15:
* Normalized schema design with multi-level constraints (PK, FK, CHECK, UNIQUE, NOT NULL, DEFAULT).
* Batch data insertion and transactional integrity.
* Data cleansing, string manipulation, and date arithmetic.
* Business-level aggregations (`GROUP BY`, `HAVING`).
* Relational joins (`INNER JOIN`, `LEFT JOIN`, anti-joins, and `SELF JOIN`).

---

## 🗄️ Relational Data Model

1. **`stores`**: Brick-and-mortar retail branches.
2. **`employees`**: Staff members with hierarchical reporting (`manager_id` self-referencing FK).
3. **`categories` & `products`**: Catalog items with strict pricing rules.
4. **`customers`**: Customer profiles with normalized email and phone records.
5. **`orders` & `order_items`**: Transactional sales ledger with line-item totals.

---

## 🎯 Key Analytical Problems Solved

1. **HR Hierarchy & Reporting**: Mapping employee reporting lines and identifying top managers using `SELF JOIN`.
2. **Catalog Variant Coverage**: Generating potential product-store matrices using `CROSS JOIN`.
3. **Customer Retention & Inactive Accounts**: Detecting zero-order customers via Anti-Joins.
4. **Sales Performance & SLA Fulfillment**: Calculating delivery turnaround times, monthly revenue cohorts, and top revenue drivers.
5. **High-Value Branch Identification**: Filtering regional store performance using combined `WHERE` and `HAVING` filters.

---

## 🚀 Execution Steps

Run the scripts sequentially in your SQL client:
1. `schema.sql` - Builds the tables and constraints.
2. `seed_data.sql` - Populates sample operational records.
3. `analytical_queries.sql` - Runs real-world business intelligence queries.
