# Power BI — Day 29: Final Project — Dashboard & Insights

**Level:** Beginner to Intermediate  
**Estimated time:** 90–120 minutes  
**Phase:** Final Project (Day 29 of 30)

## Goal
Turn the validated Day 28 model into a polished, interactive **Sales Performance Dashboard** and write business insights supported by the report.

## Starting point
Open `Day28_Final_Project_Data_Model.pbix` and use **File → Save As** to create:

`Day29_Final_Project_Dashboard_Insights.pbix`

Keep the Day 28 file unchanged.

## Recommended dashboard layout

1. **Header:** Sales Performance Analysis, reporting period, and a short subtitle.
2. **KPI row:** Total Net Sales, Total Orders, Unique Customers, Average Net Sales (or another verified measure).
3. **Main visuals:**
   - Monthly Net Sales trend — line chart.
   - Net Sales by Region — bar chart.
   - Net Sales by Category — column or bar chart.
   - Net Sales by Channel — donut chart or bar chart.
4. **Supporting detail:** matrix of Region × Category, or a product sales table.
5. **Filters:** Date/Year, Region, Category, and Channel slicers, arranged consistently.
6. **Navigation/interactivity:** Reuse the bookmarks, buttons, drill-through, and tooltip features you already tested in earlier days where they improve usability.

## Step-by-step workflow

### 1. Build the final page
Rename the main page to `Sales Performance Dashboard`, or create a new page with that name. Keep the report focused on the business questions from Day 28.

### 2. Add KPI cards
Use the measures validated on Day 28:
- Total Net Sales
- Total Orders
- Unique Customers
- Average Net Sales (clearly understood as average row-level NetSales if using the Day 28 formula)

Format currency and counts consistently. Avoid adding a KPI unless you can explain what it measures.

### 3. Add the charts
- **Line chart:** Date/Month on the X-axis and Total Net Sales on the Y-axis.
- **Bar chart:** Region on the Y-axis/category axis and Total Net Sales as the value.
- **Column or bar chart:** Category and Total Net Sales.
- **Donut or bar chart:** Channel and Total Net Sales.
- **Matrix/table:** add supporting detail without repeating every chart.

Use a date hierarchy or month-year field that sorts chronologically. If month names appear alphabetically, use a proper Month Number sort column or a Year-Month field.

### 4. Add and test slicers
Add slicers for Date/Year, Region, Category, and Channel as appropriate.
- Test each slicer separately.
- Test two slicers together.
- Clear selections and confirm the report returns to the full dataset.
- Check **Format → Edit interactions** so visuals respond as intended.

### 5. Polish layout and accessibility
- Align visuals and use consistent spacing.
- Use clear titles and meaningful number formats.
- Keep color usage consistent.
- Remove redundant legends, gridlines, borders, and unnecessary visuals.
- Ensure labels and titles remain readable.
- Give every chart a title that states what is being compared.

### 6. Verify interactivity
Test the relevant features already built in Days 24–27:
- Slicers and cross-filtering
- Bookmark/button actions
- Drill-down on date hierarchy
- Drill-through to the detail page and Back button
- Tooltips
Do not add a feature only for decoration; keep it if it helps a report user.

### 7. Write three evidence-based insights
Use your actual results; do not copy example numbers. Record:
1. **Performance:** what the overall sales total or trend indicates.
2. **Comparison:** which region/category/channel is strongest or weakest in the current view.
3. **Action:** one practical follow-up the business could investigate.

For each insight, mention the visual or filter context that supports it. Avoid claiming that one factor caused another unless the data supports causation.

### 8. Save and capture evidence
Save the PBIX and capture the dashboard, slicers in use, and at least one drill-through or bookmark interaction.

## Day 29 deliverables
- `Day29_Final_Project_Dashboard_Insights.pbix`
- A polished dashboard page
- Three written insights grounded in the data
- Screenshots of the dashboard and interactions

## Screenshot checklist
- [ ] Full dashboard with KPI cards and charts
- [ ] Dashboard filtered by a Region or Category
- [ ] Monthly trend and region/category comparisons
- [ ] Drill-through, bookmark, or tooltip feature working
- [ ] Supporting matrix/table

## GitHub folder
Create `Power BI/Day-29-Final-Project-Dashboard-Insights/` with `README.md`, `TASK.md`, and `Screenshots/`. Include the PBIX only if repository file-size limits allow.

**Next:** Day 30 — Final Review & GitHub Portfolio.
