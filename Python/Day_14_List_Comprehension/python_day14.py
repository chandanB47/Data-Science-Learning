# ==========================================
# Day 14 — Python List Comprehension
# ==========================================

print("=== 1. BASIC LIST COMPREHENSION ===")
numbers = [1, 2, 3, 4, 5]
squares = [num * num for num in numbers]
print("Numbers:", numbers)
print("Squares:", squares)


print("\n=== 2. LIST COMPREHENSION WITH IF CONDITION ===")
num_list = [10, 15, 20, 25, 30, 35]
evens = [x for x in num_list if x % 2 == 0]
print("Original List:", num_list)
print("Filtered Evens:", evens)


print("\n=== 3. LIST COMPREHENSION WITH IF-ELSE ===")
scores_demo = [45, 85, 30, 92, 60]
results_demo = ["Pass" if score >= 50 else "Fail" for score in scores_demo]
print("Scores:", scores_demo)
print("Results:", results_demo)


print("\n=== 4. STRING MANIPULATION ===")
raw_names = ["   chandan ", "RAHUL ", " nani "]
cleaned_names = [name.strip().title() for name in raw_names]
print("Raw Names:", raw_names)
print("Cleaned Names:", cleaned_names)


print("\n=== 5. NESTED LIST COMPREHENSION ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = [num for row in matrix for num in row]
print("Matrix:", matrix)
print("Flattened List:", flattened)


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Basic Squares (Cubes)
nums_q1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes = [x ** 3 for x in nums_q1]
print("\nQ1 Cubes:", cubes)


# Q2 — Filtering Odds
nums_q2 = [12, 17, 22, 29, 34, 41, 50]
odds = [x for x in nums_q2 if x % 2 != 0]
print("Q2 Odd Numbers:", odds)


# Q3 — Uppercase Strings
fruits = ["apple", "banana", "mango", "kiwi"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print("Q3 Uppercase Fruits:", uppercase_fruits)


# Q4 — Filtering Strings by Length
names_q4 = ["Chandan", "Rahul", "Nani", "Amit", "Alok"]
long_names = [name for name in names_q4 if len(name) > 4]
print("Q4 Names > 4 letters:", long_names)


# Q5 — Conditional Replacement (if-else)
scores_q5 = [45, 88, 32, 90, 65, 50]
pass_fail = ["Pass" if score >= 50 else "Fail" for score in scores_q5]
print("Q5 Pass/Fail Status:", pass_fail)


# Q6 — Range Multiples
multiples_of_5 = [x for x in range(1, 51) if x % 5 == 0]
print("Q6 Multiples of 5 (1-50):", multiples_of_5)


# Q7 — Positive Numbers Only
data_q7 = [-10, 20, -30, 40, -50, 60]
positives = [x for x in data_q7 if x > 0]
print("Q7 Positive Integers:", positives)


# Q8 — Nested List Flattening
nested_data = [[10, 20], [30, 40], [50, 60]]
flat_data = [item for sublist in nested_data for item in sublist]
print("Q8 Flattened Data:", flat_data)


# Q9 — Vowels Extraction
sentence = "Python Programming Is Fun"
vowels = [char for char in sentence if char.lower() in "aeiou"]
print("Q9 Extracted Vowels:", vowels)


# Q10 — Challenge 🔥 (Data Cleaning)
raw_scores = [" 85 ", "90", "INVALID", "78", "N/A", "92 "]
clean_scores = [
    int(item.strip())
    for item in raw_scores
    if item.strip().isdigit()
]
print("Q10 Cleaned Numeric Scores:", clean_scores)



