# Day 09 - Python If / Else

## 📚 Topics Covered

- `if` statement
- `if...else`
- `if...elif...else`
- Comparison operators with conditions
- Logical operators with conditions
  - `and`
  - `or`
  - `not`
- Nested `if`
- Conditions with numbers
- Conditions with strings
- Conditions with lists
- Membership conditions
- Truthy and Falsy values
- Conditional expressions
- User input with conditions

---

## 📝 Key Learning

The `if` statement is used to execute code when a condition is `True`.

```python
age = 20

if age >= 18:
    print("Adult")
```

### if...else

Used when there are two possible outcomes.

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### if...elif...else

Used when there are multiple conditions.

```python
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
```

---

## 🔗 Logical Operators

### AND

Both conditions must be `True`.

```python
if age >= 18 and salary >= 30000:
    print("Eligible")
```

### OR

At least one condition must be `True`.

```python
if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

### NOT

Reverses the Boolean result.

```python
if not logged_in:
    print("Please login")
```

---

## 🌳 Nested If

An `if` statement inside another `if`.

```python
if age >= 18:
    if citizen:
        print("Eligible")
```

---

## 🔍 Membership Conditions

Conditions can also check whether a value exists inside a collection.

```python
skills = ["Python", "SQL", "Power BI"]

if "Python" in skills:
    print("Python found")
```

---

## 💡 Truthy and Falsy Values

Python treats some values as `False` in conditions.

Examples:

```python
0
""
[]
{}
None
```

Example:

```python
items = []

if items:
    print("Items available")
else:
    print("List is empty")
```

---

## ⚡ Conditional Expression

A simple `if...else` can be written in one line.

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

---

## 💻 Programs Practiced

- Age eligibility checker
- Positive / Negative / Zero
- Even / Odd checker
- Student grading system
- ATM withdrawal
- Electricity bill calculator
- Login system
- Discount calculator
- Membership access checker
- Student result system
- Employee bonus calculator
- ATM menu system

---

## 🔗 Data Science Connection

Conditional logic is important in data analysis and data science for:

- Filtering data
- Creating business rules
- Categorizing records
- Creating calculated columns
- Data cleaning
- Feature engineering
- Applying business conditions

Example:

```python
if salary >= 50000:
    category = "High Salary"
else:
    category = "Regular Salary"
```

Similar conditional logic is later used with **Pandas**, SQL, and Power BI.

---

## 🎯 Skills Gained

After Day 09, I can:

- Write `if` statements
- Use `if...else`
- Use multiple conditions with `elif`
- Combine conditions using `and`, `or`, and `not`
- Write nested conditions
- Apply conditions to strings and collections
- Use membership operators inside conditions
- Handle user input using conditions
- Translate simple business rules into Python logic

---

## 📂 Files

- `README.md` → Day 09 Notes
- `if_else.py` → Learning and Practice Programs
- `output.txt` → Program Output


```
