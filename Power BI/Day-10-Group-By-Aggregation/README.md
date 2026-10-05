# 📊 Power BI — Day 10: Group By & Aggregation

## 📌 Overview
Day 10 focuses on summarizing detailed sales data with **Group By** in Power Query. You will group records by a field and calculate total, average, count, minimum, and maximum values.

**Level:** Beginner  
**Phase:** Power Query & Data Preparation  
**Dataset:** `PowerBI_Master_Sales_Dataset_1500.csv`  
**Estimated time:** 60–90 minutes

## 🎯 Learning Objectives
- Explain when to use Group By.
- Group records by City or Category.
- Calculate Sum, Average, Count Rows, Min, and Max.
- Use Advanced Group By for multiple aggregations.
- Validate summaries while preserving detailed source data.

## 📚 Key Concepts
- **Group By:** Combines rows sharing the same group value into summary rows.
- **Aggregation:** A calculation applied to each group.
- **Count Rows:** Counts source records in each group, not necessarily distinct customers.
- **Table grain:** Grouping changes the level of detail; output rows usually decrease.

## 🧰 Required Columns
Confirm these fields exist: `City`, `Category`, `NetSales`, and `Quantity`. If names differ, select the equivalent fields in your dataset.

## 🏁 Deliverables
1. City summary: total NetSales, average NetSales, transaction-row count, minimum NetSales, maximum NetSales.
2. Category summary: total NetSales, total Quantity, transaction-row count.
3. Validate at least one group total against the detailed source.
4. Save screenshots and `Day10_Group_By_Aggregation.pbix`.

## 📁 Recommended GitHub Structure
```text
Power BI/
└── Day-10-Group-By-Aggregation/
    ├── README.md
    ├── TASK.md
    ├── Day10_Group_By_Aggregation.pbix
    └── Screenshots/
        ├── 01-city-group-by.png
        ├── 02-city-summary-results.png
        ├── 03-category-group-by.png
        ├── 04-category-summary-results.png
        └── 05-validation.png
```

## ✅ Completion Criteria
- Both summary queries exist and are clearly named.
- Aggregations use the intended fields and operations.
- The detailed source query remains available.
- Results are checked for errors and reasonable values.
- PBIX and screenshots are saved.

## ⏭️ Next Day
**Day 11 — Merge Queries:** combine related tables using a matching key.
