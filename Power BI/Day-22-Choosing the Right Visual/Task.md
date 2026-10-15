# Power BI — Day 22 TASK: Choosing the Right Visual

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Build a report page using the right visual for each business question.

## Part A — Open and save
1. Open your completed Day 21 PBIX.
2. Select **File → Save As**.
3. Save as `Day22_Choosing_the_Right_Visual.pbix`.
4. Add a report page and rename it `Day 22 — Visual Selection`.

## Part B — Build six visuals
Use your actual table/column names if they differ from these examples. Reuse `[Total Net Sales]` from Day 21.

### Task 1 — Card
- [x] Add a Card visual.
- [x] Add `[Total Net Sales]`.
- [x] Set the title to **Total Net Sales**.

**Question:** What single value does the card display?

### Task 2 — Bar chart
- [x] Add a Clustered bar chart.
- [x] `Category` → Y-axis.
- [x] `[Total Net Sales]` → X-axis.
- [x] Sort descending by Total Net Sales.
- [x] Title: **Net Sales by Category**.

**Question:** Which category has the highest net sales?

### Task 3 — Line chart
- [x] Add a Line chart.
- [x] Date or Year-Month → X-axis.
- [x] `[Total Net Sales]` → Y-axis.
- [x] Title: **Monthly Net Sales Trend**.
- [x] Ensure the axis is chronological. If using month names, sort by month number; use Year-Month when multiple years are present.

**Question:** Which month or period has the highest sales in the displayed trend?

### Task 4 — Donut chart
- [x] Add a Donut chart.
- [x] `Channel` → Legend.
- [x] `[Total Net Sales]` → Values.
- [x] Title: **Net Sales Share by Channel**.

**Question:** Which channel has the largest share? If the donut is difficult to compare, switch to a bar chart and note why.

### Task 5 — Table
- [x] Add a Table visual.
- [x] Add `Product`, `Category`, and `[Total Net Sales]`.
- [x] Sort descending by Total Net Sales.
- [x] Title: **Product Sales Details**.

**Question:** Which product is at the top of the sorted table?

### Task 6 — Matrix
- [x] Add a Matrix visual.
- [x] `Region` → Rows.
- [x] `Category` → Columns.
- [x] `[Total Net Sales]` → Values.
- [x] Title: **Net Sales by Region and Category**.

**Question:** Which region/category combination has the highest net sales?

## Part C — Compare visual choices

# Day 22 — Knowledge Check: Choosing the Right Visual

**1. Why is a line chart suitable for monthly trends?**

A line chart shows changes over time and makes trends, fluctuations, and peaks easier to identify.

**2. When is a bar chart easier to read than a donut chart?**

A bar chart is easier when comparing several categories or values that are close together because bar lengths are easier to compare than slice angles.

**3. What is the difference between a table and a matrix?**

A table displays records and fields in a flat layout. A matrix organizes data into rows and columns, supports grouped summaries, and can display subtotals and grand totals.

**4. Which visual is best for displaying one headline number?**

A Card visual is best for a single headline metric, such as Total Net Sales.

**5. Which visual was most useful for answering a business question, and why?**

The category bar chart was especially useful because it immediately showed that Electronics generated the highest net sales, making category comparisons straightforward.

## Part D — Final validation
- [x] All six visuals display values.
- [x] Titles are clear and accurate.
- [x] Category chart is sorted descending.
- [x] Date axis is chronologically correct.
- [x] Donut chart is not excessively crowded.
- [x] Table and matrix totals look reasonable.
- [x] No visual is overlapping or unreadable.
- [x] Save the PBIX file.



## Part E — GitHub
Create `Power BI/Day-22-Choosing-the-Right-Visual/` and include `README.md`, `TASK.md`, screenshots, and the PBIX if appropriate for your repository size.

## Completion status
- [x] All tasks completed
- [x] Answers recorded
- [x] Screenshots captured
- [x] PBIX saved
- [x] GitHub files prepared

When finished, share your report screenshot(s). I will review the visuals and help correct any issues before Day 23.
