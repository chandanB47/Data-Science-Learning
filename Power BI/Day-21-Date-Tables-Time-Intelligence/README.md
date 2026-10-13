# Power BI — Day 21: Date Tables & Time Intelligence

## Overview
**Level:** Beginner to Intermediate  
**Phase:** Level 4 — DAX  
**Estimated time:** 75–120 minutes

## Goal
Validate your date table, confirm it is marked as a date table, check Year/Quarter/Month fields and date relationships, and learn the Year-to-Date (YTD) concept.

## Prerequisites
- Complete Day 20: Logical DAX.
- Open `Day20_Logical_DAX.pbix`.
- Keep the existing model and relationships.
- Examples use `FactSales[OrderDate]` and `DimDate[Date]`; adapt names to your model.

## Topics
- Date tables and marking a date table
- Year, Quarter, and Month fields
- Date relationships
- Basic time-intelligence concepts
- Year-to-Date (YTD)

## Deliverables
- `Day21_Date_Tables_Time_Intelligence.pbix`
- Validated `DimDate` with Year, Quarter, Month Number, and Month Name
- Month Name sorted by Month Number
- Active date relationship
- A report page showing sales by year/month and a YTD measure
- Screenshots listed in `TASK.md`

## Folder structure
```text
Power BI/
└── Day-21-Date-Tables-Time-Intelligence/
    ├── README.md
    ├── TASK.md
    ├── Day21_Date_Tables_Time_Intelligence.pbix
    └── Screenshots/
```

## Key concepts
- A dedicated date table supports consistent date filtering and time-based analysis.
- Its date column should have unique, contiguous dates and a Date data type.
- Marking a date table identifies the column representing its dates.
- YTD means Year-to-Date: an accumulated result from the beginning of a year through the current date in the evaluation context.

## Important
Validate the existing date table and relationship before creating duplicates. The task includes a basic YTD measure after the date table is validated. If your dataset covers only a limited period, YTD results are limited to the available data. Complete the tasks and share screenshots for review.
