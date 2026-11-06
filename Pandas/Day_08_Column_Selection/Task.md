# 📝 Day 08 — Column Selection Practice

## Dataset

Use the following dataset:

```python
import pandas as pd

data = {
    "Name": ["Amit", "Sneha", "Ravi", "Priya", "Kiran"],
    "Age": [25, 28, 30, 27, 32],
    "Department": ["Sales", "IT", "HR", "IT", "Finance"],
    "Salary": [50000, 60000, 55000, 65000, 70000],
    "Experience": [2, 4, 5, 3, 8]
}

df = pd.DataFrame(data)
```

---

## Task 1 — Display the Dataset

Print the complete DataFrame.

---

## Task 2 — Select One Column

Select and display the `Name` column.

Then check its type using:

```python
type()
```

**Question:** Does this return a Series or a DataFrame?

---

## Task 3 — Select Another Column

Select and display the `Salary` column.

---

## Task 4 — Select Multiple Columns

Select and display:

- `Name`
- `Department`
- `Salary`

Check the type of the result.

---

## Task 5 — Series vs DataFrame

Run both:

```python
df["Salary"]
```

and:

```python
df[["Salary"]]
```

Check the type of each result.

**Question:** What is the difference between them?

---

## ⭐ Challenge

Create a new DataFrame containing:

- Product
- Category
- Price
- Quantity
- Rating

Then complete the following:

1. Select only the `Product` column.
2. Select `Product` and `Price`.
3. Select `Category`, `Price`, and `Rating`.
4. Check the type of each result.

---

## 🎯 Completion Check

You are ready for Day 09 if you can independently:

- [ ] Select one column.
- [ ] Select multiple columns.
- [ ] Explain the difference between a Series and a DataFrame.
- [ ] Use column selection to focus on relevant data.
