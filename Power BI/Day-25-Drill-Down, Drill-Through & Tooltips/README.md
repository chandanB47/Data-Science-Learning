# Power BI — Day 25: Drill-Down, Drill-Through & Tooltips

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Help report users move from summarized results to detailed analysis using drill-down, drill-through pages, and useful tooltips.

## Learning objectives
- Create and test a hierarchy for drill-down.
- Configure a drill-through page for more detailed analysis.
- Use tooltips to show context without overcrowding the report.
- Validate navigation and return paths.

## Before you begin
1. Open your completed Day 24 PBIX.
2. Choose **File → Save As**.
3. Save a copy as `Day25_Drilldown_Drillthrough_Tooltips.pbix`.
4. Use your actual table and field names if they differ from examples.

## Part A — Create a hierarchy and test drill-down
1. Locate or create a date hierarchy with `Year`, `Quarter`, and `Month Name`.
2. Add a column or bar chart.
3. Place the hierarchy on Axis and `[Total Net Sales]` in Values.
4. Use the chart's drill controls to move from Year to Quarter to Month.
5. Confirm that the displayed level and sales values change.

**Important:** Sort `Month Name` by `Month Number`. If the dataset spans multiple years, include Year in the hierarchy so months from different years are not combined.

## Part B — Create a drill-through detail page
1. Add a new page named `Region Details`.
2. Add a table with useful fields such as `Region`, `Product`, `Category`, and `[Total Net Sales]`.
3. With the page selected, find the **Drill-through** field well in the Visualizations/Build pane.
4. Drag `Region` into the Drill-through field well.
5. Keep **Keep all filters** enabled if source-page filters should carry over.
6. Return to the main report page.
7. Right-click a region data point and choose **Drill through → Region Details**.
8. Confirm that the detail page is filtered to the selected region.
9. Use the Back button if present, or add one through **Insert → Buttons → Back**.

**Troubleshooting:** Drill-through is available when the source selection supplies the field used by the destination page. If the menu is missing, confirm that the source visual contains `Region` and the destination page has `Region` in its Drill-through field well.

## Part C — Add useful tooltips
1. Select a chart on the main page.
2. Open its Format pane and locate **Tooltips**; ensure they are enabled.
3. Hover over a data point.
4. Add a relevant measure or field to the visual's **Tooltips** field well, if available.
5. Keep tooltip content focused and relevant.

**Optional extension — report-page tooltip**
1. Add a page named `Sales Tooltip`.
2. In page formatting, enable **Tooltip** as the page type and set page size to Tooltip, if available.
3. Add a small card for `[Total Net Sales]` and one relevant detail.
4. Select the source visual and set Tooltip type to **Report page**, then select `Sales Tooltip`.
5. Hover over a data point to test it. Complete standard visual tooltips first if this extension is too advanced today.

## Part D — Validate
- Drill-down changes the chart level.
- Drill-through opens the correct detail page with the selected filter.
- Back navigation returns to the previous page.
- Tooltips appear on hover and contain useful information.
- Existing slicers continue to work.

## Final checklist
- [ ] Saved as `Day25_Drilldown_Drillthrough_Tooltips.pbix`.
- [ ] Date hierarchy added or validated.
- [ ] Drill-down tested from Year to Quarter to Month.
- [ ] `Region Details` page created.
- [ ] Drill-through tested from the main page.
- [ ] Back navigation tested.
- [ ] Tooltips enabled and tested.
- [ ] PBIX saved.



## GitHub folder
Suggested folder: `Power BI/Day-25-Drilldown-Drillthrough-Tooltips/`

Include `README.md`, `TASK.md`, screenshots, and the PBIX if appropriate for your repository size.

## Key takeaway
Drill-down changes the level of detail inside a visual; drill-through navigates to a detail page filtered by a selected data point; tooltips reveal context on hover without adding clutter to the report canvas.
