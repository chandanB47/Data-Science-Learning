# 🔢 Day 02 — Creating Arrays

## 🎯 Learning Objectives

By the end of this lesson, you should be able to:

- Create arrays using `np.array()`
- Create arrays filled with zeros using `np.zeros()`
- Create arrays filled with ones using `np.ones()`
- Generate sequences using `np.arange()`
- Generate evenly spaced values using `np.linspace()`

---

# 1️⃣ Creating Arrays with `np.array()`

The most common way to create a NumPy array is using `np.array()`.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
```

### Output

```text
[10 20 30 40 50]
```

You can also create a two-dimensional array.

```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(data)
```

### Output

```text
[[10 20 30]
 [40 50 60]]
```

A 2D array contains **rows and columns**.

---

# 2️⃣ Creating Arrays with `np.zeros()`

`np.zeros()` creates an array filled with zeros.

### One-Dimensional Array

```python
zeros_array = np.zeros(5)

print(zeros_array)
```

### Output

```text
[0. 0. 0. 0. 0.]
```

By default, NumPy creates floating-point values.

### Two-Dimensional Array

```python
zeros_matrix = np.zeros((2, 3))

print(zeros_matrix)
```

### Output

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

The shape `(2, 3)` means:

- 2 rows
- 3 columns

---

# 3️⃣ Creating Arrays with `np.ones()`

`np.ones()` creates an array filled with ones.

```python
ones_array = np.ones(5)

print(ones_array)
```

### Output

```text
[1. 1. 1. 1. 1.]
```

You can also create a two-dimensional array.

```python
ones_matrix = np.ones((3, 2))

print(ones_matrix)
```

### Output

```text
[[1. 1.]
 [1. 1.]
 [1. 1.]]
```

This array has:

- 3 rows
- 2 columns

---

# 4️⃣ Creating Sequences with `np.arange()`

`np.arange()` creates an array containing a sequence of numbers.

```python
numbers = np.arange(5)

print(numbers)
```

### Output

```text
[0 1 2 3 4]
```

The stop value is **not included**.

---

## Start, Stop, and Step

The general syntax is:

```python
np.arange(start, stop, step)
```

### Example 1 — Start and Stop

```python
numbers = np.arange(10, 20)

print(numbers)
```

Output:

```text
[10 11 12 13 14 15 16 17 18 19]
```

### Example 2 — Using a Step

```python
numbers = np.arange(0, 20, 2)

print(numbers)
```

Output:

```text
[ 0  2  4  6  8 10 12 14 16 18]
```

The `step` value determines how much each number increases.

---

# 5️⃣ Creating Arrays with `np.linspace()`

`np.linspace()` creates a specified number of **evenly spaced values** between two numbers.

The general syntax is:

```python
np.linspace(start, stop, number_of_values)
```

Example:

```python
numbers = np.linspace(0, 10, 5)

print(numbers)
```

### Output

```text
[ 0.   2.5  5.   7.5 10. ]
```

This creates **5 evenly spaced values** from `0` to `10`.

### Important Difference

Unlike `np.arange()`, `np.linspace()` normally includes the stop value.

---

# 🔄 `np.arange()` vs `np.linspace()`

| Function | Main Purpose | Example |
|---|---|---|
| `np.arange()` | Create values using a step size | `np.arange(0, 10, 2)` |
| `np.linspace()` | Create a specific number of evenly spaced values | `np.linspace(0, 10, 5)` |

### Example

```python
import numpy as np

print(np.arange(0, 10, 2))
print(np.linspace(0, 10, 5))
```

Output:

```text
[0 2 4 6 8]

[ 0.   2.5  5.   7.5 10. ]
```

The key difference is simple:

> **`arange()` asks: "What step size do you want?"**  
> **`linspace()` asks: "How many values do you want?"**

---

# 📊 Data Science Example

Suppose you want to create placeholder data for sales across five days:

```python
sales = np.zeros(5)

print(sales)
```

You can also generate employee IDs:

```python
employee_ids = np.arange(1001, 1006)

print(employee_ids)
```

Output:

```text
[1001 1002 1003 1004 1005]
```

For numerical simulations and data analysis, `linspace()` is useful when you need a fixed number of evenly distributed values.

---

# 🧠 Key Takeaways

| Function | Purpose |
|---|---|
| `np.array()` | Create an array from existing values |
| `np.zeros()` | Create an array filled with zeros |
| `np.ones()` | Create an array filled with ones |
| `np.arange()` | Create a sequence using a step |
| `np.linspace()` | Create a specific number of evenly spaced values |

---

## 📌 Important Points

- `np.arange()` usually **excludes** the stop value.
- `np.linspace()` normally **includes** the stop value.
- `(2, 3)` represents **2 rows and 3 columns**.
- `np.zeros()` and `np.ones()` create floating-point arrays by default.

---

## ➡️ Next Topic

**Day 03 — Array Properties**

You will learn:

- `shape`
- `size`
- `ndim`
- `dtype`
