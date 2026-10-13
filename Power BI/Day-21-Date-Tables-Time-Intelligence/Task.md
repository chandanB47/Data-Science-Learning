# Power BI — Day 21 TASK: Date Tables & Time Intelligence

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Validate the date table and its relationship to sales, organize date attributes, and create a basic Year-to-Date (YTD) measure.

## Part A — Open and save
1. Open `Day20_Logical_DAX.pbix`.
2. Choose **File → Save As**.
3. Save as `Day21_Date_Tables_Time_Intelligence.pbix`.
4. Check your actual fact table and date table names. Examples use `FactSales` and `DimDate`.
5. Keep the existing model. Do not create a second date table if a suitable one already exists.

## Part B — Validate the date column
1. In Data view, select `DimDate[Date]`.
2. Confirm its data type is **Date**.
3. Confirm the date column has no blanks or duplicate dates.
4. Confirm the table covers the date range in `FactSales[OrderDate]`.
5. In Model view, verify `DimDate[Date]` **1 → \*** `FactSales[OrderDate]`.
6. Confirm cardinality is one-to-many, cross-filter direction is Single, and the relationship is Active.
7. If the table and relationship already work, validate them rather than recreating them.

## Part C — Create or validate date attributes
If these columns already exist, validate them instead of duplicating them. For any missing column, select `DimDate` and choose **New column**.

```DAX
Year = YEAR(DimDate[Date])
```

```DAX
Quarter = "Q" & FORMAT(DimDate[Date], "Q")
```

```DAX
Month Number = MONTH(DimDate[Date])
```

```DAX
Month Name = FORMAT(DimDate[Date], "MMMM")
```

Optional:

```DAX
Day Name = FORMAT(DimDate[Date], "dddd")
```

```DAX
Day Number = DAY(DimDate[Date])
```

## Part D — Sort month names
1. Select `Month Name` in Data view or Model view.
2. Choose **Column tools → Sort by column → Month Number**.
3. Verify months appear chronologically, not alphabetically.
4. If Power BI reports a sort issue, check that each month name maps consistently to one month number.

## Part E — Mark as date table
1. Select `DimDate`.
2. Open **Table tools** (ribbon wording may vary).
3. Choose **Mark as date table**.
4. Select the `Date` column and confirm.
5. If it is already marked correctly, verify the setting rather than repeating the operation.

## Part F — Create a base sales measure
If it does not already exist, create:

```DAX
Total Net Sales =
    SUM(FactSales[NetSales])
```

Replace the table name if yours differs.

## Part G — Create a basic YTD measure
After validating the date table and relationship, create:

```DAX
Net Sales YTD =
    TOTALYTD(
        [Total Net Sales],
        DimDate[Date]
    )
```

This measure accumulates sales from the beginning of the year through the date in the current filter context. If the date table does not cover the relevant dates or the relationship is inactive, results may be incomplete or unexpected.

## Part H — Build a date analysis visual
1. Add a line chart or column chart.
2. Use `DimDate[Month Name]` on the axis and `[Total Net Sales]` as Values.
3. Use `DimDate[Year]` as a slicer or filter so months from different years are not accidentally combined without context.
4. Add a table containing `DimDate[Year]`, `DimDate[Month Name]`, `[Total Net Sales]`, and `[Net Sales YTD]`.
5. Select a year and inspect how YTD accumulates over the available dates.
6. If your dataset covers only a short date range, note that limitation.

## Part I — Validate
- [ ] Date column has Date data type.
- [ ] Date table has unique, contiguous dates for the required range.
- [ ] Date relationship is one-to-many, Single direction, and Active.
- [ ] Year, Quarter, Month Number, and Month Name are available.
- [ ] Month Name is sorted by Month Number.
- [ ] Date table is marked correctly.
- [ ] `Total Net Sales` and `Net Sales YTD` have no DAX errors.
- [ ] Year filtering works and visuals respond correctly.
- [ ] Existing relationships remain unchanged.
- [ ] Save the PBIX file.

## Screenshot checklist
Save screenshots in `Screenshots/`:
- [ ] `01-dimdate-columns.png` — Date table showing date attributes.
- [ ] `02-date-relationship.png` — Model view showing the date relationship.
- [ ] `03-mark-date-table.png` — Date table setting or confirmation.
- [ ] `04-month-sort.png` — Month Name sorted by Month Number.
- [ ] `05-sales-by-month.png` — Sales by month with year context.
- [ ] `06-ytd-measure.png` — YTD formula and report result.

## Knowledge check
Answer in your own words:
1. Why use a dedicated date table?
2. Why must Month Name be sorted by Month Number?
3. What does marking a table as a date table do?
4. What does YTD mean?
5. What should you check if a YTD measure returns blank or unexpected values?

## Completion checklist
- [ ] Saved `Day21_Date_Tables_Time_Intelligence.pbix`.
- [ ] Validated the date table and relationship.
- [ ] Created or verified date attributes and the YTD measure.
- [ ] Captured screenshots.
- [ ] Answered the knowledge-check questions.
- [ ] Shared screenshots here for review.

**GitHub folder:** `Power BI/Day-21-Date-Tables-Time-Intelligence/`
