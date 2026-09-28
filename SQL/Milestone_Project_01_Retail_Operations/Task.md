# 🛒 SQL Milestone Project 01 — Retail Store Operations & Analytics
## Task Sheet — Basics to Advanced

**Database:** MySQL  
**Project:** Retail Store Operations & Analytics  
**Level:** Beginner → Intermediate → Advanced  
**Status:**  Completed

---

# 🎯 Task Objective

Use the Retail Store Operations & Analytics database to strengthen and demonstrate:

- SQL fundamentals
- Data filtering and sorting
- String manipulation
- Date handling
- Aggregate functions
- `GROUP BY`
- `HAVING`
- `INNER JOIN`
- `LEFT JOIN`
- Anti-Join patterns
- `SELF JOIN`
- `CROSS JOIN`
- `CASE`
- `COALESCE`
- Business-oriented analytical queries

> **Rule:** Try each task yourself before checking a solution.

---

# 🗂️ Project Tables

```text
stores
employees
categories
products
customers
orders
order_items
```

Main relationships:

```text
stores
  ├── employees
  └── orders

employees
  └── manager_id → employees.emp_id

categories
  └── products

customers
  └── orders

orders
  └── order_items

products
  └── order_items
```

---

# 🟢 LEVEL 1 — BASIC SQL TASKS

## Task 01 — View Customers

Display all columns from the `customers` table.

**Concepts:** `SELECT`, `FROM`

- [x] Completed

---

## Task 02 — Select Specific Columns

Display:

- `customer_id`
- `full_name`
- `email`
- `city`

from `customers`.

**Concepts:** column selection

- [x] Completed

---

## Task 03 — Filter Customers by City

Display customers who live in Bengaluru.

**Concepts:** `WHERE`

- [x] Completed

---

## Task 04 — Sort Customers

Display all customers sorted by `signup_date` from newest to oldest.

**Concepts:** `ORDER BY`, `DESC`

- [x] Completed

---

## Task 05 — Find Active Stores

Display all active stores.

**Concepts:** Boolean filtering

- [x] Completed

---

## Task 06 — Products With Stock

Display products where `stock_quantity > 0`.

**Concepts:** comparison operators

- [x] Completed

---

## Task 07 — Out-of-Stock Products

Find products where `stock_quantity = 0`.

- [x] Completed

---

# 🟡 LEVEL 2 — STRING & DATA CLEANING

## Task 08 — Standardize Customer Names

Return:

- `customer_id`
- uppercase customer name
- city

Use `UPPER()`.

**Concepts:** `UPPER()`, aliases

- [x] Completed

---

## Task 09 — Clean Customer Emails

Return all customer emails in lowercase.

Use `LOWER()`.

- [x] Completed

---

## Task 10 — Normalize Phone Numbers

Remove:

- `+91 `
- `+91-`
- `-`

from customer phone numbers.

**Concepts:** nested `REPLACE()`

- [x] Completed

---

## Task 11 — Q1 Customer Data Cleaning ⭐

Create a customer-cleaning query containing:

- `customer_id`
- `standardized_name`
- `cleaned_email`
- `normalized_phone`
- `city`

**Concepts:** `UPPER()`, `LOWER()`, `REPLACE()`

- [x] Completed

---

# 🟠 LEVEL 3 — JOINS

## Task 12 — Products With Categories

Display:

- product name
- category name
- retail price
- stock quantity

Join `products` and `categories`.

**Concept:** `INNER JOIN`

- [x] Completed

---

## Task 13 — Orders With Customers

Display:

- order ID
- customer name
- order date
- order status

Join `orders` and `customers`.

- [x] Completed

---

## Task 14 — Orders With Store Information

Display:

- order ID
- order date
- store name
- city

Join `orders` and `stores`.

- [x] Completed

---

## Task 15 — Q2 Employee Hierarchy ⭐

Display:

- employee ID
- employee name
- store name
- manager name

Employees without managers must display:

```text
DIRECTOR / NO MANAGER
```

**Concepts:**

- `SELF JOIN`
- `LEFT JOIN`
- `CONCAT()`
- `COALESCE()`

- [x] Completed

---

# 🟠 LEVEL 4 — ANTI-JOIN & NULL HANDLING

## Task 16 — Customers Without Orders

Find customers who have never placed an order.

**Hint:**

Use:

```text
customers
LEFT JOIN orders
```

Then identify unmatched orders.

**Concept:** Anti-Join

- [x] Completed

---

## Task 17 — Q3 Inactive Customers ⭐

Return:

- customer ID
- full name
- email
- city
- signup date

Only customers with zero orders should appear.

- [x] Completed

---

## Task 18 — Employees Without Managers

Find employees where `manager_id` is `NULL`.

**Concept:** `IS NULL`

- [x] Completed

---

# 🔵 LEVEL 5 — AGGREGATIONS

## Task 19 — Count Customers

Find the total number of customers.

**Concept:** `COUNT()`

- [x] Completed

---

## Task 20 — Count Orders

Find the total number of orders.

- [x] Completed

---

## Task 21 — Total Units Sold

Calculate total quantity sold from `order_items`.

**Concept:** `SUM()`

- [x] Completed

---

## Task 22 — Average Product Price

Calculate the average retail price of all products.

**Concept:** `AVG()`

- [x] Completed

---

## Task 23 — Highest Product Price

Find the highest retail price.

**Concept:** `MAX()`

- [x] Completed

---

## Task 24 — Lowest Product Price

Find the lowest retail price.

**Concept:** `MIN()`

- [x] Completed

---

# 🔵 LEVEL 6 — GROUP BY & HAVING

## Task 25 — Customers by City

Count customers in each city.

**Concepts:** `GROUP BY`, `COUNT()`

- [x] Completed

---

## Task 26 — Products by Category

Count products in each category.

- [x] Completed

---

## Task 27 — Orders by Status

Count orders for each `order_status`.

- [x] Completed

---

## Task 28 — Revenue by Store

Calculate revenue for each store using:

```text
quantity × unit_sale_price - discount_amount
```

**Concepts:**

- `SUM()`
- `GROUP BY`
- joins

- [x] Completed

---

## Task 29 — HAVING Filter

Show only stores whose calculated revenue is at least:

```text
15000
```

**Concept:** `HAVING`

- [x] Completed

---

# 🟣 LEVEL 7 — DATE & BUSINESS LOGIC

## Task 30 — Days to Ship

Calculate the number of days between:

```text
order_date
shipped_date
```

**Concept:** date arithmetic

- [x] Completed

---

## Task 31 — Fulfillment Category

Create a calculated column:

```text
Not Shipped
Fast Delivery (<= 2 Days)
Standard / Delayed Delivery
```

Use `CASE`.

- [x] Completed

---

## Task 32 — Delivered Orders Only

Calculate fulfillment time only for orders with:

```text
order_status = 'DELIVERED'
```

- [x] Completed

---

# 🔴 LEVEL 8 — ADVANCED ANALYTICS

## Task 33 — Category Revenue

For each product category calculate:

- total orders involved
- total units sold
- gross sales value
- total discounts
- net revenue

**Concepts:**

- multiple `INNER JOIN`
- `COUNT(DISTINCT ...)`
- `SUM()`
- `GROUP BY`

- [x] Completed

---

## Task 34 — Category Estimated Profit

Calculate:

```text
Net Revenue - Product Cost
```

where product cost is:

```text
quantity × unit_cost
```

**Concept:** multi-table business calculation

- [x] Completed

---

## Task 35 — Store Sales Performance

For active stores, calculate:

- completed orders
- store revenue

Then filter stores with revenue >= `15000`.

**Concepts:**

- `WHERE`
- `GROUP BY`
- `HAVING`
- `ORDER BY`
- `LIMIT`

- [x] Completed

---

## Task 36 — Product-Store Coverage Matrix

Generate every combination of:

```text
active store × in-stock product
```

**Concept:** `CROSS JOIN`

- [x] Completed

---

## Task 37 — Identify Unstocked Products

Find products where:

```text
stock_quantity = 0
```

Then explain why these products would matter to a retail operations team.

- [x] Completed

---

# 🔥 LEVEL 9 — PROJECT BUSINESS QUESTIONS

These are the main milestone analytical questions.

## Q1 — Customer Data Cleaning

Standardize customer names, emails, and phone numbers.

- [x] Completed

---

## Q2 — Internal Organizational Hierarchy

Map employees to their managers and stores.

- [x] Completed

---

## Q3 — Customer Retention / Inactive Accounts

Identify customers who have never placed an order.

- [x] Completed

---

## Q4 — Order Fulfillment SLA

Calculate shipping turnaround time and classify fulfillment performance.

- [x] Completed

---

## Q5 — Category Revenue, Margins & Discount Impact

Calculate:

- gross sales
- discounts
- net revenue
- estimated profit

by category.

- [x] Completed

---

## Q6 — Store Performance

Identify active stores meeting the required revenue threshold.

- [x] Completed

---

## Q7 — Product-Store Coverage

Generate active-store and in-stock-product combinations using `CROSS JOIN`.

- [x] Completed

---

# 🧠 LEVEL 10 — CHALLENGE QUESTIONS

## Challenge 01

Which customer has placed the most orders?

- [x] Completed

---

## Challenge 02

Which product generated the highest net revenue?

- [x] Completed

---

## Challenge 03

Which category generated the highest estimated profit?

- [x] Completed

---

## Challenge 04

Which store generated the highest revenue?

- [x] Completed

---

## Challenge 05

Find customers who placed more than one order.

**Hint:** `GROUP BY` + `HAVING`

- [x] Completed

---

## Challenge 06

Find employees who report directly to Aarav Sharma.

**Concepts:** `SELF JOIN`, filtering

- [x] Completed

---

## Challenge 07

Find products that have never appeared in an order.

**Concept:** Anti-Join

- [x] Completed

---

## Challenge 08

Calculate the average order value.

**Business formula:**

```text
Total Net Revenue / Number of Orders
```

- [x] Completed

---

## Challenge 09

Calculate total discount percentage against gross sales.

**Formula:**

```text
Total Discounts / Gross Sales × 100
```

- [x] Completed

---

## Challenge 10 — Final Challenge ⭐

Create one business report query that shows, for each active store:

- store name
- city
- number of orders
- units sold
- gross sales
- discounts
- net revenue

Sort by net revenue descending.

- [x] Completed
- [x] Reviewed

---


# 📁 Recommended GitHub Structure

```text
SQL/
└── Milestone_Project_01_Retail_Operations/
    │
    ├── README.md
    ├── schema.sql
    ├── seed_data.sql
    ├── analytical_queries.sql
    └── TASK.md
```

---

# 🏁 Milestone Completion Criteria

Before marking this project complete:

- [x] Schema created successfully
- [x] All constraints understood
- [x] Seed data inserted successfully
- [x] Basic SQL tasks completed
- [x] String/data-cleaning tasks completed
- [x] JOIN tasks completed
- [x] Anti-Join understood
- [x] `SELF JOIN` understood
- [x] Aggregation tasks completed
- [x] `GROUP BY` and `HAVING` understood
- [x] Date/`CASE` analysis completed
- [x] Advanced analytical queries completed
- [x] Business challenges completed
- [x] `analytical_queries.sql` cleaned and organized
- [x] README updated
- [x] Project pushed to GitHub

---



