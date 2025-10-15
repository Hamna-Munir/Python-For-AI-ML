# Topic: Data Types in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

#    What are Data Types in Python?

# ➤ Data types define the kind of value a variable can hold.
# ➤ Python automatically assigns a data type based on the value you assign.
# ➤ Everything in Python is an object, and each object has a type.
# ➤ Common data types include: int, float, str, bool, list, tuple, set, and dict.


# ----------------------------------------------------------
#   1. Numeric Data Types
# ----------------------------------------------------------
# Python supports integers, floating-point numbers, and complex numbers.

# Integer (int)
x = 10
print(x)
print(type(x))
# Output:
# 10
# <class 'int'>

# Float (decimal numbers)
y = 5.75
print(y)
print(type(y))
# Output:
# 5.75
# <class 'float'>

# Complex numbers (a + bj form)
z = 2 + 3j
print(z)
print(type(z))
# Output:
# (2+3j)
# <class 'complex'>


# ----------------------------------------------------------
#   2. String Data Type (str)
# ----------------------------------------------------------
# ➤ A string is a sequence of characters enclosed in single or double quotes.
# ➤ Strings are immutable (cannot be changed after creation).

name = "Hamna Munir"
course = 'AI and Machine Learning'

print(name)
print(course)
print(type(name))
# Output:
# Hamna Munir
# AI and Machine Learning
# <class 'str'>


# ----------------------------------------------------------
#   3. Boolean Data Type (bool)
# ----------------------------------------------------------
# ➤ Boolean represents one of two values: True or False.
# ➤ Often used in conditions and comparisons.

is_student = True
is_graduated = False

print(is_student)
print(is_graduated)
print(type(is_student))
# Output:
# True
# False
# <class 'bool'>


# ----------------------------------------------------------
#   4. List Data Type (list)
# ----------------------------------------------------------
# ➤ A list is an ordered, mutable (changeable) collection of items.
# ➤ It can store multiple data types.

fruits = ["apple", "banana", "mango"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Hamna", 3.5, True]

print(fruits)
print(numbers)
print(mixed)
print(type(fruits))
# Output:
# ['apple', 'banana', 'mango']
# [1, 2, 3, 4, 5]
# [1, 'Hamna', 3.5, True]
# <class 'list'>

# Accessing and modifying list items
print(fruits[0])     # Output: apple
fruits[1] = "orange" # Changing value
print(fruits)        # Output: ['apple', 'orange', 'mango']


# ----------------------------------------------------------
#   5. Tuple Data Type (tuple)
# ----------------------------------------------------------
# ➤ A tuple is an ordered, immutable collection of items.
# ➤ Use parentheses () to define a tuple.

colors = ("red", "green", "blue")
print(colors)
print(type(colors))
# Output:
# ('red', 'green', 'blue')
# <class 'tuple'>

# Accessing tuple items
print(colors[1])
# Output: green


# ----------------------------------------------------------
#   6. Set Data Type (set)
# ----------------------------------------------------------
# ➤ A set is an unordered collection of unique items.
# ➤ It does not allow duplicates and is defined using curly braces {}.

unique_numbers = {1, 2, 3, 3, 4, 5}
print(unique_numbers)
print(type(unique_numbers))
# Output:
# {1, 2, 3, 4, 5}
# <class 'set'>


# ----------------------------------------------------------
#   7. Dictionary Data Type (dict)
# ----------------------------------------------------------
# ➤ A dictionary stores data as key-value pairs.
# ➤ It is mutable and defined using curly braces {}.

student = {
    "name": "Hamna Munir",
    "age": 20,
    "course": "AI/ML"
}

print(student)
print(student["name"])
print(type(student))
# Output:
# {'name': 'Hamna Munir', 'age': 20, 'course': 'AI/ML'}
# Hamna Munir
# <class 'dict'>


# ----------------------------------------------------------
#   8. None Type
# ----------------------------------------------------------
# ➤ The None type represents the absence of a value.
# ➤ It is often used to initialize variables with “no value yet”.

value = None
print(value)
print(type(value))
# Output:
# None
# <class 'NoneType'>


# ----------------------------------------------------------
#   Type Conversion (Type Casting)
# ----------------------------------------------------------
# ➤ Convert one data type to another using int(), float(), str(), list(), etc.

x = 5
y = 3.2
z = "10"

print(float(x))  # Output: 5.0
print(int(y))    # Output: 3
print(int(z))    # Output: 10


# ----------------------------------------------------------
#   Checking Data Type using type()
# ----------------------------------------------------------
# The type() function helps you identify the data type of a variable.

a = 100
b = 45.9
c = "Python"
d = [1, 2, 3]

print(type(a))
print(type(b))
print(type(c))
print(type(d))
# Output:
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'list'>


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# - Python has several built-in data types.
# - Common ones: int, float, str, bool, list, tuple, set, dict, NoneType.
# - Lists and dictionaries are mutable; tuples and strings are immutable.
# - Use type() to check, and casting functions (int(), str(), float(), etc.) to convert.
# ----------------------------------------------------------
