# 🔢 Day 01 — NumPy Basics

## 🎯 Learning Objectives

By the end of this lesson, you should understand:

- What NumPy is
- Why NumPy is used in Data Science
- What an `ndarray` is
- The difference between Python lists and NumPy arrays
- How to create a basic NumPy array
- How NumPy performs vectorized operations

---

# 1. What is NumPy?

**NumPy** stands for **Numerical Python**.

It is a Python library used for working with numerical data efficiently.

NumPy provides a powerful data structure called an **ndarray**, which allows us to store and perform operations on numerical data.

To use NumPy, import it using the standard alias:

```python
import numpy as np
```

The alias `np` is the standard convention used in Python and Data Science projects.

---

# 2. What is an `ndarray`?

An **ndarray** means **N-dimensional array**.

It is the main data structure used in NumPy.

Example:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print(type(numbers))
```

Output:

```text
[10 20 30 40 50]
<class 'numpy.ndarray'>
```

The array can store numerical data and allows us to perform calculations efficiently.

---

# 3. Why Use NumPy?

Python lists are useful for general-purpose programming, but NumPy arrays are designed specifically for numerical computing.

For example, imagine you have sales data:

```python
sales = [1000, 1500, 2000, 2500]
```

If you want to increase every sales value by `100`, you would typically use a loop with a Python list.

With NumPy:

```python
import numpy as np

sales = np.array([1000, 1500, 2000, 2500])

updated_sales = sales + 100

print(updated_sales)
```

Output:

```text
[1100 1600 2100 2600]
```

NumPy applies the operation to every element in the array.

This is one reason NumPy is useful for Data Science.

---

# 4. Python Lists vs NumPy Arrays

## Python List

```python
numbers = [10, 20, 30, 40]

print(numbers)
```

Python lists are flexible and can store different types of data.

```python
data = [10, "Python", 3.5]
```

However, lists are not optimized for large-scale numerical calculations.

---

## NumPy Array

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers)
```

NumPy arrays are designed for efficient numerical operations.

### Simple Comparison

| Feature | Python List | NumPy Array |
|---|---|---|
| General-purpose programming | Yes | Yes |
| Numerical computing | Limited | Excellent |
| Vectorized operations | No | Yes |
| Efficient for large numerical data | Less efficient | More efficient |

> **Important:** NumPy arrays are most useful when you are working with numerical data and mathematical operations.

---

# 5. Vectorized Operations

A **vectorized operation** means performing an operation on an entire array at once.

Example:

```python
import numpy as np

marks = np.array([60, 70, 80, 90])

new_marks = marks + 5

print(new_marks)
```

Output:

```text
[65 75 85 95]
```

You do not need to write a loop to add `5` to every value.

You can also perform other operations:

```python
numbers = np.array([10, 20, 30])

print(numbers + 5)
print(numbers * 2)
print(numbers / 10)
```

Output:

```text
[15 25 35]
[20 40 60]
[1. 2. 3.]
```

We will study array operations in more detail later in this roadmap.

---

# 6. NumPy in Data Science

NumPy is an important foundation for Data Science.

It is commonly used for:

- Numerical calculations
- Data analysis
- Statistical operations
- Working with matrices and arrays
- Machine Learning workflows

Libraries such as **Pandas** and many Machine Learning tools work closely with NumPy.

### Example: Sales Analysis

```python
import numpy as np

sales = np.array([1200, 1500, 1800, 2000, 2200])

increased_sales = sales * 1.10

print(increased_sales)
```

Output:

```text
[1320. 1650. 1980. 2200. 2420.]
```

NumPy allows us to apply the same calculation efficiently across an entire numerical dataset.

---

# 🧠 Key Takeaways

- **NumPy** means Numerical Python.
- The main NumPy data structure is called an **`ndarray`**.
- NumPy arrays are designed for numerical computing.
- NumPy supports **vectorized operations**.
- Vectorization allows operations to be applied to an entire array without manually writing loops.
- NumPy is an important foundation for Pandas, Data Analysis, and Machine Learning.

---

## 📌 Important Terms

| Term | Meaning |
|---|---|
| NumPy | Python library for numerical computing |
| `ndarray` | N-dimensional array used by NumPy |
| Array | A structure used to store multiple values |
| Vectorization | Performing operations on entire arrays efficiently |

---

## ➡️ Next Topic

**Day 02 — Creating Arrays**

You will learn:

- `np.array()`
- `np.zeros()`
- `np.ones()`
- `np.arange()`
- `np.linspace()`
