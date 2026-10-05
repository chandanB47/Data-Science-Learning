# 📝 Power BI — Day 10 TASK: Group By & Aggregation

**Level:** Beginner  
**Estimated time:** 60–90 minutes  
**Dataset:** `PowerBI_Master_Sales_Dataset_1500.csv`

## 🎯 Goal
Create summary tables in Power Query using **Group By**. Preserve the original detailed sales query for later lessons.

---

## Part A — Prepare Safely

### Task 1: Open your Day 9 PBIX
1. Open the Power BI file you used for Day 9.
2. Select **Home → Transform data**.
3. In the Queries pane, identify the detailed sales query.
4. Right-click it and select **Reference** (or Duplicate if Reference is unavailable).
5. Rename the new query `City_Sales_Summary`.
6. Keep the original detailed query unchanged.

**Checkpoint:** You should have the original detailed query and a separate summary query.

## Part B — Group by City

### Task 2: Create a basic grouping
1. Select `City_Sales_Summary`.
2. Select the `City` column.
3. Choose **Home → Group By**.
4. In Basic mode, set:
   - Group by: `City`
   - New column name: `Total Net Sales`
   - Operation: `Sum`
   - Column: `NetSales`
5. Select **OK** and inspect the output.

Each row now represents a city rather than an individual transaction.

### Task 3: Create multiple aggregations
For a clean final result, return to a fresh reference of the detailed query if needed, then:
1. Name the query `City_Sales_Summary`.
2. Open **Home → Group By** and choose **Advanced**.
3. Group by `City`.
4. Add these aggregations:
   - `Total Net Sales` | Sum | `NetSales`
   - `Average Net Sales` | Average | `NetSales`
   - `Transaction Rows` | Count Rows
   - `Minimum Net Sales` | Min | `NetSales`
   - `Maximum Net Sales` | Max | `NetSales`
5. Select **OK**.

If you already performed the basic grouping, do not aggregate the summarized result again. Start from the detailed source/reference and configure all five aggregations together.

**Checkpoint:** One row per City, with the five requested summary fields.

## Part C — Group by Category

### Task 4: Build a separate category summary
1. Right-click the original detailed query and select **Reference**.
2. Rename it `Category_Sales_Summary`.
3. Select `Category` and open **Home → Group By → Advanced**.
4. Group by `Category`.
5. Add:
   - `Total Net Sales` | Sum | `NetSales`
   - `Total Quantity` | Sum | `Quantity`
   - `Transaction Rows` | Count Rows
6. Select **OK**.

**Checkpoint:** Each category appears once with its summarized metrics.

## Part D — Validate and Save

## ✅ Task 5 — Validation

| Validation | Result |
|---|---|
| Original detailed query preserved | Yes |
| City summary | 10 cities |
| Category summary | 5 categories |
| Numeric data types | Valid |
| Errors | None |
| Blank group labels | None |
| City total cross-check | Verified |
| Final status | Validated |

### 🔎 Cross-Check

The `Mumbai` total from the detailed source was compared with the City summary.

**City Summary Total:** `7,128,200.5`

**Detailed Source Total:** `7,128,200.5`

**Match:** `Yes / No` - YES

### Task 6: Apply and save
1. Select **Close & Apply**.
2. Save as `Day10_Group_By_Aggregation.pbix`.
3. Save the requested screenshots in your Day 10 `Screenshots` folder.



## 🧠 Knowledge Check
Answer in your own words:
1. What does Group By do in Power Query?
2. How are Sum and Average different?
3. What does Count Rows count?
4. Why preserve the detailed source query?
5. Why does row count usually decrease after grouping?
6. How does grouping by City differ from grouping by Category?
7. Give one way to validate a group total against source records.

## ✅ Completion Checklist
- [x] Original detailed query preserved.
- [x] City summary created with five aggregations.
- [x] Category summary created with three aggregations.
- [x] Data types checked.
- [x] At least one group total validated.
- [x] No unexplained errors.
- [x] PBIX saved with the required name.
- [x] Screenshots saved.
- [x] Knowledge check answered.

## 📦 Suggested Folder Structure
```text
Power BI/
└── Day-10-Group-By-Aggregation/
    ├── README.md
    ├── TASK.md
    ├── Day10_Group_By_Aggregation.pbix
    └── Screenshots/
```

## ⏭️ Next
When you finish, share your screenshots and knowledge-check answers for review. Next lesson: **Day 11 — Merge Queries**.
