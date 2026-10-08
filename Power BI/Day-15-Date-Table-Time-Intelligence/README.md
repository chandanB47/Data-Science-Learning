# Power BI — Day 15: Date Table & Time Intelligence Foundation

## Overview
Day 15 focuses on building a proper **Date dimension** and connecting it to the sales fact table. This prepares your model for future time-intelligence calculations such as YTD, MoM, and YoY.

**Level:** Beginner → Intermediate  
**Estimated time:** 75–120 minutes

## Objectives
- Understand why a dedicated Date table is useful.
- Create a continuous Date dimension.
- Add Year, Quarter, Month Number, and Month Name.
- Sort Month Name chronologically.
- Mark the Date table appropriately.
- Create a 1:* Date-to-FactSales relationship.
- Test date filtering in a report.

## Core Concepts
A dedicated calendar lets analysis flow through:
```text
DimDate[Date] → FactSales[OrderDate]
```

A good Date table should contain one row per date, a unique Date column, the complete sales date range, and correct data types.

Typical columns:
```text
Date
Year
Quarter
Month Number
Month Name
```

### Important
Do not sort Month Name alphabetically. Use:
```text
Month Name → Sort by column → Month Number
```

Expected order: January, February, March, … December.

## Target Relationship
```text
DimDate[Date]  1 ───── * FactSales[OrderDate]
```
Use **1:***, **Single**, **Active**.

## Deliverables
1. Complete DimDate table.
2. Year, Quarter, Month Number, Month Name.
3. Correct Month Name sorting.
4. Active relationship to FactSales.
5. Date table configured appropriately.
6. Validation visual using calendar fields.
7. Five screenshots.
8. `Day15_Date_Table_Time_Intelligence.pbix`.

## GitHub Structure
```text
Power BI/
└── Day-15-Date-Table-Time-Intelligence/
    ├── README.md
    ├── TASK.md
    ├── Day15_Date_Table_Time_Intelligence.pbix
    └── Screenshots/
```

## Completion Criteria
DimDate covers the FactSales date range, Date is unique, calendar columns exist, Month Name sorts correctly, the relationship is 1:* / Single / Active, and date filtering works.

## Next
**Day 16 — Advanced Modeling: Relationships, Filter Context & Model Validation**
