#  Topic: Variables, Memory Reference, Aliasing, Reference Counting,
#          Garbage Collection, Mutability, and Cloning
#  Author: Hamna Munir
#  Description:
#   This file explains how Python manages variables and memory.
#   It covers how objects are referenced, copied, and deleted.
# ============================================================


# ============================================================
#  1. Variable and Memory Reference
# ============================================================
"""
  Concept:
In Python, variables are *references* to objects in memory,
not containers like in C or Java.

When you write:
    a = 10
You are creating an integer object `10` and the variable `a`
is a reference (label) pointing to that memory location.
"""

a = 10
b = 10
print("a:", a, "b:", b)
print("ID of a:", id(a))
print("ID of b:", id(b))  # same memory location (integer caching)

# Output:
# a: 10 b: 10
# ID of a: 140720... (same as ID of b)


# ============================================================
#  2. Aliasing
# ============================================================
"""
  Concept:
Aliasing means assigning one variable to another.
Both variables refer to the same object in memory.
"""

list1 = [1, 2, 3]
list2 = list1  # list2 is an alias of list1

list2.append(4)

print("list1:", list1)
print("list2:", list2)
print("IDs are same:", id(list1) == id(list2))  # True

# Output:
# list1: [1, 2, 3, 4]
# list2: [1, 2, 3, 4]
# IDs are same: True


# ============================================================
#  3. Reference Counting
# ============================================================
"""
  Concept:
Python uses reference counting to track how many variables
refer to the same object. When the count becomes 0, the object
is automatically deleted from memory.
"""

import sys

x = [10, 20, 30]
print("Reference Count for x:", sys.getrefcount(x))  # +1 for getrefcount call

y = x
z = x
print("After assigning y and z, Reference Count:", sys.getrefcount(x))

del y
print("After deleting y, Reference Count:", sys.getrefcount(x))


# ============================================================
#  4. Garbage Collection
# ============================================================
"""
  Concept:
Garbage Collection is the process of automatically freeing memory
when an object is no longer referenced.
Python’s garbage collector handles cyclic references and unused objects.
"""

import gc

print("\nBefore GC:", gc.collect())  # Manually trigger garbage collection
print("Garbage collection complete  ")


# ============================================================
#  5. Word Stuff (Interning)
# ============================================================
"""
  Concept:
Python optimizes memory for small integers and short strings
through a process called "interning".  
So, identical immutable values may share the same memory address.
"""

s1 = "hello"
s2 = "hello"
print("\ns1 is s2:", s1 is s2)  # True due to string interning

n1 = 256
n2 = 256
print("n1 is n2:", n1 is n2)  # True due to integer caching


# ============================================================
#  6. Mutable vs Immutable Data Types
# ============================================================
"""
  Mutable Objects:
    - Can be changed after creation.
    - Examples: list, dict, set

  Immutable Objects:
    - Cannot be changed after creation.
    - Examples: int, float, str, tuple
"""

# Mutable example:
list_a = [1, 2, 3]
print("\nBefore modification:", list_a)
list_a.append(4)
print("After modification:", list_a)
# Output: [1, 2, 3, 4]

# Immutable example:
str_a = "Hamna"
print("\nBefore modification:", str_a)
str_a = str_a + " Munir"
print("After modification:", str_a)
# Output: Hamna Munir


# ============================================================
#  7. Side Effects of Mutability
# ============================================================
"""
  Concept:
Mutability can cause side effects when multiple references
point to the same mutable object.
"""

original = [1, 2, 3]
alias = original  # Both point to same list

alias.append(99)
print("\nOriginal List:", original)  # Changed too!
print("Alias List:", alias)
# Output: [1, 2, 3, 99] for both


# ============================================================
#  8. Cloning (Copying Objects)
# ============================================================
"""
  Concept:
To avoid side effects, clone (copy) the object.
There are two types of copies:
    - Shallow Copy: Copies object but not nested objects
    - Deep Copy: Copies object and all nested objects
"""

import copy

# Shallow Copy
list_original = [[1, 2], [3, 4]]
list_shallow = copy.copy(list_original)

list_shallow[0][0] = 999
print("\nAfter Shallow Copy Modification:")
print("Original:", list_original)
print("Shallow Copy:", list_shallow)

# Deep Copy
list_original = [[1, 2], [3, 4]]
list_deep = copy.deepcopy(list_original)
list_deep[0][0] = 999

print("\nAfter Deep Copy Modification:")
print("Original:", list_original)
print("Deep Copy:", list_deep)


# ============================================================
#  9. Summary Table
# ============================================================
"""
📘 Summary:

| Concept                 | Description / Example                          |
|--------------------------|-----------------------------------------------|
| Variable Reference       | Variables point to memory locations           |
| Aliasing                 | Two variables refer to same object            |
| Reference Counting       | Tracks number of references to an object      |
| Garbage Collection       | Frees unused memory automatically             |
| Word Stuff (Interning)   | Reuses memory for small strings/ints          |
| Mutable Objects          | list, dict, set                              |
| Immutable Objects        | int, str, tuple                              |
| Side Effects             | Shared mutable data changes everywhere        |
| Cloning                  | Avoid side effects using copy() or deepcopy() |
"""

# ============================================================
#  END OF FILE
# ============================================================
