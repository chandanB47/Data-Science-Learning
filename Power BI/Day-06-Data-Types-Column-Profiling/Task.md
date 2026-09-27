# 📊 Power BI — Day 06 TASK: Data Types & Column Profiling

**Level:** Beginner  
**Day:** 6 of 30  
**Phase:** Level 2 — Power Query & Data Preparation  
**Dataset:** Power BI Master Sales Dataset — 1,500 rows

# 🎯 Task Goal
Today you will inspect data types and learn how to profile columns before performing transformations.

```text
Open Power Query
↓
Inspect Data Types
↓
Column Quality
↓
Column Distribution
↓
Column Profile
↓
Record Observations
```

# 🧭 Task 1 — Open Power Query
1. Open your Day 5 PBIX.
2. Select **Home → Transform data**.
3. Select the sales query.
4. Do not make unnecessary transformations today.

# 🔢 Task 2 — Identify Data Types
Identify the data type shown by Power Query for:

```text
OrderID: Text
OrderDate: Date
Quantity: Whole Number
UnitPrice: Decimal Number
NetSales: Decimal Number
City: Text
DiscountPct: Decimal Number
OrderStatus: Text
```

# 📚 Task 3 — Understand Main Data Types

### Text
Used for values such as City, Product, Category, and PaymentMode.

### Whole Number
Used for numbers without decimals, such as Quantity.

### Decimal Number
Used for values that can contain decimals, such as UnitPrice and sales amounts.

### Date
Contains a calendar date.

### Date/Time
Contains both date and time.

### True/False
Contains logical values.

Write one example for each:

```text
Text: A to Z like names 
Whole Number : 12334 without point values
Decimal Number: with point values like 1.2 
Date: 12/04/2026 
Date/Time: 18/05/2026, 10:34am 
True/False: true
```

# 🔍 Task 4 — Check Column Quality
1. In Power Query, open **View**.
2. Enable **Column quality**.
3. Inspect:
   - `OrderID`
   - `OrderDate`
   - `City`
   - `Quantity`
   - `NetSales`



# 📊 Task 5 — Check Column Distribution
Enable **Column distribution**.

Inspect:
- `City`
- `Category`
- `Product`
- `PaymentMode`
- `OrderStatus`

Record what you observe about repeated and distinct values.

```text
City:  10 distinct , 0 unique 
Category:  5 distinct , 0 unique
Product:  12 distinct , 0 unique 
PaymentMode:  5 distinct , 0 unique 
OrderStatus:  3 distinct , 0 unique
```

# 📈 Task 6 — Check Column Profile
Enable **Column profile**.

Select `NetSales`, then `Quantity`.

Record:

```text
Quantity profile

From your screenshot:

Count: 1000
Error: 0
Empty: 0
Distinct: 9
Unique: 0
Minimum: 1
Maximum: 10
Average: 3.481
NetSales profile

From your screenshot:

Count: 1000
Error: 0
Empty: 0
Distinct: 422
Unique: 156
Minimum: 660
Maximum: 522500
Average: ≈ 48,487.9
```

# 🧪 Task 7 — Compare Column Types

| Column | Data Type | Observation |
|---|---|---|
| City | Text | Contains city names |
| Quantity | Whole Number | Contains purchased quantity |
| UnitPrice | Decimal Number | Contains price per product |
| OrderDate | Date | Contains order date |
| NetSales | Decimal Number | Contains total sales value |

---

# 🧠 Task 8 — Data Type Challenge

| Column | Your Prediction |
|---|---|
| OrderID | Text |
| City | Text |
| Quantity | Whole Number |
| UnitPrice | Decimal Number |
| DiscountPct | Decimal Number |
| OrderDate | Date |
| NetSales | Decimal Number |
| OrderStatus | Text |

## Differences

```text
Different columns: None
Reason: All predictions matched the data types shown in Power Query..
```

# 📝 Task 9 — Knowledge Check

1. What is a data type?

A data type defines what kind of values are stored in a column, such as Text, Whole Number, Decimal Number, Date, Date/Time, or True/False.

2. Why are correct data types important?

Correct data types help Power Query and Power BI interpret and work with the data correctly.

3. What is Text used for?

Text is used for values such as City, Product, Category, and PaymentMode.

4. Difference between Whole Number and Decimal Number?
Whole Number: numbers without decimal values, such as 10 or 100.
Decimal Number: numbers that can contain decimal values, such as 10.5 or 1250.75.

5. Difference between Date and Date/Time?
Date: contains only a calendar date.
Date/Time: contains both a date and a time.

6. What does Column Quality show?

Column Quality shows the percentage of Valid, Error, and Empty values in a column.

7. What does Column Distribution help you understand?

It helps you understand distinct and repeated values in a column and how those values are distributed.

8. What does Column Profile help you inspect?

It provides statistics about a selected column, such as count, errors, empty values, distinct values, unique values, minimum, maximum, average, and distribution.

9. Why should data be inspected before transformation?

Because you should understand the existing data types, quality, values, errors, and distribution before changing the data. This reduces the risk of making incorrect transformations.

# 📸 Screenshot Checklist

Create:

```text
Day-06-Data-Types-Column-Profiling/
└── Screenshots/
```

Capture:

### 01
`01-power-query-data-types.png` — Data types visible.

### 02
`02-column-quality.png` — Column Quality enabled.

### 03
`03-column-distribution.png` — Column Distribution enabled.

### 04
`04-column-profile.png` — Column Profile for a selected column.

### 05
`05-data-type-observations.png` — Your inspection/observation work.

# 💾 Save PBIX
After completing the tasks, select **Close & Apply** and save:

```text
Day06_Data_Types_Column_Profiling.pbix
```

# 🗂️ GitHub Structure
```text
Day-06-Data-Types-Column-Profiling/
├── README.md
├── TASK.md
├── Day06_Data_Types_Column_Profiling.pbix
└── Screenshots/
    ├── 01-power-query-data-types.png
    ├── 02-column-quality.png
    ├── 03-column-distribution.png
    ├── 04-column-profile.png
    └── 05-data-type-observations.png
```

# ✅ Completion Checklist
- [x] Power Query opened
- [x] Data types identified
- [x] Main data types understood
- [x] Column Quality checked
- [x] Column Distribution checked
- [x] Column Profile checked
- [x] Columns compared
- [x] Data type challenge completed
- [x] Knowledge check completed
- [x] Screenshots captured
- [x] PBIX saved
- [x] Observations recorded
- [x] GitHub folder organized
- [x] Changes committed

# 🚀 Day 6 Finish
 we move to **Day 7 — Nulls, Errors & Duplicates**.
