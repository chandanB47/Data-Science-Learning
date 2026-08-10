# ============================================================
# DAY 02 - PYTHON NUMBERS & TYPE CASTING
# Data Science Learning
# ============================================================


# ------------------------------------------------------------
# 1. PYTHON NUMERIC DATA TYPES
# ------------------------------------------------------------

# int = whole numbers
age = 26
temperature = -10

# float = decimal numbers
price = 1499.50
percentage = 12.5

# complex = real + imaginary number
complex_number = 3 + 4j

print("----- Numeric Data Types -----")

print(age, type(age))
print(temperature, type(temperature))
print(price, type(price))
print(percentage, type(percentage))
print(complex_number, type(complex_number))


# ------------------------------------------------------------
# 2. ARITHMETIC OPERATORS
# ------------------------------------------------------------

a = 25
b = 4

print("\n----- Arithmetic Operators -----")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# ------------------------------------------------------------
# 3. NORMAL DIVISION VS FLOOR DIVISION
# ------------------------------------------------------------

number1 = 17
number2 = 5

print("\n----- Division -----")

print("Normal Division:", number1 / number2)
print("Floor Division:", number1 // number2)

# /  -> gives normal division result
# // -> gives floor division result


# ------------------------------------------------------------
# 4. MODULUS OPERATOR
# ------------------------------------------------------------

number = 17
divisor = 5

quotient = number // divisor
remainder = number % divisor

print("\n----- Quotient and Remainder -----")

print("Quotient:", quotient)
print("Remainder:", remainder)


# ------------------------------------------------------------
# 5. EXPONENT
# ------------------------------------------------------------

base = 5
power = 2

result = base ** power

print("\n----- Exponent -----")

print("5 power 2:", result)


# ------------------------------------------------------------
# 6. STRING TO INTEGER
# ------------------------------------------------------------

price_text = "1500"

print("\n----- String to Integer -----")

print("Before:", price_text, type(price_text))

price_number = int(price_text)

print("After:", price_number, type(price_number))

total = price_number + 500

print("Total:", total)


# ------------------------------------------------------------
# 7. STRING TO FLOAT
# ------------------------------------------------------------

decimal_text = "249.50"

print("\n----- String to Float -----")

print("Before:", decimal_text, type(decimal_text))

decimal_number = float(decimal_text)

print("After:", decimal_number, type(decimal_number))


# ------------------------------------------------------------
# 8. FLOAT TO INTEGER
# ------------------------------------------------------------

original_price = 999.99

converted_price = int(original_price)

print("\n----- Float to Integer -----")

print("Original:", original_price)
print("Converted:", converted_price)

# int() does NOT round.
# It removes the fractional part.
#
# 999.99 -> 999


# ------------------------------------------------------------
# 9. INTEGER TO FLOAT
# ------------------------------------------------------------

number = 250

float_number = float(number)

print("\n----- Integer to Float -----")

print("Integer:", number, type(number))
print("Float:", float_number, type(float_number))


# ------------------------------------------------------------
# 10. NUMBER TO STRING
# ------------------------------------------------------------

number = 500

number_text = str(number)

print("\n----- Number to String -----")

print("Before:", number, type(number))
print("After:", number_text, type(number_text))


# ------------------------------------------------------------
# 11. MULTIPLE TYPE CONVERSIONS
# ------------------------------------------------------------

number = 250

number_float = float(number)
number_string = str(number_float)

print("\n----- Multiple Conversions -----")

print(number, type(number))
print(number_float, type(number_float))
print(number_string, type(number_string))

# Conversion:
#
# 250
# ↓
# 250.0
# ↓
# "250.0"


# ------------------------------------------------------------
# 12. IMPLICIT TYPE CONVERSION
# ------------------------------------------------------------

integer_number = 10
decimal_number = 2.5

result = integer_number + decimal_number

print("\n----- Implicit Conversion -----")

print("Integer:", integer_number)
print("Float:", decimal_number)
print("Result:", result)
print("Result Type:", type(result))

# Python automatically converts the result to float.


# ------------------------------------------------------------
# 13. EXPLICIT TYPE CONVERSION
# ------------------------------------------------------------

value = "100"

converted_value = int(value)

print("\n----- Explicit Conversion -----")

print("Before:", value, type(value))
print("After:", converted_value, type(converted_value))


# ------------------------------------------------------------
# 14. USER INPUT + NUMERIC CASTING
# ------------------------------------------------------------

print("\n----- User Input -----")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")


# ------------------------------------------------------------
# 15. SIMPLE BILL CALCULATOR
# ------------------------------------------------------------

print("\n----- Bill Calculator -----")

product = input("Enter product name: ")

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Product:", product)
print("Quantity:", quantity)
print(f"Total Bill: ₹{total:.2f}")


# ------------------------------------------------------------
# 16. TEMPERATURE CONVERTER
# ------------------------------------------------------------

print("\n----- Celsius to Fahrenheit -----")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"Celsius: {celsius:.2f}")
print(f"Fahrenheit: {fahrenheit:.2f}")


# ------------------------------------------------------------
# 17. AVERAGE CALCULATOR
# ------------------------------------------------------------

print("\n----- Average Calculator -----")

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
third = float(input("Enter third number: "))

average = (first + second + third) / 3

print(f"Average: {average:.2f}")


# ------------------------------------------------------------
# 18. SALARY + BONUS CALCULATOR
# ------------------------------------------------------------

print("\n----- Salary Calculator -----")

basic_salary = float(input("Enter basic salary: "))
bonus_percentage = float(input("Enter bonus percentage: "))

bonus_amount = basic_salary * bonus_percentage / 100
total_salary = basic_salary + bonus_amount

print(f"Basic Salary: ₹{basic_salary:.2f}")
print(f"Bonus: ₹{bonus_amount:.2f}")
print(f"Total Salary: ₹{total_salary:.2f}")


# ------------------------------------------------------------
# 19. CONVERT SECONDS
# ------------------------------------------------------------

print("\n----- Seconds Converter -----")

total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600

remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60

seconds = remaining_seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)


# ------------------------------------------------------------
# 20. SWAPPING NUMBERS
# ------------------------------------------------------------

a = 10
b = 20

print("\n----- Swap Numbers -----")

print("Before:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After:")
print("a =", a)
print("b =", b)


# ------------------------------------------------------------
# 21. DECIMAL STRING CONVERSION
# ------------------------------------------------------------

value = "250.50"

print("\n----- Decimal String Conversion -----")

# int(value) would fail because "250.50"
# represents a decimal number.

number = float(value)

print("Original:", value, type(value))
print("Converted:", number, type(number))


# ------------------------------------------------------------
# 22. SHOPPING BILL + DISCOUNT
# ------------------------------------------------------------

print("\n----- Shopping Bill -----")

product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
product_quantity = int(input("Enter quantity: "))
discount_percentage = float(input("Enter discount percentage: "))

subtotal = product_price * product_quantity

discount_amount = subtotal * discount_percentage / 100

final_total = subtotal - discount_amount

print("\n----- BILL -----")

print("Product:", product_name)
print("Quantity:", product_quantity)

print(f"Price: ₹{product_price:.2f}")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Discount: ₹{discount_amount:.2f}")
print(f"Final Total: ₹{final_total:.2f}")


