# ==========================================================
# DAY 06 - PYTHON TUPLES
# Data Science Learning Journey
# ==========================================================

print("========== DAY 06 - PYTHON TUPLES ==========\n")

# ----------------------------------------------------------
# 1. Creating Tuples
# ----------------------------------------------------------

print("1. Creating Tuples")

fruits = ("Apple", "Banana", "Orange")

numbers = (10, 20, 30, 40, 50)

student = ("Chandan", 26, 89.5, True)

print(fruits)
print(numbers)
print(student)


# ----------------------------------------------------------
# 2. Tuple Length
# ----------------------------------------------------------

print("\n2. Length")

print(len(fruits))


# ----------------------------------------------------------
# 3. Indexing
# ----------------------------------------------------------

print("\n3. Indexing")

print(fruits[0])
print(fruits[1])
print(fruits[-1])


# ----------------------------------------------------------
# 4. Slicing
# ----------------------------------------------------------

print("\n4. Slicing")

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])


# ----------------------------------------------------------
# 5. Membership
# ----------------------------------------------------------

print("\n5. Membership")

print("Apple" in fruits)
print("Mango" in fruits)


# ----------------------------------------------------------
# 6. Loop Through Tuple
# ----------------------------------------------------------

print("\n6. Loop")

for fruit in fruits:
    print(fruit)


# ----------------------------------------------------------
# 7. count()
# ----------------------------------------------------------

print("\n7. count()")

values = (1,2,2,3,2,4)

print(values.count(2))


# ----------------------------------------------------------
# 8. index()
# ----------------------------------------------------------

print("\n8. index()")

print(fruits.index("Banana"))


# ----------------------------------------------------------
# 9. Packing
# ----------------------------------------------------------

print("\n9. Tuple Packing")

person = ("Chandan",26,"Bengaluru")

print(person)


# ----------------------------------------------------------
# 10. Unpacking
# ----------------------------------------------------------

print("\n10. Tuple Unpacking")

name, age, city = person

print(name)
print(age)
print(city)


# ----------------------------------------------------------
# 11. Nested Tuple
# ----------------------------------------------------------

print("\n11. Nested Tuple")

students = (
    ("Chandan",26),
    ("Rahul",24),
    ("Kiran",25)
)

print(students)

print(students[0])

print(students[1][0])


# ----------------------------------------------------------
# 12. Tuple to List
# ----------------------------------------------------------

print("\n12. Tuple to List")

fruits_list = list(fruits)

print(fruits_list)

fruits_list.append("Kiwi")

print(fruits_list)


# ----------------------------------------------------------
# 13. List to Tuple
# ----------------------------------------------------------

print("\n13. List to Tuple")

new_tuple = tuple(fruits_list)

print(new_tuple)


# ----------------------------------------------------------
# 14. Immutability
# ----------------------------------------------------------

print("\n14. Immutability")

print("Tuples cannot be modified after creation.")


# ----------------------------------------------------------
# 15. Mini Example
# ----------------------------------------------------------

print("\n15. Student Data")

student = ("Chandan",26,92,88,95)

marks = student[2:]

print("Marks :", marks)

print("Highest :", max(marks))

print("Lowest :", min(marks))

print("Average :", sum(marks)/len(marks))


print("\n========== DAY 06 COMPLETED ==========")





