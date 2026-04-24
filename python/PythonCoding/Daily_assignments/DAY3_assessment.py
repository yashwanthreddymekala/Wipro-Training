'''# 1. Largest and smallest numbers in a list
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))

# 2. Length of a string
string_input = input("Enter a string: ")
print("Length of the string:", len(string_input))

# 3. Alphabetical order of a list of names
names = input("Enter a list of names separated by spaces: ").split()
names.sort()
print("Names in alphabetical order:", names)

# 4. Sum of a list of numbers
numbers2 = list(map(int, input("Enter another list of numbers separated by spaces: ").split()))
print("Sum of the numbers:", sum(numbers2))

# 5. String in uppercase
string2 = input("Enter another string: ")
print("Uppercase string:", string2.upper())'''



'''def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#driver
num = int(input("Enter a positive integer: "))

print(f"The factorial of {num} is {factorial(num)}.")'''



'''def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

#driver
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
'''
'''largest = find_largest(num1, num2, num3)
print(f"The largest number is {largest}.")'''



'''
def greet(name):
    print(f"Hello, {name}!")

user_name = input("Enter your name: ")

greet(user_name)'''



'''def average(numbers):
    return sum(numbers) / len(numbers)

#driver
numbers_list = list(map(float, input("Enter numbers separated by spaces: ").split()))

avg = average(numbers_list)
print(f"The average of the numbers is: {avg}")'''


'''
# Define the function to check palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

#driver
# Test the function with different strings
test_strings = ["level", "Hello", "Racecar", "A man a plan a canal Panama"]

for string in test_strings:
    if is_palindrome(string):
        print(f'"{string}" is a palindrome.')
    else:
        print(f'"{string}" is not a palindrome.')'''




'''import math

# 1. Find the square root of a number
num = float(input("Enter a number to find its square root: "))
sqrt_num = math.sqrt(num)
print(f"The square root of {num} is {sqrt_num}")

# 2. Calculate the sine of an angle (in degrees)
angle_deg = float(input("Enter an angle in degrees to find its sine: "))
angle_rad = math.radians(angle_deg)  # Convert degrees to radians
sine_value = math.sin(angle_rad)
print(f"The sine of {angle_deg}° is {sine_value}")

# 3. Find the greatest common divisor (GCD) of two numbers
a = int(input("Enter the first number to find GCD: "))
b = int(input("Enter the second number to find GCD: "))
gcd_value = math.gcd(a, b)
print(f"The GCD of {a} and {b} is {gcd_value}")
'''





'''import random

# 1. Generate and print a random integer between 1 and 100
rand_int = random.randint(1, 100)
print(f"Random integer between 1 and 100: {rand_int}")

# 2. Create a list of 5 random integers between 1 and 50 and print the list
rand_list = [random.randint(1, 50) for _ in range(5)]
print(f"List of random numbers: {rand_list}")

# 3. Shuffle a list of numbers and print the shuffled list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")'''



'''

import datetime

# 1. Get and print the current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# 2. Calculate the number of days between two dates
date1 = datetime.date(2024, 1, 1)  # Example: January 1, 2024
date2 = datetime.date(2024, 4, 24)
delta = date2 - date1
print(f"Number of days between {date1} and {date2}: {delta.days} days")

# 3. Format and print the current date as "DD-MM-YYYY"
formatted_date = current_datetime.strftime("%d-%m-%Y")
print("Formatted current date:", formatted_date)'''



'''
import os

# 1. Print the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# 2. Create a new directory and verify its existence
new_dir = "my_new_directory"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created.")
else:
    print(f"Directory '{new_dir}' already exists.")

# Verify existence
if os.path.exists(new_dir):
    print(f"Verified: '{new_dir}' exists.")

# 3. List all files and directories in the current directory
entries = os.listdir(cwd)
print("Files and directories in the current directory:")
for entry in entries:
    print(entry)'''



'''my_math/
│
├── __init__.py
├── arithmetic.py
└── geometry.py'''


''' arithmetic.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"


# geometry.py
import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width


# main.py
''''''from my_math import add, subtract, multiply, divide, area_circle, area_rectangle

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))

print("Area of circle (radius 3):", area_circle(3))
print("Area of rectangle (length 4, width 6):", area_rectangle(4, 6))

# Arithmetic operations
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))'''
'''
# Geometry calculations
print("Area of circle (radius 3):", area_circle(3))
print("Area of rectangle (length 4, width 6):", area_rectangle(4, 6))
'''



# string_operations.py

def reverse_string(s):
    return s[::-1]

def to_uppercase(s):
    return s.upper()

def string_length(s):
    return len(s)

'''# string_validations.py

def is_palindrome(s):
    s_clean = s.lower().replace(" ", "")  # Ignore case and spaces
    return s_clean == s_clean[::-1]

def is_alpha(s):
    return s.isalpha()

from .string_operations import reverse_string, to_uppercase, string_length
from .string_validations import is_palindrome, is_alpha

__all__ = [
    "reverse_string", "to_uppercase", "string_length",
    "is_palindrome", "is_alpha"
]'''

'''from string_utils import reverse_string, to_uppercase, string_length, is_palindrome, is_alpha

# Sample string
sample = "Racecar"

print(f"Original string: {sample}")
print(f"Reversed string: {reverse_string(sample)}")
print(f"Uppercase string: {to_uppercase(sample)}")
print(f"Length of string: {string_length(sample)}")
print(f"Is palindrome: {is_palindrome(sample)}")
print(f"Contains only alphabetic characters: {is_alpha(sample)}")'''