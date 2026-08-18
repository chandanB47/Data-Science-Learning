# ==========================================
# Day 13 - Python Advanced Lists
# ==========================================


# 1. Indexing

students = ["Chandan", "Rahul", "Nani", "Amit"]

print("First Student:", students[0])
print("Last Student:", students[-1])


# 2. Slicing

numbers = [10, 20, 30, 40, 50]

print("\nSlicing")
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])


# 3. append()

fruits = ["Apple", "Banana"]

fruits.append("Mango")

print("\nAfter append:", fruits)


# 4. insert()

fruits.insert(1, "Orange")

print("After insert:", fruits)


# 5. extend()

fruits.extend(["Grapes", "Pineapple"])

print("After extend:", fruits)


# 6. remove()

fruits.remove("Banana")

print("After remove:", fruits)


# 7. pop()

removed = fruits.pop(1)

print("After pop:", fruits)
print("Removed Item:", removed)


# 8. count()

numbers = [10, 20, 10, 30, 10]

print("\nCount of 10:", numbers.count(10))


# 9. index()

print("Index of 30:", numbers.index(30))


# 10. sort()

numbers.sort()

print("Sorted:", numbers)


# 11. reverse()

numbers.reverse()

print("Reversed:", numbers)


# 12. Copying Lists

original = [10, 20, 30]

copied = original.copy()

copied.append(40)

print("\nOriginal:", original)
print("Copied:", copied)


# 13. Nested Lists

students = [
    ["Chandan", 85],
    ["Rahul", 90],
    ["Nani", 78]
]

print("\nStudent:", students[0][0])
print("Marks:", students[0][1])









