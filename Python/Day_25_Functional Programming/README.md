# Day 25 — Functional Programming: `map()`, `filter()`, `reduce()`

📌 **Overview**

Day 25 covers Python's core functional programming trio: `map()`, `filter()`, and `reduce()`.

In Data Science and Distributed Computing (such as PySpark and Hadoop MapReduce architectures), the Map-Filter-Reduce paradigm is the foundational pattern for transformations, subsets, and aggregations across massive datasets.

Understanding these functions alongside Python's lazy evaluation model is essential for writing clean, pipeline-friendly, memory-efficient code.

---

📚 **Topics Covered**

* What is Functional Programming in Python?
* The `map()` function: syntax, transformation, and multi-iterable pairing
* The `filter()` function: predicate filtering and `None` truthiness filtering
* Lazy evaluation and consuming iterator objects
* The `functools.reduce()` function: cumulative rolling computations
* `map()`/`filter()` vs. List Comprehensions: performance and readability trade-offs
* Combining `map()`, `filter()`, and `reduce()` into an end-to-end data pipeline

---

### 1. Transforming Data with `map()`
`map(function, iterable, ...)` applies a function to every item of an iterable and returns a lazy iterator.

```python
# Single iterable transformation
temperatures_c = [0, 20, 35, 100]
to_fahrenheit = lambda c: (c * 9 / 5) + 32

temps_f = list(map(to_fahrenheit, temperatures_c))
print(temps_f)  # Output: [32.0, 68.0, 95.0, 212.0]

# Multi-iterable parallel mapping
weights = [0.2, 0.3, 0.5]
scores = [80, 90, 100]
weighted_scores = list(map(lambda w, s: w * s, weights, scores))
print(weighted_scores)  # Output: [16.0, 27.0, 50.0]
```

### 2. Subsetting Data with filter()
filter(function_or_None, iterable) yields items for which function(item) returns True. Passing None strips all falsy values (0, "", None, False, []).

```Python
measurements = [12.5, -3.2, 0.0, 45.1, -1.0, 18.9]

# Keep only positive measurements
positive_readings = list(filter(lambda x: x > 0, measurements))
print(positive_readings)  # Output: [12.5, 45.1, 18.9]

# Strip falsy / missing data with None
dirty_tokens = ["data", "", None, "python", 0, "ml"]
clean_tokens = list(filter(None, dirty_tokens))
print(clean_tokens)  # Output: ['data', 'python', 'ml']
```

### 3. Cumulative Aggregation with functools.reduce()
reduce(function, sequence[, initial]) continually applies a function of two arguments to cumulative items from left to right, boiling a sequence down to a single value.

```Python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Factorial / Product calculation: (((1 * 2) * 3) * 4) * 5
product = reduce(lambda acc, val: acc * val, numbers)
print(product)  # Output: 120

# With an initial accumulator seed value
total_with_seed = reduce(lambda acc, val: acc + val, numbers, 100)
print(total_with_seed)  # Output: 115
```
