# Power BI — Day 22: Choosing the Right Visual

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Choose an appropriate Power BI visual for a business question, then build a report page that communicates sales information clearly.

## Learning objectives
- Explain when to use bar, column, line, pie/donut, table, matrix, and card visuals.
- Match a visual to the question being asked.
- Build a sales analysis page using existing measures and fields.
- Check that each visual communicates one clear message.

## Visual selection guide

| Visual | Best used for | Example question |
|---|---|---|
| Bar chart | Compare categories; especially long labels | Which product categories have the highest sales? |
| Column chart | Compare a small number of categories or periods | Which region has the highest sales? |
| Line chart | Show a trend over time | How did sales change month by month? |
| Pie/donut chart | Show parts of a whole with a few categories | What share of sales comes from each channel? |
| Table | Show exact values and row-level detail | What are the sales values for each product? |
| Matrix | Summarize across rows and columns | What are sales by region and category? |
| Card | Highlight one important number | What are total net sales? |

**Tip:** Donut charts are harder to compare when there are many categories or values are similar. Use a bar chart when precise comparisons matter.

## Before you begin
1. Open your Day 21 Power BI file.
2. Select **File → Save As** and save a copy as `Day22_Choosing_the_Right_Visual.pbix`.
3. Confirm your date table and relationships are working.
4. Reuse your existing `Total Net Sales` measure. If missing, create it using your actual fact table name:
   ```DAX
   Total Net Sales = SUM(FactSales[NetSales])
   ```
   Replace `FactSales` if your sales table has a different name.

## Practical exercise
Create a new report page named **Day 22 — Visual Selection**. Use your actual field/table names if they differ from the examples.

### Visual 1 — Card: total sales
1. Add a **Card** visual.
2. Add `[Total Net Sales]`.
3. Title it **Total Net Sales**.
4. Confirm it displays one overall value.

### Visual 2 — Bar chart: compare categories
1. Add a **Clustered bar chart**.
2. Put `Category` on the Y-axis.
3. Put `[Total Net Sales]` on the X-axis.
4. Sort by Total Net Sales descending.
5. Title it **Net Sales by Category**.

### Visual 3 — Line chart: monthly trend
1. Add a **Line chart**.
2. Put `DimDate[Date]` or a suitable Year-Month field on the X-axis.
3. Put `[Total Net Sales]` on the Y-axis.
4. Title it **Monthly Net Sales Trend**.
5. If using `Month Name`, sort it by `Month Number`. For multiple years, use Year-Month so the same month from different years is not combined.

### Visual 4 — Donut chart: share by channel
1. Add a **Donut chart**.
2. Put `Channel` in Legend.
3. Put `[Total Net Sales]` in Values.
4. Title it **Net Sales Share by Channel**.
5. If there are many channels or the segments are hard to compare, replace it with a bar chart.

### Visual 5 — Table: exact values
1. Add a **Table** visual.
2. Add `Product`, `Category`, and `[Total Net Sales]`.
3. Sort by Total Net Sales descending.
4. Title it **Product Sales Details**.

### Visual 6 — Matrix: two-dimensional comparison
1. Add a **Matrix** visual.
2. Put `Region` in Rows.
3. Put `Category` in Columns.
4. Put `[Total Net Sales]` in Values.
5. Title it **Net Sales by Region and Category**.
6. Check that totals and subtotals look reasonable.

### Optional — Column chart
Build a clustered column chart showing `[Total Net Sales]` by `Region` or `PaymentMode`. Compare it with the bar chart and note which is easier to read for your data.

## Suggested layout
- Top: Total Net Sales card.
- Middle: category bar chart and monthly trend line chart.
- Bottom: channel donut and Region × Category matrix.
- Move the product table to a second page if the main page becomes crowded.

Prioritize readability over fitting every visual on one page.

## Validation checklist
- [ ] Each visual answers a specific business question.
- [ ] Card shows one overall sales value.
- [ ] Category bars are sorted usefully.
- [ ] Line chart uses a true date or correctly sorted Year-Month axis.
- [ ] Donut categories represent parts of the same whole.
- [ ] Table shows exact values with readable column names.
- [ ] Matrix rows, columns, and totals make sense.
- [ ] Titles clearly explain each visual.
- [ ] No visual is unnecessarily crowded.
- [ ] PBIX file is saved.

## Screenshot checklist
Save screenshots in `Screenshots/`:
- `01-total-sales-card.png`
- `02-sales-by-category-bar.png`
- `03-monthly-sales-line.png`
- `04-sales-share-donut.png`
- `05-product-sales-table.png`
- `06-region-category-matrix.png`
- `07-day22-report-page.png`

## GitHub folder
Suggested folder: `Power BI/Day-22-Choosing-the-Right-Visual/`

Include `README.md`, `TASK.md`, screenshots, and the PBIX file if appropriate for your repository size.

## Key takeaway
Choose a visual based on the business question—not simply because it looks attractive. Comparisons usually suit bars/columns, trends suit lines, exact values suit tables, two-dimensional summaries suit matrices, and single KPIs suit cards.
