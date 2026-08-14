# ==========================================
# Day 11 - Python Functions
# ==========================================


# 1. Simple Function

def welcome():
    print("Welcome to Python Functions")


welcome()


# 2. Function with Parameter

def greet(name):
    print("Hello", name)


greet("Chandan")
greet("Rahul")


# 3. Multiple Parameters

def student_info(name, age, course):
    print("\nStudent Information")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_info("Chandan", 26, "Data Science")


# 4. Function with Return

def add(a, b):
    return a + b


result = add(10, 20)

print("\nAddition:", result)


# 5. Multiple Return Examples

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(20, 10)

print("\nCalculation Results")
print("Addition:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])


# 6. Default Parameter

def welcome_user(name="Guest"):
    print("\nWelcome", name)


welcome_user("Chandan")
welcome_user()


# 7. Function with User Input

def square(number):
    return number * number


num = int(input("\nEnter a number: "))

result = square(num)

print("Square:", result)


# 8. Function with If/Else

def check_result(marks):

    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


marks = float(input("\nEnter marks: "))

result = check_result(marks)

print("Result:", result)