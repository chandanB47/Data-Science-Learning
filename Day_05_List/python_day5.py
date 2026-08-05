# ==========================================================
# DAY 05 - PYTHON LISTS
# Data Science Learning Journey
# ==========================================================

print("========== DAY 05 - PYTHON LISTS ==========\n")

# ----------------------------------------------------------
# 1. Creating Lists
# ----------------------------------------------------------

print("1. Creating Lists")

fruits = ["Apple", "Banana", "Orange"]

numbers = [10, 20, 30, 40, 50]

student = ["Chandan", 26, 89.5, True]

print("Fruits :", fruits)
print("Numbers:", numbers)
print("Student:", student)


# ----------------------------------------------------------
# 2. Accessing List Elements
# ----------------------------------------------------------

print("\n2. Accessing Elements")

print("First Fruit :", fruits[0])
print("Second Fruit:", fruits[1])
print("Last Fruit  :", fruits[-1])


# ----------------------------------------------------------
# 3. List Slicing
# ----------------------------------------------------------

print("\n3. List Slicing")

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])


# ----------------------------------------------------------
# 4. Updating List
# ----------------------------------------------------------

print("\n4. Updating List")

fruits[1] = "Mango"

print(fruits)


# ----------------------------------------------------------
# 5. append()
# ----------------------------------------------------------

print("\n5. append()")

fruits.append("Kiwi")

print(fruits)


# ----------------------------------------------------------
# 6. insert()
# ----------------------------------------------------------

print("\n6. insert()")

fruits.insert(2, "Grapes")

print(fruits)


# ----------------------------------------------------------
# 7. extend()
# ----------------------------------------------------------

print("\n7. extend()")

more_fruits = ["Pineapple", "Papaya"]

fruits.extend(more_fruits)

print(fruits)


# ----------------------------------------------------------
# 8. remove()
# ----------------------------------------------------------

print("\n8. remove()")

fruits.remove("Apple")

print(fruits)


# ----------------------------------------------------------
# 9. pop()
# ----------------------------------------------------------

print("\n9. pop()")

removed_item = fruits.pop()

print("Removed:", removed_item)

print(fruits)


# ----------------------------------------------------------
# 10. clear()
# ----------------------------------------------------------

print("\n10. clear()")

colors = ["Red", "Blue", "Green"]

print(colors)

colors.clear()

print(colors)


# ----------------------------------------------------------
# 11. count()
# ----------------------------------------------------------

print("\n11. count()")

numbers = [1,2,2,3,2,4,5]

print(numbers.count(2))


# ----------------------------------------------------------
# 12. index()
# ----------------------------------------------------------

print("\n12. index()")

print(fruits.index("Mango"))


# ----------------------------------------------------------
# 13. sort()
# ----------------------------------------------------------

print("\n13. sort()")

marks = [85,65,90,70,95]

marks.sort()

print("Ascending :", marks)

marks.sort(reverse=True)

print("Descending:", marks)


# ----------------------------------------------------------
# 14. reverse()
# ----------------------------------------------------------

print("\n14. reverse()")

marks.reverse()

print(marks)


# ----------------------------------------------------------
# 15. copy()
# ----------------------------------------------------------

print("\n15. copy()")

marks_copy = marks.copy()

print("Original:", marks)

print("Copy    :", marks_copy)


# ----------------------------------------------------------
# 16. Membership Operators
# ----------------------------------------------------------

print("\n16. Membership")

print("Mango" in fruits)

print("Apple" in fruits)

print("Apple" not in fruits)


# ----------------------------------------------------------
# 17. Loop Through List
# ----------------------------------------------------------

print("\n17. Loop")

for fruit in fruits:
    print(fruit)


# ----------------------------------------------------------
# 18. List Length
# ----------------------------------------------------------

print("\n18. Length")

print(len(fruits))


# ----------------------------------------------------------
# 19. Nested List
# ----------------------------------------------------------

print("\n19. Nested List")

student = [

    ["Chandan",26],

    ["Rahul",24],

    ["Kiran",25]

]

print(student)

print(student[0])

print(student[1][0])


# ----------------------------------------------------------
# 20. Mini Example
# ----------------------------------------------------------

print("\n20. Student Marks")

student_marks = [85,72,95,66,88]

print("Marks :", student_marks)

print("Highest:", max(student_marks))

print("Lowest :", min(student_marks))

print("Total  :", sum(student_marks))

print("Average:", sum(student_marks)/len(student_marks))


print("\n========== DAY 05 COMPLETED ==========")





