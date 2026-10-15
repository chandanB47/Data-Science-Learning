# Power BI — Day 23: Formatting & Visual Hierarchy

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Improve the readability and consistency of your Day 22 report using clear titles, readable labels, consistent fonts, alignment, spacing, and visual hierarchy.

## Learning objectives
- Write clear visual titles.
- Format labels and numbers consistently.
- Use alignment and spacing to organize a report page.
- Make the most important information noticeable first.
- Reduce clutter without hiding useful information.

## Before you begin
1. Open your completed Day 22 PBIX.
2. Choose **File → Save As**.
3. Save a copy as `Day23_Formatting_Visual_Hierarchy.pbix`.
4. Keep your Day 22 file unchanged.

## Part A — Choose a consistent style
- Use one font family throughout the page.
- Use a consistent title style.
- Keep titles more prominent than supporting labels.
- Use a small, consistent color palette.
- Keep backgrounds and borders subtle.
- Avoid unnecessary decoration, excessive colors, and crowded labels.

## Part B — Improve visual titles
Select each visual and open **Format visual → General → Title** (the exact pane layout may vary by Power BI version).

Use these titles:
- Card: **Total Net Sales**
- Bar chart: **Net Sales by Category**
- Line chart: **Monthly Net Sales Trend**
- Donut chart: **Net Sales Share by Channel**
- Table: **Product Sales Details**
- Matrix: **Net Sales by Region and Category**

Check spelling, capitalization, and consistency.

## Part C — Format labels and numbers
1. Format sales measures consistently as currency or an appropriate numeric format.
2. Use consistent decimal places; avoid unnecessary decimals.
3. Turn on data labels only where they help interpretation.
4. Ensure axis labels, category names, and table headings are readable.
5. If labels overlap, enlarge the visual, reduce label density, or turn off some labels.

**Note:** Use the correct currency for your dataset/business context. Do not assume a currency symbol if it is not specified.

## Part D — Align and space visuals
1. Arrange the Total Net Sales card near the top.
2. Place the main comparison and trend visuals in the next row.
3. Put supporting visuals lower on the page or on a separate page if needed.
4. Use alignment/distribution options where available.
5. Keep gaps between visuals consistent.
6. Ensure no visual overlaps another or is clipped at the page edge.

## Part E — Establish visual hierarchy
Use this order of attention:
1. **Primary KPI:** Total Net Sales card.
2. **Main analysis:** Net Sales by Category and Monthly Net Sales Trend.
3. **Supporting detail:** channel breakdown, matrix, and product table.

- Make the most important KPI easy to find.
- Use size and position—not bright colors everywhere—to signal importance.
- Remove redundant legends, unnecessary gridlines, and decorative elements when they add no value.
- Keep enough whitespace for an organized report.

## Part F — Review the page
Ask yourself:
- Can a viewer understand the purpose quickly?
- Are titles descriptive?
- Are numbers formatted consistently?
- Is the reading order obvious?
- Are visuals aligned and evenly spaced?
- Is anything too small, crowded, or redundant?
- Does every visual add useful information?

## Final checklist
- [ ] Saved as `Day23_Formatting_Visual_Hierarchy.pbix`.
- [ ] Titles are clear and consistent.
- [ ] Sales values use a consistent format.
- [ ] Fonts and label sizes are readable.
- [ ] Visuals are aligned with consistent spacing.
- [ ] The primary KPI stands out without excessive decoration.
- [ ] Unnecessary clutter has been removed.
- [ ] Report has been reviewed at normal viewing size.

## Screenshot checklist
Save screenshots in a `Screenshots/` folder:
- `01-before-formatting.png` (optional)
- `02-title-and-label-formatting.png`
- `03-alignment-and-spacing.png`
- `04-final-report-page.png`

## GitHub folder
Suggested folder: `Power BI/Day-23-Formatting-Visual-Hierarchy/`

Include `README.md`, `TASK.md`, screenshots, and the PBIX file if appropriate for your repository size.

## Key takeaway
Good formatting is not decoration. It helps viewers identify important information, read values accurately, and understand the story told by the report.
