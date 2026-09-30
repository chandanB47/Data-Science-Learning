# 📊 Power BI — Day 09: Conditional & Custom Columns

**Level:** Beginner  
**Day:** 9 of 30  
**Phase:** Level 2 — Power Query & Data Preparation  
**Dataset:** `PowerBI_Master_Sales_Dataset_1500.csv`

## 🎯 Day 9 Goal

Learn how to create new columns in Power Query using:
- Conditional Columns
- Custom Columns
- Simple `if ... then ... else` logic
- Basic column calculations
- Validation of newly created columns

## 📚 Topics

### Conditional Columns
Create a new value based on a rule or condition.

Example:
```text
If NetSales >= 5000 → "High"
Else → "Low"
```

### Custom Columns
Create a new value using a formula.

Example:
```text
[Quantity] * [UnitPrice]
```

### Basic M Logic
Understand the idea:
```text
if condition then result else result
```

### Validation
Check results, data types, errors, and row count after creating new columns.

## 📁 Expected GitHub Structure

```text
Power BI/
└── Day-09-Conditional-Custom-Columns/
    ├── README.md
    ├── TASK.md
    ├── Day09_Conditional_Custom_Columns.pbix
    └── Screenshots/
        ├── 01-conditional-column.png
        ├── 02-conditional-results.png
        ├── 03-custom-column.png
        ├── 04-custom-results.png
        └── 05-final-validation.png
```

## ✅ Day 9 Deliverables

- Create one Conditional Column
- Create one Custom Column
- Use simple business logic
- Verify generated values
- Review Applied Steps
- Validate data types and errors
- Save the Day 9 `.pbix`
- Capture screenshots
- Update GitHub

## 📸 Screenshot Checklist

| # | Screenshot | Required |
|---|---|---|
| 01 | Conditional Column setup | ✅ |
| 02 | Conditional Column results | ✅ |
| 03 | Custom Column formula | ✅ |
| 04 | Custom Column results | ✅ |
| 05 | Final validation | ✅ |

## 🎓 Expected Learning Outcome

> I can create rule-based and formula-based columns in Power Query and validate the results before using them in a report.

## ➡️ Next Day

**Day 10 — Group By & Aggregation**
