# 📝 Power BI — Day 12 TASK: Append Queries + Mini Project

**Level:** Beginner  
**Estimated time:** 90–120 minutes  
**Dataset:** `PowerBI_Master_Sales_Dataset_1500.csv`

## 🎯 Goal
Learn how to combine tables vertically using **Append Queries**, validate the result, and complete a mini project using your Power Query skills from Days 6–11.

## Part A — Prepare the Source

### Task 1: Open Day 11
1. Open your completed Day 11 PBIX.
2. Select **Home → Transform data**.
3. Identify the original detailed sales query.
4. Keep the original query unchanged.

### Task 2: Create Sales_Part_A
1. Right-click the original detailed sales query.
2. Select **Reference**.
3. Rename it `Sales_Part_A`.
4. Filter `OrderDate` to one portion of the available dates.
5. Keep the same columns and data types.

### Task 3: Create Sales_Part_B
1. Right-click the original detailed sales query again.
2. Select **Reference**.
3. Rename it `Sales_Part_B`.
4. Apply a complementary `OrderDate` filter for the remaining portion.
5. Keep the same columns and data types.

Structure:
```text
Original Sales
   ├── Sales_Part_A
   └── Sales_Part_B
```

## Part B — Check Compatibility

### Task 4
For both queries:
1. Check column names.
2. Check data types.
3. Confirm both represent the same type of records.
4. Confirm Part A and Part B contain different rows.

Record:
```text
Rows in Part A = 865
Rows in Part B = 635
```

## Part C — Append

### Task 5: Append as New
1. Select **Home → Append Queries → Append Queries as New**.
2. Choose **Two tables**.
3. First table: `Sales_Part_A`.
4. Second table: `Sales_Part_B`.
5. Select **OK**.
6. Rename the result `Sales_Appended`.

**Checkpoint:** The result should contain rows from both source queries.

## Part D — Validate

### Task 6
Calculate:

```text
Expected rows = 1500
Rows in Sales_Part_A + Rows in Sales_Part_B
```

Compare with `Sales_Appended`.

Then check:
- `OrderID`
- `OrderDate`
- `NetSales`
- `Quantity`
- Data types
- Errors
- Unexpected nulls

The row count should match when the two parts are non-overlapping and no extra filtering occurs.

## Part E — Mini Project

### Task 7: Data quality
Use `Sales_Appended` as your base. Review:
- Nulls
- Errors
- Duplicate OrderIDs
- Incorrect data types
- Unexpected formatting

Do not blindly delete records.

### Task 8: Conditional Column
Create `Sales Level`:

```text
NetSales >= 5000 → High
Otherwise → Low
```

### Task 9: Custom Column
Create `Calculated Sales`:

```text
[Quantity] * [UnitPrice]
```

Check that it is numeric.

### Task 10: City Summary
Create a **Reference** from the cleaned/appended query and name it:

`MiniProject_City_Summary`

Use **Group By → Advanced**:
- Group by: `City`
- `Total Net Sales` → Sum of `NetSales`
- `Average Net Sales` → Average of `NetSales`
- `Transaction Rows` → Count Rows

### Task 11: Review Merge
If your Day 11 customer lookup query is still available:
1. Create a reference from the cleaned appended sales query.
2. Merge using `CustomerID`.
3. Use **Left Outer**.
4. Expand one useful field such as `CustomerType`.

If the lookup is not available, review the Day 11 work instead of creating an unrelated merge.

## Part F — Final Validation

### Task 12
Review Applied Steps. Your workflow should logically resemble:

```text
Source
↓
Data Preparation
↓
Append
↓
Conditional Column
↓
Custom Column
↓
Optional Merge
↓
Final Clean Data
```

Then confirm:
- No unexplained errors.
- Correct data types.
- `OrderID` is appropriate for identification.
- `NetSales` and `Quantity` are numeric.
- `Sales Level` contains expected categories.
- `Calculated Sales` is numeric.
- Appended row count is correct.
- City summary has one row per City.

### Task 13: Save
1. Select **Close & Apply**.
2. Save as:
`Day12_Append_Mini_Project.pbix`



## ✅ Completion Checklist

- [x] Sales_Part_A created.
- [x] Sales_Part_B created.
- [x] Columns/data types checked.
- [x] Append Queries as New completed.
- [x] Sales_Appended created.
- [x] Row count validated.
- [x] Errors/duplicates checked.
- [x] Sales Level created.
- [x] Calculated Sales created.
- [x] City summary created.
- [x] Merge skill reviewed/applied.
- [x] PBIX saved.
- [x] Screenshots saved.
- [x] Knowledge check completed.

## 📦 Folder Structure
```text
Power BI/
└── Day-12-Append-Queries-Mini-Project/
    ├── README.md
    ├── TASK.md
    ├── Day12_Append_Mini_Project.pbix
    └── Screenshots/
```

## ⏭️ Next
After finishing, share your screenshots and knowledge-check answers for review.

**Day 13 → Introduction to Data Modeling & Relationships**
