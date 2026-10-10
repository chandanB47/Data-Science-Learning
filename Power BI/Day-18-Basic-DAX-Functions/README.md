# Power BI — Day 18: Basic DAX Functions

## Overview
**Level:** Beginner to Intermediate  
**Phase:** Level 4 — DAX  
**Estimated time:** 75–120 minutes

## Goal
Create basic aggregation measures with `SUM`, `AVERAGE`, `COUNT`, `COUNTA`, and `DISTINCTCOUNT`. Validate their results in report visuals and test how they respond to slicers.

## Prerequisites
- Complete Day 17: Measures vs. Calculated Columns.
- Open `Day17_Measures_vs_Calculated_Columns.pbix`.
- Keep the existing model and relationships.
- Check your actual table and column names before entering formulas. Examples below use `FactSales`.

## Topics
- `SUM`, `AVERAGE`, `COUNT`, `COUNTA`, and `DISTINCTCOUNT`
- Basic aggregation measures
- Validate measures in visuals and filter context

## Deliverables
- `Day18_Basic_DAX_Functions.pbix`
- Five basic aggregation measures
- A report page with Cards and a grouped visual
- Screenshots listed in `TASK.md`

## Folder structure
```text
Power BI/
└── Day-18-Basic-DAX-Functions/
    ├── README.md
    ├── TASK.md
    ├── Day18_Basic_DAX_Functions.pbix
    └── Screenshots/
```

## Key idea
DAX aggregation functions summarize a column. A measure is evaluated in the current filter context, so slicers and visual groupings can change its result.

## Important
Use measures for today's calculations. Do not create calculated columns for totals or distinct counts. Complete the tasks and share screenshots for review before continuing to Day 19.
