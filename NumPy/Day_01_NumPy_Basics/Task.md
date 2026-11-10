# 📝 Day 01 — NumPy Basics: Practice Tasks

**Estimated time:** 20–30 minutes

## 🎯 Goal

Practice creating NumPy arrays and understand why NumPy is useful for numerical data.

---

## Task 1 — Import NumPy

Write the code to import NumPy using the standard alias `np`.

Then print a message:

```text
NumPy imported successfully
```

---

## Task 2 — Create Your First Array

Create a NumPy array containing the following values:

```text
10, 20, 30, 40, 50
```

Print:

1. The array
2. The type of the array

### Question

What is the type of a NumPy array?

---

## Task 3 — Student Marks

A student's marks in five subjects are:

```text
65, 72, 80, 75, 90
```

Complete the following:

1. Create a NumPy array called `marks`.
2. Print the array.
3. Add `5` bonus marks to every subject **without using a loop**.
4. Print the updated marks.

Expected result:

```text
[70 77 85 80 95]
```

---

## Task 4 — Sales Data

A company has the following monthly sales:

```text
1200, 1500, 1800, 2000
```

Complete the following:

1. Create a NumPy array called `sales`.
2. Increase every sales value by `10%`.
3. Print the updated sales values.

**Hint:** Multiply the array by `1.10`.

---

## Task 5 — List vs NumPy Array

Consider the following Python list:

```python
numbers_list = [10, 20, 30]
```

And the following NumPy array:

```python
numbers_array = np.array([10, 20, 30])
```

Try the following operation:

```python
numbers_array + 10
```

### Answer these questions:

1. What happens when you add `10` to the NumPy array?
2. Why is this useful when working with numerical datasets?

---

# 🎯 Challenge Task

A shop recorded the following daily profits:

```text
500, 750, 1000, 1250, 1500
```

The shop gives every day's profit a **20% increase** for a forecasting exercise.

Your task:

1. Create a NumPy array called `profits`.
2. Calculate the forecasted profits.
3. Print both the original and forecasted arrays.

### Bonus Question

Explain in your own words:

> What is vectorization, and why can it be useful in Data Science?

```text

Vectorization means performing an operation on an entire NumPy array at once instead of writing a loop to process each value individually.

```

Example

```
profits = np.array([500, 750, 1000])
forecasted_profits = profits * 1.20
```
---

# ✅ Completion Checklist

- [x] I can import NumPy.
- [x] I can create a basic NumPy array.
- [x] I understand what `ndarray` means.
- [x] I can perform a basic vectorized operation.
- [x] I understand one advantage of NumPy over Python lists.
- [ ] I completed the challenge task.
