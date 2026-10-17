# Power BI — Day 25 TASK: Drill-Down, Drill-Through & Tooltips

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Add ways for report viewers to move from summary visuals to detailed information.

## Part A — Open and save
- [x] Open your completed Day 24 PBIX.
- [x] Choose **File → Save As**.
- [x] Save as `Day25_Drilldown_Drillthrough_Tooltips.pbix`.

## Part B — Build a drill-down hierarchy
- [x] Use or create a hierarchy containing Year → Quarter → Month.
- [x] Add a bar or column chart.
- [x] Put the hierarchy on Axis and `[Total Net Sales]` in Values.
- [x] Test drill controls from Year to Quarter to Month.
- [x] Confirm chart values change at each level.
- [x] Sort Month Name by Month Number; include Year if data spans multiple years.

**Question:** What changes when you drill from Year to Month?

## Part C — Create a drill-through page
- [x] Add a page named `Region Details`.
- [x] Add a table with useful details such as Product, Category, Region, and `[Total Net Sales]`.
- [x] Add `Region` to the page's Drill-through field well.
- [x] Keep all filters enabled if source filters should carry over.
- [x] From the main page, right-click a region data point and choose **Drill through → Region Details**.
- [x] Confirm the page is filtered to the selected region.
- [x] Test Back navigation.

**Question:** What detail did the drill-through page reveal that was not obvious on the summary page?

## Part D — Configure tooltips
- [x] Select a chart and enable Tooltips in its Format pane.
- [x] Hover over a data point.
- [x] Add a relevant field or measure to the Tooltips field well, if available.
- [x] Keep tooltip information useful and uncluttered.

**Optional:** Create a report-page tooltip by following the README.

**Question:** What useful information does your tooltip show?

## Part E — Validate
- [x] Drill-down changes the visual's level of detail.
- [x] Drill-through opens the correct page.
- [x] Region filter carries over as expected.
- [x] Back navigation works.
- [x] Tooltips appear on hover.
- [x] Existing slicers continue to work.
- [x] PBIX saved successfully.


## Part G — GitHub
Create `Power BI/Day-25-Drilldown-Drillthrough-Tooltips/` and include `README.md`, `TASK.md`, screenshots, and the PBIX if appropriate for your repository size.

## Completion status
- [x] All tasks completed
- [x] Review questions answered
- [x] Screenshots captured
- [x] PBIX saved
- [x] GitHub files prepared

When finished, share screenshots of your drill-down chart, drill-through page, and tooltip. I will review them before Day 26 — Bookmarks, Buttons & KPIs.
