# Power BI — Day 19: CALCULATE & Filter Context

## Overview
**Level:** Beginner to Intermediate  
**Phase:** Level 4 — DAX  
**Estimated time:** 75–120 minutes

## Goal
Learn how `CALCULATE` evaluates an expression under a modified filter context. Create measures for total sales and filtered sales, then test them with report visuals and slicers.

## Prerequisites
- Complete Day 18: Basic DAX Functions.
- Open `Day18_Basic_DAX_Functions.pbix`.
- Keep the existing star-schema relationships.
- The examples use `FactSales` and `DimProduct[Category]`. Adapt names to match your model.

## Topics
- `CALCULATE`
- Filter context
- Applying filters in measures
- How calculations change when filters are applied

## Deliverables
- `Day19_CALCULATE_Filter_Context.pbix`
- A base sales measure and at least two `CALCULATE` measures
- A report page comparing total sales and category-filtered sales
- Screenshots listed in `TASK.md`

## Folder structure
```text
Power BI/
└── Day-19-CALCULATE-Filter-Context/
    ├── README.md
    ├── TASK.md
    ├── Day19_CALCULATE_Filter_Context.pbix
    └── Screenshots/
```

## Key concepts
- **Filter context:** filters applied when a measure is evaluated, including slicers, visual axes, report/page filters, and relationships.
- **`CALCULATE`:** evaluates an expression in a modified filter context.
- A measure can return different results across categories or slicer selections because its filter context changes.

## Important
`Technology` is only an example category. Use a value that exists in your dataset. Finish the tasks and share screenshots for review before moving to Day 20.
