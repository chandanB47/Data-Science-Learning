# 🔎 Day 05: Lookup & Reference Functions

Welcome to **Day 05** of the Excel for Data Science & Analytics track. This module covers essential lookup techniques—from legacy `VLOOKUP` to modern `XLOOKUP` and dynamic `INDEX + MATCH` pairs—to merge relational tables and automate business data retrieval.

---

## 📌 Module Overview

- **Module**: Excel for Data Science & Analytics
- **Day**: 05
- **Topic**: Lookup & Reference Functions
- **Business Exercise**: Automated Order Lookup & Master Table Enrichment
- **Dataset**: `Sales_data 10K.xlsx`

---

## 🎯 Learning Objectives

- Master `VLOOKUP` syntax, rules, and column index constraints.
- Implement `XLOOKUP` for bi-directional, resilient, and multi-column lookups.
- Build flexible lookups using the `INDEX` + `MATCH` combination.
- Understand the critical distinction between **Exact Match** and **Approximate Match**.
- Gracefully handle `#N/A` errors using built-in error arguments and `IFERROR`.
- Automate multi-table joins between transactional sales data and dimension master tables.

---

## 🔑 Formula Cheatsheet

| Function / Pattern | Syntax | Description | Example |
| :--- | :--- | :--- | :--- |
| **VLOOKUP** | `=VLOOKUP(lookup_val, table, col_idx, FALSE)` | Searches leftmost column; returns value from column index | `=VLOOKUP(D2, Products!A:D, 2, FALSE)` |
| **XLOOKUP (Basic)** | `=XLOOKUP(lookup_val, lookup_rng, return_rng)` | Modern lookup across any direction (default exact match) | `=XLOOKUP(D2, Products!A:A, Products!B:B)` |
| **XLOOKUP (Safe)** | `=XLOOKUP(lookup_val, lookup_rng, return_rng, "Not Found")` | Returns fallback value instead of `#N/A` if match fails | `=XLOOKUP(D2, Products!A:A, Products!B:B, "Invalid ID")` |
| **INDEX + MATCH** | `=INDEX(return_rng, MATCH(lookup_val, lookup_rng, 0))` | Robust 2-part lookup separating row search from retrieval | `=INDEX(Products!B:B, MATCH(D2, Products!A:A, 0))` |
| **Approximate Match** | `=XLOOKUP(val, tier_rng, rate_rng, , -1)` | Finds closest match at or below the lookup value | `=XLOOKUP(H2, TierTable!A:A, TierTable!B:B, , -1)` |

---

## ⚖️ Lookup Methods Comparison

| Feature | `VLOOKUP` | `INDEX + MATCH` | `XLOOKUP` |
| :--- | :--- | :--- | :--- |
| **Lookup Direction** | Left-to-Right only | Any direction (Left/Right) | Any direction (Left/Right) |
| **Match Mode Default** | Approximate (`TRUE`) | Exact requires `0` | Exact (`0`) |
| **Column Insertion Safety** | ❌ Breaks if columns shift | ✅ Safe (references ranges) | ✅ Safe (references ranges) |
| **Error Handling** | Requires `IFERROR()` wrap | Requires `IFERROR()` wrap | ✅ Built-in 4th argument |
| **Performance (Large Data)** | Slower on large sheets | Fast & memory efficient | Highly optimized |

---

## 💼 Business Scenario: Order Fulfillment & Pricing Enrichment

You are working with a transactional dataset of 10,000 sales records (`Sales_data 10K.xlsx`). The transaction records contain only `Product_ID` and `Customer_ID`. 

Management needs you to enrich the raw transaction log with metadata from external master tables:
1. Fetch `Product_Name`, `Category`, and `Unit_Price` from `Product_Master`.
2. Fetch `Customer_Name` and `Region` from `Customer_Master`.
3. Apply progressive commission rates using an **Approximate Match** tier lookup table.

---

