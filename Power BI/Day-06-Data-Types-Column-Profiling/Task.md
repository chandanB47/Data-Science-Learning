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
OrderID:
OrderDate:
Quantity:
UnitPrice:
NetSales:
City:
DiscountPct:
OrderStatus:
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
Text:
Whole Number:
Decimal Number:
Date:
Date/Time:
True/False:
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

Record:

```text
OrderID:
OrderDate:
City:
Quantity:
NetSales:
```

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
City:
Category:
Product:
PaymentMode:
OrderStatus:
```

# 📈 Task 6 — Check Column Profile
Enable **Column profile**.

Select `NetSales`, then `Quantity`.

Record:

```text
NetSales profile:

Quantity profile:
```

# 🧪 Task 7 — Compare Column Types
Complete:

| Column | Data Type | Observation |
|---|---|---|
| City | | |
| Quantity | | |
| UnitPrice | | |
| OrderDate | | |
| NetSales | | |

# 🧠 Task 8 — Data Type Challenge
Predict the appropriate type before checking Power Query:

| Column | Your Prediction |
|---|---|
| OrderID | |
| City | |
| Quantity | |
| UnitPrice | |
| DiscountPct | |
| OrderDate | |
| NetSales | |
| OrderStatus | |

Record any differences:

```text
Different columns:
Reason:
```

# 📝 Task 9 — Knowledge Check

1. What is a data type?
2. Why are correct data types important?
3. What is Text used for?
4. Difference between Whole Number and Decimal Number?
5. Difference between Date and Date/Time?
6. What does Column Quality show?
7. What does Column Distribution help you understand?
8. What does Column Profile help you inspect?
9. Why should data be inspected before transformation?

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
- [ ] Power Query opened
- [ ] Data types identified
- [ ] Main data types understood
- [ ] Column Quality checked
- [ ] Column Distribution checked
- [ ] Column Profile checked
- [ ] Columns compared
- [ ] Data type challenge completed
- [ ] Knowledge check completed
- [ ] Screenshots captured
- [ ] PBIX saved
- [ ] Observations recorded
- [ ] GitHub folder organized
- [ ] Changes committed

# 🚀 Day 6 Finish
 we move to **Day 7 — Nulls, Errors & Duplicates**.
