# Topic: Type Conversion and Type Casting in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

#    What is Type Conversion / Type Casting?

# ➤ Type conversion (or type casting) refers to changing the data type of a variable.
# ➤ Python automatically or manually converts one data type into another.
# ➤ It helps in performing operations between different types safely.


# ----------------------------------------------------------
#   1. Implicit Type Conversion (Automatic)
# ----------------------------------------------------------
# ➤ Python automatically converts one data type to another compatible type.
# ➤ Also called “Type Coercion”.

# Example 1: Integer + Float
num_int = 10
num_float = 3.5

result = num_int + num_float  # int automatically converted to float
print(result)
print(type(result))
# Output:
# 13.5
# <class 'float'>

# Example 2: Boolean in numeric operation
x = True  # True = 1, False = 0
y = 5
print(x + y)
print(type(x + y))
# Output:
# 6
# <class 'int'>

# Example 3: Integer + Complex
a = 5
b = 2 + 3j
print(a + b)
print(type(a + b))
# Output:
# (7+3j)
# <class 'complex'>


# ----------------------------------------------------------
#   2. Explicit Type Conversion (Manual)
# ----------------------------------------------------------
# ➤ Done by using built-in functions like int(), float(), str(), bool(), list(), tuple(), set(), etc.
# ➤ The programmer explicitly converts the variable type.

# Example 1: Converting int to float
x = 10
y = float(x)
print(y)
print(type(y))
# Output:
# 10.0
# <class 'float'>

# Example 2: Converting float to int
x = 9.99
y = int(x)
print(y)
print(type(y))
# Output:
# 9
# <class 'int'>

# Example 3: Converting string to int
num_str = "50"
num_int = int(num_str)
print(num_int + 10)
print(type(num_int))
# Output:
# 60
# <class 'int'>

# Example 4: Converting int to string
x = 100
y = str(x)
print(y)
print(type(y))
# Output:
# 100
# <class 'str'>

# Example 5: Converting list to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
# Output:
# (1, 2, 3)
# <class 'tuple'>

# Example 6: Converting tuple to list
my_tuple = (4, 5, 6)
my_list = list(my_tuple)
print(my_list)
print(type(my_list))
# Output:
# [4, 5, 6]
# <class 'list'>

# Example 7: Converting list to set (removes duplicates)
my_list = [1, 2, 2, 3, 4, 4]
my_set = set(my_list)
print(my_set)
print(type(my_set))
# Output:
# {1, 2, 3, 4}
# <class 'set'>

# Example 8: Converting Boolean to int
x = True
y = int(x)
print(y)
print(type(y))
# Output:
# 1
# <class 'int'>

# Example 9: Converting None to string
x = None
y = str(x)
print(y)
print(type(y))
# Output:
# None
# <class 'str'>


# ----------------------------------------------------------
#   3. Invalid Conversions
# ----------------------------------------------------------
# ➤ Some conversions are not allowed and will cause an error.

# Example:
# a = "Hello"
# b = int(a)  # ❌ Error: cannot convert non-numeric string to int
# print(b)


# ----------------------------------------------------------
#   4. Converting Between Collections
# ----------------------------------------------------------
# ➤ You can convert one collection type into another for flexibility.

# String to list
text = "Python"
chars = list(text)
print(chars)
# Output: ['P', 'y', 't', 'h', 'o', 'n']

# List to string
words = ['AI', 'ML', 'Python']
sentence = " ".join(words)
print(sentence)
# Output: AI ML Python

# Dictionary keys and values conversion
student = {"name": "Hamna", "age": 20, "course": "AI/ML"}
keys = list(student.keys())
values = list(student.values())
print(keys)
print(values)
# Output:
# ['name', 'age', 'course']
# ['Hamna', 20, 'AI/ML']


# ----------------------------------------------------------
#   5. Practical Example of Type Casting
# ----------------------------------------------------------
# Example: Reading input (always returns string) and converting it

age = "20"
age = int(age)  # convert string to int
print("Next year your age will be:", age + 1)
# Output:
# Next year your age will be: 21


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# - Type conversion changes one data type into another.
# - Implicit Conversion: Python automatically converts compatible types.
# - Explicit Conversion: Done manually using built-in functions.
# - Not all conversions are possible (e.g., "abc" → int).
# - Common casting functions: int(), float(), str(), bool(), list(), tuple(), set(), dict().
# ----------------------------------------------------------
