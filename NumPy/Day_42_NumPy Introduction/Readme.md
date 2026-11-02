# 🔢 Day 42 — NumPy Introduction

## 🎯 Learning Objectives

By the end of this lesson, you should understand:

- What NumPy is
- What an `ndarray` is
- The difference between Python lists and NumPy arrays
- Why NumPy is useful in Data Science
- How to create a basic NumPy array

---

## 📌 What is NumPy?

**NumPy** stands for **Numerical Python**.

It is a Python library used for efficient numerical computing and data analysis.

The main object in NumPy is called an:

> **ndarray — N-dimensional array**

NumPy is widely used in Data Science because it provides fast and efficient operations on numerical data.

---

## 📦 Importing NumPy

The standard way to import NumPy is:

```python
import numpy as np
```

The alias `np` is the standard convention used by most Python developers and Data Scientists.

---

## 🆚 Python Lists vs NumPy Arrays

### Python List

```python
numbers = [10, 20, 30, 40, 50]

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

### NumPy Array

```python
import numpy as np

numbers_array = np.array([10, 20, 30, 40, 50])

print(numbers_array)
```

Output:

```text
[10 20 30 40 50]
```

Although they look similar, NumPy arrays are designed for numerical operations.

---

## ⚡ Vectorized Operations

One major advantage of NumPy is that you can perform operations on an entire array without writing a loop.

```python
import numpy as np

sales = np.array([100, 200, 300])

new_sales = sales + 50

print(new_sales)
```

Output:

```text
[150 250 350]
```

This approach is called a **vectorized operation**.

Instead of manually processing each value with a loop, NumPy applies the operation to the entire array.

---

## 📊 Data Science Example

Suppose a company has the following daily sales:

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

NumPy makes it easy to perform calculations across large numerical datasets.

---

## 🧠 Key Takeaways

| Python List | NumPy Array |
|---|---|
| General-purpose data storage | Numerical computing |
| Requires loops for many calculations | Supports vectorized operations |
| Less efficient for large numerical data | More efficient for numerical operations |

### Important Terms

- **NumPy** → Numerical Python library
- **ndarray** → The main array object in NumPy
- **Vectorization** → Performing operations on an entire array without manually writing loops

---

## ➡️ Next Topic

**Day 43 — Creating Arrays**

You will learn how to create arrays using:

- `np.array()`
- `np.zeros()`
- `np.ones()`
- `np.arange()`
