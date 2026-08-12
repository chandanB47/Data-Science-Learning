# Day 10 - Python Match / Case

## 📚 Topics Covered

- `match` statement
- `case` statement
- Default case using `_`
- Matching numbers
- Matching strings
- Multiple patterns using `|`
- `match` with user input
- `match` with numeric input
- Calculator using `match`
- Menu-driven programs
- `match` with conditions (guards)
- Difference between `match/case` and `if/elif/else`

---

## 📝 Key Learning

`match/case` is used when we need to compare a value against multiple possible patterns or choices.

### Basic Syntax

```python
choice = 2

match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Delete")
    case _:
        print("Invalid choice")
```

The `_` case works as the default/catch-all case when no other case matches.

---

## 🔢 Matching Multiple Values

The `|` operator allows multiple patterns in one case.

```python
day = "Sunday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")
```

---

## 🧠 Match vs If / Elif

### `if / elif`

Best when checking conditions or ranges.

```python
marks = 85

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
```

### `match / case`

Best when matching specific values or patterns.

```python
choice = 2

match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Delete")
    case _:
        print("Invalid")
```

---

## 💻 Programs Practiced

- Number matching
- Day of week
- Food menu
- Restaurant menu
- Calculator
- Traffic signal
- ATM menu
- Application menu
- Movie ticket selection
- String matching
- Multiple pattern matching
- Match with user input
- Match with conditions

---

## 🔗 Data Science & Real-World Connection

`match/case` can be useful for handling fixed choices such as:

- Menu selections
- User commands
- Status values
- Categories
- Application options
- Processing different types of commands

For example:

```python
status = "success"

match status:
    case "success":
        print("Transaction completed")
    case "failed":
        print("Transaction failed")
    case "pending":
        print("Transaction pending")
    case _:
        print("Unknown status")
```

---

## ⚠️ Important

`match/case` is not a replacement for every `if/elif` statement.

Use `if/elif` when you need conditions such as:

```python
marks >= 90
salary > 50000
age >= 18
```

Use `match/case` when you are primarily matching specific values or patterns.

---

## 🎯 Skills Gained

After Day 10, I can:

- Use `match/case`
- Match numbers
- Match strings
- Handle multiple patterns
- Create menu-driven programs
- Use a default case
- Use user input with `match`
- Combine `match` with `if`
- Understand when to use `match` versus `if/elif`

---

## 📂 Files

- `README.md` → Day 10 Notes
- `match_case.py` → Learning and Practice Programs
- `output.txt` → Program Output

---

## 📈 Progress

```text
Day 01 - Python Basics              ✅
Day 02 - Numbers & Type Casting     ✅
Day 03 - Strings                    ✅
Day 04 - Booleans & Operators       ✅
Day 05 - Lists                      ✅
Day 06 - Tuples                     ✅
Day 07 - Sets                       ✅
Day 08 - Dictionaries               ✅
Day 09 - If / Else                  ✅
Day 10 - Match / Case               ✅
```

