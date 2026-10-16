# Power BI — Day 24 TASK: Slicers & Interactions

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Add slicers and verify that the report responds correctly to user selections.

## Part A — Open and save
- [ ] Open your completed Day 23 PBIX.
- [ ] Choose **File → Save As**.
- [ ] Save as `Day24_Slicers_and_Interactions.pbix`.

## Part B — Create a Region slicer
- [ ] Add a Slicer visual.
- [ ] Add `Region`.
- [ ] Choose list or dropdown style.
- [ ] Set title to **Filter by Region**.
- [ ] Select a region and verify that the KPI and relevant visuals update.

**Question:** Which values or visuals changed when you selected a region?

## Part C — Create a Year or Date slicer
- [ ] Add a second Slicer visual.
- [ ] Use `DimDate[Year]` or `DimDate[Date]`.
- [ ] Choose a suitable style, such as a year list or date range.
- [ ] Set a clear title.
- [ ] Select a year/date range and verify the result.

**Question:** How did the report change after you filtered the date?

## Part D — Test selection behavior
- [ ] Test selecting one region.
- [ ] Test selecting another region.
- [ ] Test single-select or multi-select behavior where available.
- [ ] Clear the selection and confirm the report returns to the full view.

**Question:** What is the difference between filtering to one selection and allowing multiple selections?

## Part E — Configure visual interactions
1. Select a chart.
2. Open **Format → Edit interactions** (the exact location may vary by version).
3. Review the interaction icons over other visuals.
4. Choose the intended behavior: Filter, Highlight (where supported), or None.

- [ ] Main KPI responds appropriately.
- [ ] Category and trend charts respond appropriately.
- [ ] Table and matrix behave as expected.
- [ ] Unwanted interactions are set to None.
- [ ] Selecting a bar produces the expected filter/highlight behavior.
- [ ] Exit Edit interactions and test again.

**Question:** Give one example of an interaction you kept and explain why.

## Part F — Validate
- [ ] Slicers use the correct fields.
- [ ] Relationships support expected filtering.
- [ ] No unrelated visual goes blank unexpectedly.
- [ ] Clearing selections restores the full report.
- [ ] PBIX saved successfully.

## Part G — Screenshots
Save in `Screenshots/`:
- [ ] `01-region-slicer.png`
- [ ] `02-year-or-date-slicer.png`
- [ ] `03-filtered-report-example.png`
- [ ] `04-edit-interactions.png`
- [ ] `05-full-report-reset.png`

## Part H — GitHub
Create `Power BI/Day-24-Slicers-and-Interactions/` and include `README.md`, `TASK.md`, screenshots, and the PBIX if appropriate for your repository size.

## Completion status
- [ ] All tasks completed
- [ ] Questions answered
- [ ] Screenshots captured
- [ ] PBIX saved
- [ ] GitHub files prepared

Next -  Day 25 — Drill-Down, Drill-Through & Tooltips.
