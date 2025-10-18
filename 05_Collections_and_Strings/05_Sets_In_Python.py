# Topic: Sets in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

# ----------------------------------------------------------
#   What is a Set in Python?
# ----------------------------------------------------------
# ➤ A set is an **unordered**, **mutable**, and **unindexed** collection of **unique elements**.
# ➤ Sets are used to store multiple items in a single variable.
# ➤ They automatically remove duplicate elements.
# ➤ Sets are defined using curly braces `{}` or the `set()` constructor.

# Example:
fruits = {"apple", "banana", "cherry"}
print(fruits)
# Output: {'banana', 'cherry', 'apple'}   (order may vary)

# ----------------------------------------------------------
#   Characteristics of Sets
# ----------------------------------------------------------
# ✔ Unordered – Items have no defined order.
# ✔ Unindexed – No index-based access like lists or tuples.
# ✔ No duplicates – Duplicate values are automatically removed.
# ✔ Mutable – You can add or remove elements after creation.
# ✔ Elements must be immutable (strings, numbers, tuples).

# Example showing automatic duplicate removal:
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)
# Output: {1, 2, 3, 4}

# ----------------------------------------------------------
#   Creating Sets in Python
# ----------------------------------------------------------

# Using curly braces
colors = {"red", "green", "blue"}
print(colors)
# Output: {'green', 'blue', 'red'}

# Using set() constructor
set_from_list = set([1, 2, 3, 4])
print(set_from_list)
# Output: {1, 2, 3, 4}

# Creating an empty set
empty_set = set()
print(type(empty_set))
# Output: <class 'set'>

# ----------------------------------------------------------
#   Accessing Set Elements
# ----------------------------------------------------------
# Since sets are unordered and unindexed, you cannot access elements by index.
# But you can loop through them.

for item in colors:
    print(item)
# Output (order may vary):
# red
# green
# blue

# ----------------------------------------------------------
#   Adding Elements to a Set
# ----------------------------------------------------------

# Add a single element
colors.add("yellow")
print(colors)
# Output: {'green', 'blue', 'yellow', 'red'}

# Add multiple elements using update()
colors.update(["black", "white"])
print(colors)
# Output: {'green', 'blue', 'yellow', 'black', 'white', 'red'}

# ----------------------------------------------------------
#   Removing Elements from a Set
# ----------------------------------------------------------

# Using remove() (raises error if element not found)
colors.remove("white")
print(colors)
# Output: {'green', 'blue', 'yellow', 'black', 'red'}

# Using discard() (no error if element not found)
colors.discard("purple")
print(colors)
# Output: {'green', 'blue', 'yellow', 'black', 'red'}

# Using pop() (removes a random item)
removed_item = colors.pop()
print("Removed:", removed_item)
print(colors)
# Output may vary (since sets are unordered)

# Clear all elements
colors.clear()
print(colors)
# Output: set()

# ----------------------------------------------------------
#   Set Operations
# ----------------------------------------------------------
# Sets are often used for mathematical operations like union, intersection, etc.

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union → combines all elements from both sets (no duplicates)
print(A | B)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection → common elements
print(A & B)
# Output: {4, 5}

# Difference → elements in A but not in B
print(A - B)
# Output: {1, 2, 3}

# Symmetric Difference → elements in A or B but not both
print(A ^ B)
# Output: {1, 2, 3, 6, 7, 8}

# ----------------------------------------------------------
#   Set Methods
# ----------------------------------------------------------
C = {1, 2, 3}
D = {3, 4, 5}

print(C.union(D))              # Output: {1, 2, 3, 4, 5}
print(C.intersection(D))       # Output: {3}
print(C.difference(D))         # Output: {1, 2}
print(C.symmetric_difference(D))  # Output: {1, 2, 4, 5}

# Check subset and superset relationships
print(C.issubset(D))           # Output: False
print(C.issuperset(D))         # Output: False
print(C.isdisjoint(D))         # Output: False

# ----------------------------------------------------------
#   Frozen Sets (Immutable Sets)
# ----------------------------------------------------------
# ➤ A frozenset is like a normal set but **cannot be changed** (immutable).
# ➤ Useful when you need a set that must remain constant (e.g., as a dictionary key).

frozen = frozenset([1, 2, 3])
print(frozen)
# Output: frozenset({1, 2, 3})

# frozen.add(4)  # ❌ This will cause an error because frozensets are immutable.

# ----------------------------------------------------------
#   Summary
# ----------------------------------------------------------
# - Sets are unordered collections of unique items.
# - Mutable: can add or remove items.
# - Supports mathematical operations: union, intersection, difference.
# - Elements must be immutable.
# - Use frozenset() for immutable sets.
# ----------------------------------------------------------
