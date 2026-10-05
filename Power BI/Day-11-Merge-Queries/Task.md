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

## 🔎 Task 6 — Merge Validation

| Validation | Result |
|---|---|
| Left table rows preserved | Yes — 145 |
| CustomerID unchanged | Yes |
| CustomerType expanded | Yes |
| City expanded | Yes |
| Nulls in expanded fields | None |
| Unmatched CustomerID | None |
| Final status | Validated |

### 📌 Observation

> The Left Outer Merge preserved all rows from the sales query. CustomerType and City were successfully expanded from the customer lookup table. All 145 sales rows matched a CustomerID in the lookup.


## Part F — Understand the Key

### 🔑Task 7
Open the Merge dialog and think about what would happen if `CustomerID` were matched to an unrelated field such as `Category`.


### Correct Join Key

The merge uses:

```text
Sales_Merged_Customer → CustomerID
Customer_Lookup_Practice → CustomerID
```

Do not permanently change your final query. The purpose is to understand that a merge is meaningful only when the selected columns represent the same relationship.

## Part G — Merge or Append?

## 🔀 Task 8 — Merge or Append?

| Scenario | Choice | Reason |
|---|---|---|
| Add CustomerType to sales using CustomerID | **Merge** | Related tables with a matching key |
| Combine January transactions with February transactions | **Append** | Same type of data; adding rows |
| Bring Product Category from a product lookup into orders | **Merge** | Related tables with a matching key |
| Combine two tables containing the same type of monthly transactions | **Append** | Similar tables; adding rows |

### 📌 Rule

```text
Related tables + matching key → MERGE

Similar tables + additional rows → APPEND

```

## Part H — Save

### 💾 Task 9 — Review & Save
1. Review Applied Steps.

Before saving, check **Query Settings → Applied Steps** for `Sales_Merged_Customer`.

You should see steps related to:

```text
Source
Merged Queries
Expanded Customer_Lookup_Practice
```

2. Confirm the Merge and Expand steps.
3. Check for errors.
4. Select **Close & Apply**.
5. Save as `Day11_Merge_Queries.pbix`.


# 🧠 Day 11 — Knowledge Check

### Q1. What is Merge Queries used for?

Merge Queries is used to combine related data from two queries by matching a common key.

### Q2. What is a join key?

A join key is a column used to match related records between two tables or queries.

### Q3. Why did we use `CustomerID`?

We used `CustomerID` because it identifies the same customer in both the sales query and the customer lookup query.

### Q4. What does a Left Outer Join preserve?

A Left Outer Join preserves all rows from the first (left) table and brings matching records from the second table.

### Q5. Why should the lookup table have unique `CustomerID` values?

A lookup table should have one row per CustomerID to prevent one sales record from matching multiple lookup records and creating unwanted duplication.

### Q6. What does Expand do after a merge?

Expand extracts selected fields from the merged table column and adds them as normal columns.

### Q7. What can cause nulls after a merge?

Nulls can occur when a CustomerID has no match in the lookup, data types differ, formatting or spaces differ, or the lookup does not contain every customer.

### Q8. What is the difference between Merge and Append?

Merge combines related tables using a matching key and adds related columns. Append combines similar tables by adding rows.

### Q9. What could happen with an unrelated join key?

An unrelated join key can produce incorrect matches, unmatched records, or meaningless results.

### Q10. Why keep the original detailed query?

The original detailed query should be preserved so transaction-level data remains available for validation and future transformations.




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
