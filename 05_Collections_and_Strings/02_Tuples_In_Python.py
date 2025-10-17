# Topic: Tuples in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

#    What is a Tuple in Python?

# ➤ A Tuple is an ordered, immutable (unchangeable) collection of elements.
# ➤ It can store items of different data types.
# ➤ Tuples are defined using parentheses ().
# ➤ Once created, tuple elements cannot be modified, added, or removed.

# Example:
my_tuple = (10, "AI", 3.14, True)
print(my_tuple)
# Output: (10, 'AI', 3.14, True)


# ----------------------------------------------------------
#   Creating Tuples
# ----------------------------------------------------------

# Empty tuple
empty_tuple = ()
print(empty_tuple)
# Output: ()

# Tuple with integers
numbers = (1, 2, 3, 4, 5)
print(numbers)
# Output: (1, 2, 3, 4, 5)

# Mixed data types
mixed = ("Python", 10, 2.5, False)
print(mixed)
# Output: ('Python', 10, 2.5, False)

# Single element tuple (comma required)
single = (5,)
print(single)
# Output: (5,)


# ----------------------------------------------------------
#   Accessing Tuple Elements
# ----------------------------------------------------------
# ➤ Tuples are indexed like lists.
# ➤ Elements can be accessed using positive or negative indexes.

fruits = ("apple", "banana", "cherry", "mango")
print(fruits[0])    # Output: apple
print(fruits[-1])   # Output: mango
print(fruits[1:3])  # Output: ('banana', 'cherry')


# ----------------------------------------------------------
#   Immutability of Tuples
# ----------------------------------------------------------
# ➤ Tuples cannot be changed after creation.
# ➤ Any attempt to modify a tuple will result in an error.

# Example (will raise an error if uncommented):
# fruits[0] = "grape"  # TypeError: 'tuple' object does not support item assignment


# ----------------------------------------------------------
#   Tuple Operations
# ----------------------------------------------------------
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
result = tuple1 + tuple2
print(result)
# Output: (1, 2, 3, 4, 5)

# Repetition
print(tuple1 * 2)
# Output: (1, 2, 3, 1, 2, 3)

# Membership
print(2 in tuple1)      # Output: True
print(10 not in tuple1) # Output: True


# ----------------------------------------------------------
#   Looping Through a Tuple
# ----------------------------------------------------------
colors = ("red", "green", "blue")

for color in colors:
    print(color)
# Output:
# red
# green
# blue


# ----------------------------------------------------------
#   Tuple Functions
# ----------------------------------------------------------
numbers = (5, 2, 8, 5, 1)

print(len(numbers))   # Output: 5
print(min(numbers))   # Output: 1
print(max(numbers))   # Output: 8
print(numbers.count(5))  # Output: 2
print(numbers.index(8))  # Output: 2


# ----------------------------------------------------------
#   Nested Tuples
# ----------------------------------------------------------
nested = ((1, 2), (3, 4), (5, 6))
print(nested[1])      # Output: (3, 4)
print(nested[1][0])   # Output: 3


# ----------------------------------------------------------
#   Tuple Packing and Unpacking
# ----------------------------------------------------------
# ➤ Packing: Assigning multiple values into one tuple.
# ➤ Unpacking: Extracting tuple elements into individual variables.

# Packing
student = ("Hamna", 20, "AI/ML Student")

# Unpacking
name, age, course = student
print(name)
print(age)
print(course)
# Output:
# Hamna
# 20
# AI/ML Student


# ----------------------------------------------------------
#   Tuples vs Lists
# ----------------------------------------------------------
# | Feature         | List                | Tuple               |
# |-----------------|--------------------|---------------------|
# | Syntax          | [ ]                | ( )                 |
# | Mutability      | Mutable            | Immutable            |
# | Performance     | Slower             | Faster               |
# | Use Case        | Dynamic data       | Fixed/constant data  |

# Example:
list_example = [1, 2, 3]
tuple_example = (1, 2, 3)

list_example[0] = 100   # Works fine
# tuple_example[0] = 100  # Would raise TypeError


# ----------------------------------------------------------
#   When to Use Tuples
# ----------------------------------------------------------
# ✔ When you don’t want data to change (immutability)
# ✔ When you want faster performance
# ✔ When using as keys in dictionaries (tuples are hashable)
# ✔ When returning multiple values from a function


# ----------------------------------------------------------
#   Tuple Inside a Function
# ----------------------------------------------------------
def get_student_info():
    name = "Hamna"
    age = 20
    course = "AI/ML"
    return (name, age, course)  # returning multiple values as a tuple

info = get_student_info()
print(info)
# Output: ('Hamna', 20, 'AI/ML')


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# - Tuples are ordered, immutable collections.
# - Created using parentheses () and can store mixed data types.
# - Faster and memory-efficient compared to lists.
# - Support indexing, slicing, looping, and packing/unpacking.
# - Used for fixed data or as dictionary keys.
# ----------------------------------------------------------
