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
- [ ] Add a Card visual.
- [ ] Add `[Total Net Sales]`.
- [ ] Set the title to **Total Net Sales**.

**Question:** What single value does the card display?

### Task 2 — Bar chart
- [ ] Add a Clustered bar chart.
- [ ] `Category` → Y-axis.
- [ ] `[Total Net Sales]` → X-axis.
- [ ] Sort descending by Total Net Sales.
- [ ] Title: **Net Sales by Category**.

**Question:** Which category has the highest net sales?

### Task 3 — Line chart
- [ ] Add a Line chart.
- [ ] Date or Year-Month → X-axis.
- [ ] `[Total Net Sales]` → Y-axis.
- [ ] Title: **Monthly Net Sales Trend**.
- [ ] Ensure the axis is chronological. If using month names, sort by month number; use Year-Month when multiple years are present.

**Question:** Which month or period has the highest sales in the displayed trend?

### Task 4 — Donut chart
- [ ] Add a Donut chart.
- [ ] `Channel` → Legend.
- [ ] `[Total Net Sales]` → Values.
- [ ] Title: **Net Sales Share by Channel**.

**Question:** Which channel has the largest share? If the donut is difficult to compare, switch to a bar chart and note why.

### Task 5 — Table
- [ ] Add a Table visual.
- [ ] Add `Product`, `Category`, and `[Total Net Sales]`.
- [ ] Sort descending by Total Net Sales.
- [ ] Title: **Product Sales Details**.

**Question:** Which product is at the top of the sorted table?

### Task 6 — Matrix
- [ ] Add a Matrix visual.
- [ ] `Region` → Rows.
- [ ] `Category` → Columns.
- [ ] `[Total Net Sales]` → Values.
- [ ] Title: **Net Sales by Region and Category**.

**Question:** Which region/category combination has the highest net sales?

## Part C — Compare visual choices
Write short answers in your notes:
1. Why is a line chart suitable for monthly trends?
2. When is a bar chart easier to read than a donut chart?
3. What is the difference between a table and a matrix?
4. Which visual is best for displaying one headline number?
5. Which visual was most useful for answering a business question, and why?

## Part D — Final validation
- [ ] All six visuals display values.
- [ ] Titles are clear and accurate.
- [ ] Category chart is sorted descending.
- [ ] Date axis is chronologically correct.
- [ ] Donut chart is not excessively crowded.
- [ ] Table and matrix totals look reasonable.
- [ ] No visual is overlapping or unreadable.
- [ ] Save the PBIX file.

## Part E — Screenshots
Capture:
- [ ] `01-total-sales-card.png`
- [ ] `02-sales-by-category-bar.png`
- [ ] `03-monthly-sales-line.png`
- [ ] `04-sales-share-donut.png`
- [ ] `05-product-sales-table.png`
- [ ] `06-region-category-matrix.png`
- [ ] `07-day22-report-page.png`

## Part F — GitHub
Create `Power BI/Day-22-Choosing-the-Right-Visual/` and include `README.md`, `TASK.md`, screenshots, and the PBIX if appropriate for your repository size.

## Completion status
- [ ] All tasks completed
- [ ] Answers recorded
- [ ] Screenshots captured
- [ ] PBIX saved
- [ ] GitHub files prepared

When finished, share your report screenshot(s). I will review the visuals and help correct any issues before Day 23.
