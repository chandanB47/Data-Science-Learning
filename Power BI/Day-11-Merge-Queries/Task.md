# 📝 Power BI — Day 11 TASK: Merge Queries

**Level:** Beginner  
**Estimated time:** 60–90 minutes  
**Dataset:** `PowerBI_Master_Sales_Dataset_1500.csv`

## 🎯 Goal
Learn how to combine related queries by matching a common column. Practice a **Left Outer Merge**, expand the matched data, and validate the result.

## Part A — Prepare the Queries

### Task 1: Open Day 10
1. Open your completed Day 10 PBIX.
2. Select **Home → Transform data**.
3. Identify the original detailed sales query.
4. Do not delete your Day 10 summary queries.

### Task 2: Create a Customer Lookup Practice Query
If you already have a separate customer lookup table, use it and skip to Task 3.

Otherwise:
1. Right-click the original detailed sales query.
2. Select **Reference**.
3. Rename it `Customer_Lookup_Practice`.
4. Keep `CustomerID`, `CustomerType`, and `City` if available.
5. Select `CustomerID`.
6. Choose **Home → Remove Rows → Remove Duplicates**.
7. Confirm each CustomerID appears once.

**Why?** A lookup table should normally have one row per key for this practice.

## Part B — Create the Merge Query

### Task 3
1. Right-click the original detailed sales query.
2. Select **Reference**.
3. Rename it `Sales_Merged_Customer`.
4. Confirm `CustomerID` exists.
5. Confirm the CustomerID data type is compatible with the lookup query.

## Part C — Perform the Merge

### Task 4
1. Select `Sales_Merged_Customer`.
2. Choose **Home → Merge Queries**.
3. Top table: `Sales_Merged_Customer`.
4. Bottom table: `Customer_Lookup_Practice`.
5. Click `CustomerID` in both tables.
6. Set **Join Kind → Left Outer (all from first, matching from second)**.
7. Select **OK**.

A new column containing table values should appear. Seeing `Table` in the cells is expected.

## Part D — Expand the Result

### Task 5
1. Find the new merged column.
2. Click its **Expand** button.
3. Select:
   - `CustomerType`
   - `City`
4. You may uncheck **Use original column name as prefix** for cleaner names.
5. Select **OK**.

Your result should contain the original sales columns plus the selected customer information.

## Part E — Validate

### Task 6
Check:
1. The Left Outer Merge preserves the left/sales table row count.
2. CustomerID values remain unchanged.
3. CustomerType and City contain expected values.
4. Filter the expanded fields for nulls.
5. Investigate nulls instead of immediately deleting them.

Possible causes:
- CustomerID is missing from the lookup.
- Data types differ.
- Formatting/spaces differ.
- Lookup does not contain every customer.
- Lookup key is not unique.

## Part F — Understand the Key

### Task 7
Open the Merge dialog and think about what would happen if `CustomerID` were matched to an unrelated field such as `Category`.

Do not permanently change your final query. The purpose is to understand that a merge is meaningful only when the selected columns represent the same relationship.

## Part G — Merge or Append?

### Task 8
Choose **Merge** or **Append**:

1. Add CustomerType to sales using CustomerID.
2. Combine January transactions with February transactions.
3. Bring Product Category from a product lookup into orders.
4. Combine two tables containing the same type of monthly transactions.

Rule:
```text
Related tables + matching key → MERGE
Similar tables + additional rows → APPEND
```

## Part H — Save

### Task 9
1. Review Applied Steps.
2. Confirm the Merge and Expand steps.
3. Check for errors.
4. Select **Close & Apply**.
5. Save as `Day11_Merge_Queries.pbix`.


## 🧠 Knowledge Check
Answer in your own words:
1. What is Merge Queries used for?
2. What is a join key?
3. Why did we use CustomerID?
4. What does Left Outer Join preserve?
5. Why should the lookup table have unique CustomerID values?
6. What does Expand do after a merge?
7. What can cause nulls after a merge?
8. What is the difference between Merge and Append?
9. What could happen with an unrelated join key?
10. Why keep the original detailed query?

## ✅ Completion Checklist
- [x] Two related queries prepared.
- [x] Matching CustomerID fields confirmed.
- [x] Left Outer Merge completed.
- [x] CustomerType and City expanded.
- [x] Row count checked.
- [x] Null/unmatched values checked.
- [x] Applied Steps reviewed.
- [x] PBIX saved as `Day11_Merge_Queries.pbix`.
- [x] Five screenshots saved.
- [x] Knowledge check completed.

## 📦 Folder Structure
```text
Power BI/
└── Day-11-Merge-Queries/
    ├── README.md
    ├── TASK.md
    ├── Day11_Merge_Queries.pbix
    └── Screenshots/
```

## ⏭️ Next
After finishing Day 11, share your screenshots for review.

**Day 12 → Append Queries + Mini Project**
