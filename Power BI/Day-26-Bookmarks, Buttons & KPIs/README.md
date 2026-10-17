# Power BI — Day 26: Bookmarks, Buttons & KPIs

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Improve report navigation and communicate key business results using bookmarks, buttons, KPI cards, and conditional formatting.

## Learning objectives
- Create and test a bookmark that captures a report view.
- Add a button for navigation or bookmark actions.
- Use KPI cards to emphasize important measures.
- Apply conditional formatting to make important values easier to identify.
- Test the report as an end user.

## Before you begin
1. Open your completed Day 25 PBIX.
2. Choose **File → Save As**.
3. Save a copy as `Day26_Bookmarks_Buttons_KPIs.pbix`.
4. Keep the previous day's file unchanged.

## Part A — Create a bookmark
1. Go to your main report page and set slicers to a useful view, such as a particular region or year.
2. Open **View → Bookmarks** (the exact pane placement may vary by Power BI version).
3. Add a bookmark and rename it `Regional View`.
4. Review bookmark options. If slicer selections should be restored, ensure the **Data** option is enabled.
5. Change a slicer selection, then select the bookmark to test whether the saved view returns.

## Part B — Add a button
1. Select **Insert → Buttons** and choose a suitable button, such as Blank or Back.
2. For page navigation, enable **Action**, set the type to **Page navigation**, and choose a destination.
3. Alternatively, set Action type to **Bookmark** and choose `Regional View`.
4. Give the button a clear label, such as **Open Regional View** or **Back to Overview**.
5. Test the button in report-reading mode (often Ctrl+click in Power BI Desktop).

**Tip:** If Action is off, a button may be decorative only. Test the action before considering the task complete.

## Part C — Add or review KPI cards
Use existing measures where available:
- `[Total Net Sales]`
- `[Average Net Sales]`
- `[Unique Customers]`
- `[Net Sales YTD]`

1. Add a Card visual for each useful KPI.
2. Use clear titles such as **Total Net Sales** or **Net Sales YTD**.
3. Format values consistently and avoid too many cards.
4. Verify that slicers affect the cards as expected.

If a measure is unavailable, skip that KPI rather than duplicating or approximating a calculation.

## Part D — Apply conditional formatting
1. Select a table or matrix containing `[Total Net Sales]`.
2. Find **Conditional formatting** for background color, font color, or data bars in the field menu or Format pane (options vary by visual/version).
3. Apply a simple rule or color scale to `[Total Net Sales]`.
4. Check that high/low values are easier to identify and text remains readable.
5. Test with different slicer selections.

Avoid using color alone to communicate critical status.

## Part E — End-user test
- Click each button and confirm its action.
- Select each bookmark and confirm the intended view returns.
- Change slicers and check KPI cards update.
- Check conditional formatting remains useful after filtering.
- Confirm there is a clear way to return to the overview page.

## Final checklist
- [ ] Saved as `Day26_Bookmarks_Buttons_KPIs.pbix`.
- [ ] `Regional View` bookmark created and tested.
- [ ] At least one functional button added.
- [ ] Button action tested.
- [ ] KPI cards added or reviewed.
- [ ] Conditional formatting applied to a table or matrix.
- [ ] Slicers and navigation tested.
- [ ] PBIX saved.



## GitHub folder
Suggested folder: `Power BI/Day-26-Bookmarks-Buttons-KPIs/`

Include `README.md`, `TASK.md`, screenshots, and the PBIX if appropriate for your repository size.

## Key takeaway
Bookmarks save a report state, buttons provide navigation or actions, KPI cards spotlight important measures, and conditional formatting helps users interpret values quickly.
