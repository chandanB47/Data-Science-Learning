# Power BI — Day 25 TASK: Drill-Down, Drill-Through & Tooltips

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Add ways for report viewers to move from summary visuals to detailed information.

## Part A — Open and save
- [ ] Open your completed Day 24 PBIX.
- [ ] Choose **File → Save As**.
- [ ] Save as `Day25_Drilldown_Drillthrough_Tooltips.pbix`.

## Part B — Build a drill-down hierarchy
- [ ] Use or create a hierarchy containing Year → Quarter → Month.
- [ ] Add a bar or column chart.
- [ ] Put the hierarchy on Axis and `[Total Net Sales]` in Values.
- [ ] Test drill controls from Year to Quarter to Month.
- [ ] Confirm chart values change at each level.
- [ ] Sort Month Name by Month Number; include Year if data spans multiple years.

**Question:** What changes when you drill from Year to Month?

## Part C — Create a drill-through page
- [ ] Add a page named `Region Details`.
- [ ] Add a table with useful details such as Product, Category, Region, and `[Total Net Sales]`.
- [ ] Add `Region` to the page's Drill-through field well.
- [ ] Keep all filters enabled if source filters should carry over.
- [ ] From the main page, right-click a region data point and choose **Drill through → Region Details**.
- [ ] Confirm the page is filtered to the selected region.
- [ ] Test Back navigation.

**Question:** What detail did the drill-through page reveal that was not obvious on the summary page?

## Part D — Configure tooltips
- [ ] Select a chart and enable Tooltips in its Format pane.
- [ ] Hover over a data point.
- [ ] Add a relevant field or measure to the Tooltips field well, if available.
- [ ] Keep tooltip information useful and uncluttered.

**Optional:** Create a report-page tooltip by following the README.

**Question:** What useful information does your tooltip show?

## Part E — Validate
- [ ] Drill-down changes the visual's level of detail.
- [ ] Drill-through opens the correct page.
- [ ] Region filter carries over as expected.
- [ ] Back navigation works.
- [ ] Tooltips appear on hover.
- [ ] Existing slicers continue to work.
- [ ] PBIX saved successfully.


## Part G — GitHub
Create `Power BI/Day-25-Drilldown-Drillthrough-Tooltips/` and include `README.md`, `TASK.md`, screenshots, and the PBIX if appropriate for your repository size.

## Completion status
- [ ] All tasks completed
- [ ] Review questions answered
- [ ] Screenshots captured
- [ ] PBIX saved
- [ ] GitHub files prepared

When finished, share screenshots of your drill-down chart, drill-through page, and tooltip. I will review them before Day 26 — Bookmarks, Buttons & KPIs.
