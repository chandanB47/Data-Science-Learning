# Power BI — Day 24: Slicers & Interactions

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Make your report interactive by adding slicers and checking how visuals filter or highlight one another.

## Learning objectives
- Create and format slicers.
- Understand single-select and multi-select behavior.
- Test cross-filtering and cross-highlighting.
- Control which visuals respond to a slicer or another visual.
- Validate that interactions produce sensible results.

## Before you begin
1. Open your completed Day 23 PBIX.
2. Select **File → Save As**.
3. Save a copy as `Day24_Slicers_and_Interactions.pbix`.
4. Use your actual table and field names if they differ from the examples.

## Part A — Add a Region slicer
1. Add a **Slicer** visual.
2. Drag `Region` into the slicer's field well.
3. Choose a list or dropdown style.
4. Title it **Filter by Region**.
5. Select one region and check whether the KPI, charts, table, and matrix update.

## Part B — Add a Year or Date slicer
1. Add another Slicer visual.
2. Use `DimDate[Year]` if your date table has a Year column, or use `DimDate[Date]`.
3. For a date field, choose a suitable type such as **Between**, if available.
4. Title it **Filter by Year** or **Filter by Date**.
5. Select a year/date range and verify that the report responds.

## Part C — Test selection behavior
1. Select one region and note the result.
2. Try selecting a different region.
3. Test single-select and multi-select behavior where available in your version.
4. Clear the selection using the slicer's clear-selection control.
5. Note how the report changes for each selection.

## Part D — Test visual interactions
1. Select the Region bar chart or another chart.
2. Choose **Format → Edit interactions** in the ribbon (location may vary by Power BI version).
3. Review the icons shown over the other visuals. Choose the intended behavior:
   - **Filter:** show only data matching the selection.
   - **Highlight:** emphasize the selected contribution while retaining context, where supported.
   - **None:** prevent the selected visual from affecting that target.
4. Ensure the main KPI and analysis visuals respond appropriately to the Region slicer.
5. Select a category bar and observe whether the other visuals filter or highlight.
6. Exit Edit interactions and test again.

## Part E — Validate
- Check that slicers use fields with the correct data types.
- Verify relationships support the intended filtering direction.
- Ensure a selection does not unexpectedly blank unrelated visuals.
- Clear all selections and confirm the full report returns.
- If a visual does not respond, check Edit interactions, relationships, and whether the measure uses related fields.

## Final checklist
- [ ] Saved as `Day24_Slicers_and_Interactions.pbix`.
- [ ] Region slicer added and tested.
- [ ] Year or Date slicer added and tested.
- [ ] Single/multiple selection behavior checked.
- [ ] Visual interactions tested.
- [ ] Unwanted interactions set to None where appropriate.
- [ ] Clear-selection behavior tested.
- [ ] Full report returns after clearing selections.
- [ ] PBIX saved.



## GitHub folder
Suggested folder: `Power BI/Day-24-Slicers-and-Interactions/`

Include `README.md`, `TASK.md`, screenshots, and the PBIX if appropriate for your repository size.

## Key takeaway
Slicers provide report filtering controls, while visual interactions determine how selections in one visual affect other visuals. Test the experience from the viewer's perspective.
