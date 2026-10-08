# Power BI — Day 15 TASK: Date Table & Time Intelligence Foundation

**Level:** Beginner → Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Create a proper Date dimension, connect it to FactSales, and prepare the model for future time-intelligence DAX.

## Part A — Start from Day 14
### Task 1
1. Open `Day14_Star_Schema_Dimensions.pbix`.
2. Save a copy as `Day15_Date_Table_Time_Intelligence.pbix`.
3. Open Model view.
4. Confirm FactSales and existing dimensions are available.

## Part B — Check OrderDate
### Task 2
1. Open Data view.
2. Select FactSales.
3. Find `OrderDate`.
4. Confirm its data type is Date or Date/Time.
5. Record the earliest and latest dates.

```text
Minimum OrderDate = __________
Maximum OrderDate = __________
```

If OrderDate is Text, fix the data type in Power Query first.

## Part C — Create DimDate
### Task 3
Select **Modeling → New table** and create:

```DAX
DimDate =
CALENDAR(
    MIN(FactSales[OrderDate]),
    MAX(FactSales[OrderDate])
)
```

Replace FactSales with your actual fact table name if necessary.

**Checkpoint:** DimDate should contain one row for every calendar date in the required range.

## Part D — Add Calendar Columns
### Task 4 — Year
```DAX
Year = YEAR(DimDate[Date])
```

### Task 5 — Quarter
```DAX
Quarter = "Q" & FORMAT(DimDate[Date], "Q")
```

### Task 6 — Month Number
```DAX
Month Number = MONTH(DimDate[Date])
```

### Task 7 — Month Name
```DAX
Month Name = FORMAT(DimDate[Date], "MMMM")
```

Your table should contain at least Date, Year, Quarter, Month Number, and Month Name.

## Part E — Sort Months Correctly
### Task 8
1. Select `DimDate[Month Name]`.
2. Open **Column tools**.
3. Choose **Sort by column**.
4. Select `Month Number`.

Expected order:
```text
January
February
March
April
May
June
July
August
September
October
November
December
```

## Part F — Mark the Date Table
### Task 9
1. Select the `DimDate` table.
2. Open **Table tools**.
3. Select **Mark as date table**.
4. Choose the `Date` column.
5. Confirm.

## Part G — Create the Relationship
### Task 10
In Model view connect:
```text
DimDate[Date]  1 ───── * FactSales[OrderDate]
```
Set:
- Cardinality: **One to many (1:*)**
- Cross filter direction: **Single**
- Active: **Yes**

## Part H — Validate DimDate
### Task 11
Check:
- [ ] Date is unique.
- [ ] No unexpected blank Date.
- [ ] DimDate covers the complete FactSales date range.
- [ ] One row exists per calendar date.
- [ ] Year is numeric.
- [ ] Month Number is numeric.
- [ ] Month Name is text.
- [ ] Date is a Date type.

## Part I — Build a Validation Report
### Task 12
Create a Table or Matrix visual using:
- `DimDate[Year]`
- `DimDate[Quarter]`
- `DimDate[Month Name]`
- `FactSales[NetSales]`

Confirm sales can be analyzed by calendar fields.

## Part J — Test Filtering
### Task 13
Create a slicer using `DimDate[Year]`. Select one year and observe whether NetSales changes.

Expected flow:
```text
DimDate → Relationship → FactSales → NetSales
```

### Task 14
Use `DimDate[Month Name]` and confirm months appear chronologically. If they appear alphabetically, repeat Task 8.

## Part K — Optional Columns
### Task 15
Optional:
```DAX
Day Name = FORMAT(DimDate[Date], "dddd")
```

### Task 16
Optional:
```DAX
Day Number = DAY(DimDate[Date])
```

Do not build YTD/YoY/MoM yet. Those come later.

## Part L — Understand the Foundation
### Task 17
Understand the dependency:
```text
Correct Date Table
       ↓
Correct Date Relationship
       ↓
Calendar Filtering
       ↓
DAX Time Intelligence
       ↓
YTD / YoY / MoM
```

## Knowledge Check
Answer in your own words:
1. Why create a dedicated Date table?
2. Why should Date be unique?
3. Why should DimDate cover the full sales date range?
4. What is Month Number used for?
5. Why sort Month Name by Month Number?
6. What does Mark as date table do?
7. Why is the Date relationship 1:*?
8. Which side should filter the other?
9. Why not use FactSales[OrderDate] for every calendar analysis?
10. What future DAX features depend on a proper Date table?

## Screenshot Checklist
- [ ] `01-date-table.png` — DimDate calendar.
- [ ] `02-date-columns.png` — calendar columns.
- [ ] `03-month-sort.png` — Month Name sorted by Month Number.
- [ ] `04-date-relationship.png` — DimDate → FactSales relationship.
- [ ] `05-date-validation.png` — report visual using calendar fields.

## Completion Checklist
- [ ] Day 14 PBIX copied.
- [ ] OrderDate checked.
- [ ] Min/max dates recorded.
- [ ] DimDate created.
- [ ] Year created.
- [ ] Quarter created.
- [ ] Month Number created.
- [ ] Month Name created.
- [ ] Month Name sorted correctly.
- [ ] DimDate marked as date table.
- [ ] 1:* relationship created.
- [ ] Single direction selected.
- [ ] Date filtering tested.
- [ ] Month order validated.
- [ ] Knowledge check answered.
- [ ] Screenshots saved.
- [ ] PBIX saved as `Day15_Date_Table_Time_Intelligence.pbix`.

## Folder Structure
```text
Power BI/
└── Day-15-Date-Table-Time-Intelligence/
    ├── README.md
    ├── TASK.md
    ├── Day15_Date_Table_Time_Intelligence.pbix
    └── Screenshots/
```

## Next
After completion, share your screenshots and knowledge-check answers for review.

**Day 16 → Advanced Modeling: Relationships, Filter Context & Model Validation**
