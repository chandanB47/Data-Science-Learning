# ==========================================
# Day 26 — Python Recursion
# Script: recursion.py
# ==========================================

import sys
from functools import lru_cache

print("=== 1. BASIC FACTORIAL & CALL STACK ===")
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial(5):", factorial(5))
print("Factorial(6):", factorial(6))
print("Current recursion limit:", sys.getrecursionlimit())


print("\n=== 2. FIBONACCI WITH MEMOIZATION ===")
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(10):", fibonacci(10))
print("Fibonacci(50) (Memoized instant compute):", fibonacci(50))


print("\n=== 3. ARBITRARY NESTED TREE TRAVERSAL ===")
def extract_keys(data):
    found_keys = []
    if isinstance(data, dict):
        for key, value in data.items():
            found_keys.append(key)
            found_keys.extend(extract_keys(value))
    elif isinstance(data, list):
        for element in data:
            found_keys.extend(extract_keys(element))
    return found_keys

nested_payload = {
    "user": "r_sharma",
    "metadata": {
        "device": "Android",
        "specs": {"os_ver": 14, "screen": "AMOLED"}
    },
    "tags": ["mobile", "analytics"]
}

print("Extracted Keys:", extract_keys(nested_payload))


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Recursive Sum
def sum_natural(n):
    if n <= 1:
        return n
    return n + sum_natural(n - 1)

print("Q1 Sum of 1 to 10:", sum_natural(10))


# Q2 — String Reversal
def reverse_str(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_str(s[:-1])

print("Q2 Reversal of 'DataScience':", reverse_str("DataScience"))


# Q3 — Recursive Power
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print("Q3 Power 2^8:", power(2, 8))


# Q4 — Count Nested Elements
def count_nested_elements(nested_data):
    count = 0
    for item in nested_data:
        if isinstance(item, list):
            count += count_nested_elements(item)
        else:
            count += 1
    return count

nested_sample = [1, [2, [3, 4], 5], 6, [7, [8, [9]]]]
print("Q4 Total Nested Numbers:", count_nested_elements(nested_sample))


# Q5 — Palindrome Checker
def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    def check(text):
        if len(text) <= 1:
            return True
        if text[0] != text[-1]:
            return False
        return check(text[1:-1])
    return check(cleaned)

print("Q5 'racecar' is palindrome?:", is_palindrome("racecar"))
print("Q5 'machine' is palindrome?:", is_palindrome("machine"))


# Q6 — Greatest Common Divisor (Euclid)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print("Q6 GCD of 48 and 18:", gcd(48, 18))


# Q7 — Flatten Arbitrary Nested Lists
def flatten_list(nested_seq):
    flat = []
    for elem in nested_seq:
        if isinstance(elem, (list, tuple)):
            flat.extend(flatten_list(elem))
        else:
            flat.append(elem)
    return flat

deep_seq = [10, [20, 30, [40, [50, 60]]], 70]
print("Q7 Flattened Sequence:", flatten_list(deep_seq))


# Q8 — Binary Search
def binary_search(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

sorted_arr = [11, 24, 35, 48, 52, 67, 89, 95]
print("Q8 Index of 52:", binary_search(sorted_arr, 0, len(sorted_arr) - 1, 52))
print("Q8 Index of 100:", binary_search(sorted_arr, 0, len(sorted_arr) - 1, 100))


# Q9 — Deep Value Search
def find_nested_value(data, target_key):
    if isinstance(data, dict):
        if target_key in data:
            return data[target_key]
        for val in data.values():
            result = find_nested_value(val, target_key)
            if result is not None:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_nested_value(item, target_key)
            if result is not None:
                return result
    return None

nested_api = {
    "status": "success",
    "response": {
        "payload": {
            "auth": {
                "token": "JWT_TOKEN_SECURE_98127"
            }
        }
    }
}
print("Q9 Extracted Token:", find_nested_value(nested_api, "token"))


# Q10 — Challenge 🔥 (Recursive Decision Tree Route Finder)
decision_tree = {
    "feature": "income",
    "split": 50000,
    "left": {
        "feature": "credit_score",
        "split": 650,
        "left": {"class": "REJECT"},
        "right": {"class": "APPROVE"}
    },
    "right": {
        "feature": "debt",
        "split": 20000,
        "left": {"class": "APPROVE"},
        "right": {"class": "MANUAL_REVIEW"}
    }
}

def predict_tree(node, sample):
    # Base Case: Leaf node reached
    if "class" in node:
        return node["class"]
    
    # Recursive Step: Evaluate threshold and branch
    feature_name = node["feature"]
    threshold = node["split"]
    sample_val = sample.get(feature_name, 0)
    
    if sample_val <= threshold:
        return predict_tree(node["left"], sample)
    else:
        return predict_tree(node["right"], sample)

applicant_1 = {"income": 45000, "credit_score": 720, "debt": 5000}
applicant_2 = {"income": 80000, "credit_score": 600, "debt": 35000}

print(f"Q10 Applicant 1 Prediction: {predict_tree(decision_tree, applicant_1)}")
print(f"Q10 Applicant 2 Prediction: {predict_tree(decision_tree, applicant_2)}")








