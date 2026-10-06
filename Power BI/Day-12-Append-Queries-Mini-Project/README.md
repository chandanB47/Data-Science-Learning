# 📊 Power BI — Day 12: Append Queries & Mini Project

## 📌 Overview
Day 12 completes the Power Query & Data Preparation section. You will learn **Append Queries**, understand Append vs Merge, validate the combined data, and complete a mini project using skills from Days 6–11.

**Level:** Beginner  
**Estimated time:** 90–120 minutes

## 🎯 Learning Objectives
- Combine tables vertically with Append.
- Understand Append Queries vs Append Queries as New.
- Check compatible columns and data types.
- Validate row counts after appending.
- Apply cleaning, conditional columns, custom columns, grouping, and merge skills together.

## 📚 Key Concept

**Append combines rows.**

```text
Sales Part A
   Row 1
   Row 2
   Row 3
      +
Sales Part B
   Row 4
   Row 5
   Row 6
      ↓
Sales Appended
   Row 1
   Row 2
   Row 3
   Row 4
   Row 5
   Row 6
```

### Merge vs Append

| Merge | Append |
|---|---|
| Combines columns | Combines rows |
| Uses a matching key | Uses compatible columns |
| Similar to SQL JOIN | Similar to SQL UNION |
| Horizontal | Vertical |

## 🧰 Practical Setup
Your main dataset is one sales table. For realistic Append practice, create two reference queries from the original sales query:
- `Sales_Part_A`
- `Sales_Part_B`

Then use **Append Queries as New** to create:
- `Sales_Appended`

Keep the original detailed query unchanged.

## 🏁 Deliverables
1. Two compatible source queries.
2. `Sales_Appended` query.
3. Row-count validation.
4. Data-quality checks.
5. Mini project using previous Power Query skills.
6. Screenshots.
7. `Day12_Append_Mini_Project.pbix`.

## 📁 GitHub Structure
```text
Power BI/
└── Day-12-Append-Queries-Mini-Project/
    ├── README.md
    ├── TASK.md
    ├── Day12_Append_Mini_Project.pbix
    └── Screenshots/
        ├── 01-source-queries.png
        ├── 02-append-dialog.png
        ├── 03-appended-results.png
        ├── 04-validation.png
        ├── 05-mini-project-cleaning.png
        └── 06-mini-project-final.png
```

## 🧠 Skills Covered
- Day 6 — Data Types & Column Profiling
- Day 7 — Nulls, Errors & Duplicates
- Day 8 — Rename, Split & Replace
- Day 9 — Conditional & Custom Columns
- Day 10 — Group By & Aggregation
- Day 11 — Merge Queries
- Day 12 — Append Queries + Mini Project

## ⏭️ Next Phase
**Day 13 — Introduction to Data Modeling & Relationships**
