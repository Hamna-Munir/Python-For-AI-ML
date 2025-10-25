# Topic: Built-in Functions in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

#    What are Built-in Functions?

# ➤ Built-in functions are functions that are already defined in Python.
# ➤ You don’t need to create or import them — they are available by default.
# ➤ They make programming faster and easier by performing common tasks.

# Example:
print("Hello, Hamna!")  # print() is a built-in function
# Output: Hello, Hamna!


# ----------------------------------------------------------
#   Commonly Used Built-in Functions in Python
# ----------------------------------------------------------

# 1. print() → Displays output on the screen
print("Learning Python for AI/ML")
# Output: Learning Python for AI/ML

# 2. input() → Takes user input as a string
# name = input("Enter your name: ")
# print("Welcome,", name)

# 3. len() → Returns the number of items in an object (like string, list, tuple)
text = "Python"
print(len(text))
# Output: 6

# 4. type() → Returns the data type of a variable
x = 10
print(type(x))
# Output: <class 'int'>

# 5. int(), float(), str() → Convert between data types
num_str = "25"
print(int(num_str) + 5)
# Output: 30

# 6. abs() → Returns the absolute (positive) value
print(abs(-15))
# Output: 15

# 7. round() → Rounds a number to the nearest integer or specified decimals
print(round(7.68))
# Output: 8

print(round(7.6874, 2))
# Output: 7.69

# 8. max() and min() → Return the largest and smallest values
numbers = [2, 8, 5, 1, 9]
print(max(numbers))
# Output: 9
print(min(numbers))
# Output: 1

# 9. sum() → Returns the total sum of elements in an iterable
print(sum(numbers))
# Output: 25

# 10. sorted() → Returns a new sorted list
print(sorted(numbers))
# Output: [1, 2, 5, 8, 9]

# 11. range() → Generates a sequence of numbers
for i in range(3):
    print(i)
# Output:
# 0
# 1
# 2

# 12. enumerate() → Returns index and value while looping
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry

# 13. zip() → Combines two or more iterables
names = ["Hamna", "Ali", "Sara"]
scores = [95, 88, 92]
combined = list(zip(names, scores))
print(combined)
# Output: [('Hamna', 95), ('Ali', 88), ('Sara', 92)]

# 14. id() → Returns the unique memory address of an object
a = 10
b = 10
print(id(a), id(b))
# Output: (same memory ID for both since small integers are cached)

# 15. help() → Shows documentation about any function or object
# help(print)  # Uncomment to see the documentation for print()

# ----------------------------------------------------------
#   Math-related Built-in Functions
# ----------------------------------------------------------
import math

print(math.sqrt(25))   # Square root
# Output: 5.0

print(math.pow(2, 3))  # Power (2^3)
# Output: 8.0

print(math.floor(9.8))  # Round down
# Output: 9

print(math.ceil(9.2))   # Round up
# Output: 10

# ----------------------------------------------------------
#   Boolean and Utility Functions
# ----------------------------------------------------------
print(all([True, True, False]))
# Output: False  (because not all values are True)

print(any([True, False, False]))
# Output: True  (because at least one value is True)

print(isinstance(10, int))
# Output: True

print(dir(str))
# Output: Lists all attributes and methods of the str class


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# - Built-in functions are pre-defined and ready to use.
# - They make coding faster and reduce the need for custom code.
# - Common examples include print(), len(), sum(), max(), min(), type(), etc.
# - Python has over 100 built-in functions.
# - You can view them all using the command:
#     >>> print(dir(__builtins__))
# ----------------------------------------------------------
