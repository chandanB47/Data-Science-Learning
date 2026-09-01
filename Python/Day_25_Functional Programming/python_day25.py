# ==========================================
# Day 25 — Functional Tools: map, filter, reduce
# Script: functional_tools.py
# ==========================================

from functools import reduce

print("=== 1. DATA TRANSFORMATION WITH MAP ===")
celsius_temps = [0, 15, 25, 37, 100]
fahrenheit_temps = list(map(lambda c: round((c * 9 / 5) + 32, 1), celsius_temps))
print("Celsius:   ", celsius_temps)
print("Fahrenheit:", fahrenheit_temps)

# Multi-iterable parallel mapping
quantities = [2, 5, 10]
unit_prices = [49.99, 12.50, 3.20]
totals = list(map(lambda q, p: round(q * p, 2), quantities, unit_prices))
print("Line Totals:", totals)


print("\n=== 2. SUBSETTING WITH FILTER ===")
scores = [85, 42, 90, 58, 73, 31, 99]
passing_scores = list(filter(lambda s: s >= 60, scores))
print("Original Scores:", scores)
print("Passing Scores: ", passing_scores)

# Dropping falsy values with filter(None, ...)
mixed_records = ["valid", "", None, "user_42", 0, [], "admin"]
clean_records = list(filter(None, mixed_records))
print("Clean Records (No Falsy):", clean_records)


print("\n=== 3. AGGREGATION WITH REDUCE ===")
factors = [2, 3, 4, 5]
cumulative_product = reduce(lambda acc, x: acc * x, factors)
print("Cumulative Product of [2, 3, 4, 5]:", cumulative_product)

# Using reduce with an initial accumulator
running_total = reduce(lambda acc, x: acc + x, factors, 50)
print("Sum with initial seed 50:", running_total)


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — String Length Mapping
words_q1 = ["data", "science", "python", "machine"]
word_lengths = list(map(len, words_q1))
print("Q1 Word Lengths:", word_lengths)


# Q2 — Multi-List Dot Product
vector_a = [1, 2, 3, 4]
vector_b = [5, 6, 7, 8]
dot_product = sum(map(lambda a, b: a * b, vector_a, vector_b))
print("Q2 Vector Dot Product:", dot_product)


# Q3 — Non-Empty String Filter
entries_q3 = ["alpha", "", "beta", "   ", "gamma", ""]
valid_entries = list(filter(lambda s: bool(s.strip()), entries_q3))
print("Q3 Non-Empty Strings:", valid_entries)


# Q4 — Threshold Predicate Filter
salaries = [45000, 72000, 120000, 31000, 95000]
high_salaries = list(filter(lambda sal: sal > 60000, salaries))
print("Q4 Salaries > 60,000:", high_salaries)


# Q5 — Cumulative Product with Reduce
nums_q5 = [2, 4, 6, 8]
prod_q5 = reduce(lambda acc, v: acc * v, nums_q5)
print("Q5 Product of [2, 4, 6, 8]:", prod_q5)


# Q6 — Finding Maximum via Reduce
unsorted_vals = [28, 74, 12, 89, 45, 93, 61]
custom_max = reduce(lambda a, b: a if a > b else b, unsorted_vals)
print("Q6 Max via reduce:", custom_max)


# Q7 — Multi-Set Intersection with Reduce
sets_list = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
common_elements = reduce(lambda s1, s2: s1 & s2, sets_list)
print("Q7 Common Elements across Sets:", common_elements)


# Q8 — Cleaning and Typecasting Stream
raw_ids = [" 101 ", "204", "INVALID", " 305 ", "N/A"]
clean_ids = list(map(int, map(str.strip, filter(lambda x: x.strip().isdigit(), raw_ids))))
print("Q8 Clean Integer IDs:", clean_ids)


# Q9 — Grouping Count Dictionary with Reduce
categories = ["A", "B", "A", "C", "B", "A"]
def count_reducer(acc, cat):
    acc[cat] = acc.get(cat, 0) + 1
    return acc

frequency_map = reduce(count_reducer, categories, {})
print("Q9 Category Counts via Reduce:", frequency_map)


# Q10 — Challenge 🔥 (Functional ETL Pipeline)
raw_orders = [
    {"item": "Laptop",  "price": 1000.0, "status": "COMPLETED"},
    {"item": "Mouse",   "price": 25.0,   "status": "CANCELLED"},
    {"item": "Monitor", "price": 300.0,  "status": "COMPLETED"},
    {"item": "Cable",   "price": 15.0,   "status": "PENDING"},
    {"item": "Keyboard","price": 80.0,   "status": "COMPLETED"}
]

# Step 1: Filter completed transactions
completed_orders = filter(lambda order: order["status"] == "COMPLETED", raw_orders)

# Step 2: Map prices with 18% tax applied
taxed_prices = map(lambda order: round(order["price"] * 1.18, 2), completed_orders)

# Step 3: Reduce prices to single total sum
total_revenue = reduce(lambda acc, price: acc + price, taxed_prices, 0.0)

print(f"Q10 Final Revenue (Completed + 18% Tax): ${total_revenue:,.2f}")




