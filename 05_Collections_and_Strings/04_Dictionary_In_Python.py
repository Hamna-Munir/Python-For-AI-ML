# Topic: Dictionaries in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

# ----------------------------------------------------------
#   What is a Dictionary in Python?
# ----------------------------------------------------------
# ➤ A dictionary is a collection of **key-value pairs**.
# ➤ It is **unordered**, **mutable**, and **indexed by keys** (not by positions).
# ➤ Each key in a dictionary must be **unique** and **immutable** (like strings, numbers, or tuples).
# ➤ Dictionaries are used to store data values in a structured way.

# Example:
student = {"name": "Hamna", "age": 20, "course": "AI/ML"}
print(student)
# Output: {'name': 'Hamna', 'age': 20, 'course': 'AI/ML'}

# ----------------------------------------------------------
#   Accessing Dictionary Values
# ----------------------------------------------------------

# Using key names
print(student["name"])   # Output: Hamna
print(student["age"])    # Output: 20

# Using get() method (safe way — avoids errors if key doesn’t exist)
print(student.get("course"))   # Output: AI/ML
print(student.get("grade", "Not Found"))  # Output: Not Found

# ----------------------------------------------------------
#   Adding and Updating Dictionary Items
# ----------------------------------------------------------

# Add a new key-value pair
student["grade"] = "A"
print(student)
# Output: {'name': 'Hamna', 'age': 20, 'course': 'AI/ML', 'grade': 'A'}

# Update an existing value
student["age"] = 21
print(student)
# Output: {'name': 'Hamna', 'age': 21, 'course': 'AI/ML', 'grade': 'A'}

# ----------------------------------------------------------
#   Removing Items from a Dictionary
# ----------------------------------------------------------

# Using pop() method (removes specific key)
student.pop("grade")
print(student)
# Output: {'name': 'Hamna', 'age': 21, 'course': 'AI/ML'}

# Using popitem() (removes the last inserted item)
student.popitem()
print(student)
# Output: {'name': 'Hamna', 'age': 21}

# Using del keyword
del student["age"]
print(student)
# Output: {'name': 'Hamna'}

# Using clear() method (removes all items)
student.clear()
print(student)
# Output: {}

# ----------------------------------------------------------
#   Creating Dictionary using dict() Constructor
# ----------------------------------------------------------

info = dict(name="Hamna", age=20, field="Machine Learning")
print(info)
# Output: {'name': 'Hamna', 'age': 20, 'field': 'Machine Learning'}

# ----------------------------------------------------------
#   Nested Dictionaries
# ----------------------------------------------------------

students = {
    "student1": {"name": "Hamna", "age": 20},
    "student2": {"name": "Ayesha", "age": 22}
}

print(students["student1"]["name"])  
# Output: Hamna

print(students["student2"]["age"])   
# Output: 22

# ----------------------------------------------------------
#   Dictionary Methods
# ----------------------------------------------------------

person = {"name": "Hamna", "age": 20, "city": "Faisalabad"}

print(person.keys())     # Output: dict_keys(['name', 'age', 'city'])
print(person.values())   # Output: dict_values(['Hamna', 20, 'Faisalabad'])
print(person.items())    # Output: dict_items([('name', 'Hamna'), ('age', 20), ('city', 'Faisalabad')])

# Copying a dictionary
copy_person = person.copy()
print(copy_person)
# Output: {'name': 'Hamna', 'age': 20, 'city': 'Faisalabad'}

# ----------------------------------------------------------
#   Looping Through a Dictionary
# ----------------------------------------------------------

for key in person:
    print(key, ":", person[key])
# Output:
# name : Hamna
# age : 20
# city : Faisalabad

# ----------------------------------------------------------
#   Dictionary Comprehension
# ----------------------------------------------------------

squares = {x: x**2 for x in range(1, 6)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ----------------------------------------------------------
#   Summary
# ----------------------------------------------------------
# - Dictionary = key-value pairs.
# - Keys must be unique and immutable.
# - Supports operations: add, update, delete, and access by key.
# - Common methods: keys(), values(), items(), pop(), clear(), copy().
# - Can store nested data structures.
# - Excellent for structured or JSON-like data handling.
# ----------------------------------------------------------
