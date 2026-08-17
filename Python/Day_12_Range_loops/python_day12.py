# ==========================================
# Day 12 - Python Range and Loop Practice
# ==========================================


# 1. Print numbers from 0 to 4

print("Numbers from 0 to 4")

for i in range(5):
    print(i)


# 2. Print numbers from 1 to 10

print("\nNumbers from 1 to 10")

for i in range(1, 11):
    print(i)


# 3. Print even numbers

print("\nEven Numbers")

for i in range(2, 21, 2):
    print(i)


# 4. Print odd numbers

print("\nOdd Numbers")

for i in range(1, 20, 2):
    print(i)


# 5. Countdown

print("\nCountdown")

for i in range(10, 0, -1):
    print(i)


# 6. Multiplication Table

number = int(input("\nEnter a number for multiplication table: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 7. Sum of numbers

number = int(input("\nEnter a number to calculate sum: "))

total = 0

for i in range(1, number + 1):
    total = total + i

print("Sum:", total)


# 8. Square using Function

def square(number):
    return number * number


print("\nSquares from 1 to 5")

for i in range(1, 6):
    print(i, "=", square(i))


    