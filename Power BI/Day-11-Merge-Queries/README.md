# 📊 Power BI — Day 11: Merge Queries

## 📌 Overview
Day 11 introduces **Merge Queries** in Power Query. You will learn how to combine information from two related tables by matching a common column.

**Level:** Beginner  
**Phase:** Power Query & Data Preparation  
**Dataset:** `PowerBI_Master_Sales_Dataset_1500.csv`  
**Estimated time:** 60–90 minutes

## 🎯 Learning Objectives
- Explain what Merge Queries does.
- Identify a suitable matching/key column.
- Perform a merge between two queries.
- Understand **Left Outer** Join.
- Expand columns from the merged table.
- Validate unmatched records.
- Understand the difference between Merge and Append.

## 📚 Key Concepts

### Merge Queries
Merge combines two tables **horizontally** by matching values in a common column.

### Join Key
The column used to match the two queries. It should represent the same business information in both tables and have compatible data types.

### Left Outer Join
Keeps **all rows from the first/left table** and brings matching rows from the second/right table.

### Merge vs Append

| Merge | Append |
|---|---|
| Combines columns from related tables | Combines rows from tables |
| Uses a matching key | Matches columns by name |
| Similar to SQL JOIN | Similar to SQL UNION |
| Horizontal combination | Vertical combination |

## 🧰 Practical Setup
Your sales data contains fields such as `OrderID`, `CustomerID`, `City`, `Category`, `Product`, `NetSales`, and `CustomerType`.

For this lesson you need two related queries. If your PBIX has only one sales query, the TASK file shows how to safely create a lookup practice query using a reference.

## 🏁 Day 11 Deliverables
1. Successful Merge Queries operation.
2. Correct matching key.
3. Left Outer merge.
4. Expanded information from the second query.
5. Validation of unmatched records.
6. Screenshots in `Screenshots/`.
7. PBIX: `Day11_Merge_Queries.pbix`.

## 📁 Recommended GitHub Structure
```text
Power BI/
└── Day-11-Merge-Queries/
    ├── README.md
    ├── TASK.md
    ├── Day11_Merge_Queries.pbix
    └── Screenshots/
        ├── 01-source-queries.png
        ├── 02-merge-dialog.png
        ├── 03-merged-column.png
        ├── 04-expanded-results.png
        └── 05-validation.png
```

## ✅ Completion Criteria
- Two related queries are available.
- Correct matching key is selected.
- Left Outer Join is completed.
- Merged data is expanded.
- Data types and unmatched rows are checked.
- Original source remains available.
- Screenshots and PBIX are saved.

## ⏭️ Next Day
**Day 12 — Append Queries & Mini Project**
