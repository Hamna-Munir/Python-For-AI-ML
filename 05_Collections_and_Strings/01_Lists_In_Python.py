# Topic: Lists in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

#    What is a List in Python?

# ➤ A List is an ordered, mutable (changeable) collection of items.
# ➤ It can store elements of different data types — integers, strings, floats, etc.
# ➤ Lists are one of the most commonly used data structures in Python.
# ➤ Lists are defined using square brackets [].

# Example:
my_list = [10, "AI", 3.14, True]
print(my_list)
# Output: [10, 'AI', 3.14, True]


# ----------------------------------------------------------
#   Creating Lists
# ----------------------------------------------------------

# Empty list
empty_list = []
print(empty_list)
# Output: []

# List of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)
# Output: [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)
# Output: ['apple', 'banana', 'cherry']

# Mixed data types
mixed = [10, "Python", 3.14, False]
print(mixed)
# Output: [10, 'Python', 3.14, False]


# ----------------------------------------------------------
#   Accessing List Elements
# ----------------------------------------------------------
# ➤ Lists are indexed starting from 0.
# ➤ You can access elements using positive or negative indexes.

fruits = ["apple", "banana", "cherry", "mango"]
print(fruits[0])   # Output: apple
print(fruits[2])   # Output: cherry
print(fruits[-1])  # Output: mango (last element)


# ----------------------------------------------------------
#   Slicing Lists
# ----------------------------------------------------------
# ➤ You can get a subset of elements using slicing [start:end:step]

print(fruits[1:3])    # Output: ['banana', 'cherry']
print(fruits[:2])     # Output: ['apple', 'banana']
print(fruits[::2])    # Output: ['apple', 'cherry']


# ----------------------------------------------------------
#   Modifying Lists
# ----------------------------------------------------------
# ➤ Lists are mutable — you can change their elements.

fruits[1] = "blueberry"
print(fruits)
# Output: ['apple', 'blueberry', 'cherry', 'mango']


# ----------------------------------------------------------
#   Adding Elements to a List
# ----------------------------------------------------------

# Using append() → adds element at the end
fruits.append("orange")
print(fruits)
# Output: ['apple', 'blueberry', 'cherry', 'mango', 'orange']

# Using insert() → adds element at specific index
fruits.insert(2, "grape")
print(fruits)
# Output: ['apple', 'blueberry', 'grape', 'cherry', 'mango', 'orange']

# Using extend() → adds multiple elements from another list
fruits.extend(["kiwi", "melon"])
print(fruits)
# Output: ['apple', 'blueberry', 'grape', 'cherry', 'mango', 'orange', 'kiwi', 'melon']


# ----------------------------------------------------------
#   Removing Elements from a List
# ----------------------------------------------------------

# Using remove() → removes first occurrence of a value
fruits.remove("cherry")
print(fruits)
# Output: ['apple', 'blueberry', 'grape', 'mango', 'orange', 'kiwi', 'melon']

# Using pop() → removes element by index (default: last)
fruits.pop()
print(fruits)
# Output: ['apple', 'blueberry', 'grape', 'mango', 'orange', 'kiwi']

# Using del → deletes by index or entire list
del fruits[0]
print(fruits)
# Output: ['blueberry', 'grape', 'mango', 'orange', 'kiwi']

# Clear entire list
fruits.clear()
print(fruits)
# Output: []


# ----------------------------------------------------------
#   Looping Through a List
# ----------------------------------------------------------
numbers = [1, 2, 3, 4, 5]

# Using for loop
for num in numbers:
    print(num)
# Output:
# 1
# 2
# 3
# 4
# 5


# Using while loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
# Output:
# 1
# 2
# 3
# 4
# 5


# ----------------------------------------------------------
#   List Membership
# ----------------------------------------------------------
# ➤ Use "in" and "not in" to check if an item exists in a list.

numbers = [10, 20, 30, 40]
print(20 in numbers)      # Output: True
print(50 not in numbers)  # Output: True


# ----------------------------------------------------------
#   Useful List Functions and Methods
# ----------------------------------------------------------

numbers = [5, 2, 8, 1, 9]

print(len(numbers))     # Output: 5
print(min(numbers))     # Output: 1
print(max(numbers))     # Output: 9
print(sum(numbers))     # Output: 25

numbers.sort()
print(numbers)
# Output: [1, 2, 5, 8, 9]

numbers.reverse()
print(numbers)
# Output: [9, 8, 5, 2, 1]

# Copying lists
copy_numbers = numbers.copy()
print(copy_numbers)
# Output: [9, 8, 5, 2, 1]


# ----------------------------------------------------------
#   Nested Lists (Lists inside Lists)
# ----------------------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])      # Output: [1, 2, 3]
print(matrix[1][2])   # Output: 6


# ----------------------------------------------------------
#   List Comprehension
# ----------------------------------------------------------
# ➤ A concise way to create lists using a single line.

squares = [x**2 for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# - Lists are ordered, mutable collections.
# - Created using [] and can hold mixed data types.
# - Elements can be added, updated, or removed.
# - Support slicing, looping, and comprehension.
# - Commonly used in data handling, iteration, and ML preprocessing.
# ----------------------------------------------------------
