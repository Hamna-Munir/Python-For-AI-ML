# Topic: Functions in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

# ----------------------------------------------------------
#   What is a Function in Python?
# ----------------------------------------------------------
# ➤ A function is a **block of reusable code** that performs a specific task.
# ➤ Functions help make code **modular, readable, and reusable**.
# ➤ Instead of writing the same code repeatedly, you can define it once and call it multiple times.
# ➤ In Python, functions are created using the `def` keyword.

# ----------------------------------------------------------
#   Syntax:
# ----------------------------------------------------------
# def function_name(parameters):
#     """optional docstring"""
#     # function body
#     return value

# ----------------------------------------------------------
#   Example 1: Basic Function
# ----------------------------------------------------------
def greet():
    print("Hello, welcome to Python programming!")

greet()
# Output: Hello, welcome to Python programming!

# ----------------------------------------------------------
#   Example 2: Function with Parameters
# ----------------------------------------------------------
def greet_user(name):
    print("Hello,", name, "!")
    
greet_user("Hamna")
# Output: Hello, Hamna !

# ----------------------------------------------------------
#   Example 3: Function with Return Statement
# ----------------------------------------------------------
def add(a, b):
    result = a + b
    return result

sum_result = add(10, 20)
print("Sum:", sum_result)
# Output: Sum: 30

# ----------------------------------------------------------
#   Example 4: Function with Default Parameter
# ----------------------------------------------------------
def greet_person(name="User"):
    print("Hi,", name)

greet_person()
# Output: Hi, User

greet_person("Hamna")
# Output: Hi, Hamna

# ----------------------------------------------------------
#   Example 5: Function with Multiple Parameters
# ----------------------------------------------------------
def student_info(name, age, course):
    print(f"Name: {name}, Age: {age}, Course: {course}")

student_info("Hamna", 20, "AI/ML")
# Output: Name: Hamna, Age: 20, Course: AI/ML

# ----------------------------------------------------------
#   Example 6: Returning Multiple Values
# ----------------------------------------------------------
def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return add, sub, mul

x, y, z = calculate(10, 5)
print("Addition:", x)
print("Subtraction:", y)
print("Multiplication:", z)
# Output:
# Addition: 15
# Subtraction: 5
# Multiplication: 50

# ----------------------------------------------------------
#   Example 7: Keyword and Positional Arguments
# ----------------------------------------------------------
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Positional arguments
display_info("Hamna", 20)
# Output: Name: Hamna, Age: 20

# Keyword arguments
display_info(age=20, name="Hamna")
# Output: Name: Hamna, Age: 20

# ----------------------------------------------------------
#   Example 8: Variable-Length Arguments
# ----------------------------------------------------------
# *args → allows multiple positional arguments
# **kwargs → allows multiple keyword arguments

def show_details(*args, **kwargs):
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)

show_details(1, 2, 3, name="Hamna", age=20)
# Output:
# Positional Arguments: (1, 2, 3)
# Keyword Arguments: {'name': 'Hamna', 'age': 20}

# ----------------------------------------------------------
#   Example 9: Nested Functions
# ----------------------------------------------------------
def outer_function():
    print("This is the outer function.")
    
    def inner_function():
        print("This is the inner function.")
    
    inner_function()

outer_function()
# Output:
# This is the outer function.
# This is the inner function.

# ----------------------------------------------------------
#   Example 10: Lambda Functions (Anonymous Functions)
# ----------------------------------------------------------
# ➤ Lambda functions are small, one-line anonymous functions defined using `lambda`.
# ➤ They are used when a simple function is needed temporarily.

square = lambda x: x ** 2
print(square(5))
# Output: 25

add_nums = lambda a, b: a + b
print(add_nums(10, 20))
# Output: 30

# ----------------------------------------------------------
#   Example 11: Docstrings (Documentation Strings)
# ----------------------------------------------------------
# ➤ Docstrings are used to describe what a function does.
# ➤ They are written inside triple quotes as the first line of a function.

def multiply(a, b):
    """This function returns the product of two numbers."""
    return a * b

print(multiply(4, 5))
# Output: 20

print(multiply.__doc__)
# Output: This function returns the product of two numbers.

# ----------------------------------------------------------
#   Example 12: Pass Statement in Functions
# ----------------------------------------------------------
# ➤ The `pass` statement is used as a placeholder for future code.
# ➤ It allows you to define an empty function temporarily.

def future_function():
    pass  # To be implemented later

# ----------------------------------------------------------
#   Summary
# ----------------------------------------------------------
# - Functions organize code into reusable blocks.
# - Defined using `def` keyword.
# - Can take parameters and return values.
# - Default, keyword, *args, and **kwargs make them flexible.
# - Lambda = short anonymous function.
# - Use docstrings for documentation.
# - Pass statement is used as a placeholder.
# ----------------------------------------------------------

