# Power BI — Day 20: Logical DAX

## Overview
**Level:** Beginner to Intermediate  
**Phase:** Level 4 — DAX  
**Estimated time:** 75–120 minutes

## Goal
Use DAX logical functions to express simple business rules. Create and test measures using `IF`, `SWITCH`, `AND`, and `OR`.

## Prerequisites
- Complete Day 19: CALCULATE & Filter Context.
- Open `Day19_CALCULATE_Filter_Context.pbix`.
- Keep the existing model and relationships.
- Check your actual table and column names. Examples use `FactSales` and `NetSales`.

## Topics
- `IF`
- `SWITCH`
- `AND`
- `OR`
- Business-logic measures

## Deliverables
- `Day20_Logical_DAX.pbix`
- A sales classification measure using `IF`
- A sales tier measure using `SWITCH`
- At least one measure that uses `AND` or `OR`
- A report page to test the measures
- Screenshots listed in `TASK.md`

## Folder structure
```text
Power BI/
└── Day-20-Logical-DAX/
    ├── README.md
    ├── TASK.md
    ├── Day20_Logical_DAX.pbix
    └── Screenshots/
```

## Key ideas
- `IF` returns one result when a condition is true and another when it is false.
- `SWITCH` maps an expression or conditions to multiple outcomes.
- `AND` requires both conditions to be true.
- `OR` requires at least one condition to be true.
- Measures evaluate in the current filter context. For row-by-row classifications, a calculated column may be more appropriate; this task focuses on logical measures.

## Important
The thresholds and labels below are practice business rules, not official business definitions. Complete the tasks and share screenshots for review before Day 21.
