# 📝 Day 42 — Practice Tasks

## Task 1 — Import NumPy

Write the code to import NumPy using the standard alias `np`.

---

## Task 2 — Create an Array

Create a NumPy array containing:

```text
10, 20, 30, 40, 50
```

Print the array.

---

## Task 3 — Check the Type

Using the array from Task 2, print its type using the `type()` function.

Answer this question:

**What type of object is a NumPy array?**
```

A NumPy array is an object of type numpy.ndarray. The term ndarray means N-dimensional array, which can store numerical data in one or more dimensions.

```
---

## Task 4 — Vectorized Operation

Create the following NumPy array:

```text
100, 200, 300, 400
```

Add `50` to every element **without using a loop**.

Expected output:

```text
[150 250 350 450]
```

---

## Task 5 — Sales Increase

A company has the following daily sales:

```text
1200, 1500, 1800, 2000, 2200
```

### Your task:

1. Convert the sales data into a NumPy array.
2. Increase every sales value by **10%**.
3. Print the updated sales values.

**Hint:** Multiply the array by `1.10`.

---

## 🎯 Challenge Question

In your own words:

**Why might NumPy arrays be more useful than Python lists when working with large numerical datasets?**

```
NumPy arrays are more useful because they allow us to perform calculations on many values at once without writing loops.
 They are also generally more efficient and faster for large numerical datasets than standard Python lists.
```

```text
Simple example

With a NumPy array:

sales = np.array([100, 200, 300])
updated_sales = sales * 1.10

```

NumPy performs the calculation on all values at once.
