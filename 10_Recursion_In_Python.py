#   Topic: Recursion in Python
#   Author: Hamna Munir
#   Description:
#   This file explains recursion, how it works internally,
#   and includes examples of simple, nested, and advanced recursion.
# ============================================================


# ============================================================
#  1. What is Recursion?
# ============================================================
"""
  Definition:
Recursion is a process in which a function calls itself
directly or indirectly to solve a problem.

It breaks down a big problem into smaller subproblems
until it reaches a simple base case.

Every recursive function must have:
    ➤ A Base Case – the stopping condition
    ➤ A Recursive Case – the step where the function calls itself
"""

# Example: Simple recursive function to print numbers

def print_numbers(n):
    if n == 0:   # Base Case
        return
    print(n)
    print_numbers(n - 1)  # Recursive Case

print("Printing numbers using recursion:")
print_numbers(5)
# Output:
# 5
# 4
# 3
# 2
# 1


# ============================================================
#  2. How Recursion Works Internally (Call Stack)
# ============================================================
"""
  Concept:
Each time a recursive function is called, Python pushes a new frame
onto the *call stack*. When the function returns, the frame is popped off.

For example, in print_numbers(3):
    → print_numbers(3)
        → print_numbers(2)
            → print_numbers(1)
                → print_numbers(0)  (base case reached)
Then it unwinds back up the stack.
"""


# ============================================================
#  3. Factorial Using Recursion
# ============================================================
"""
Factorial of n = n × (n-1) × (n-2) × ... × 1
Example: 5! = 5×4×3×2×1 = 120
"""

def factorial(n):
    if n == 0 or n == 1:  # Base Case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive Case

print("\nFactorial of 5 is:", factorial(5))
# Output: 120


# ============================================================
#  4. Fibonacci Series Using Recursion
# ============================================================
"""
Fibonacci Sequence:
0, 1, 1, 2, 3, 5, 8, 13, ...

Formula:
fib(n) = fib(n-1) + fib(n-2)
"""

def fibonacci(n):
    if n <= 1:  # Base Case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci sequence (first 6 numbers):")
for i in range(6):
    print(fibonacci(i), end=" ")
# Output: 0 1 1 2 3 5


# ============================================================
#  5. Sum of Natural Numbers Using Recursion
# ============================================================

def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

print("\n\nSum of first 5 natural numbers:", recursive_sum(5))
# Output: 15


# ============================================================
#  6. Palindrome Check Using Recursion
# ============================================================

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

word = "madam"
print(f"\nIs '{word}' a palindrome?", is_palindrome(word))
# Output: True


# ============================================================
#  7. Reverse a String Using Recursion
# ============================================================

def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])

text = "Hamna"
print("\nReversed string:", reverse_string(text))
# Output: anmaH


# ============================================================
#  8. Nested Recursion
# ============================================================
"""
  Concept:
A recursive function calling itself more than once in the same call.
Example: McCarthy 91 function
"""

def mcCarthy_91(n):
    if n > 100:
        return n - 10
    else:
        return mcCarthy_91(mcCarthy_91(n + 11))

print("\nMcCarthy 91 output for n = 99:", mcCarthy_91(99))
# Output: 91


# ============================================================
#   9. Indirect Recursion
# ============================================================
"""
  Concept:
In indirect recursion, one function calls another, and that function
calls the first one again.
"""

def funcA(n):
    if n > 0:
        print(n)
        funcB(n - 1)

def funcB(n):
    if n > 1:
        print(n)
        funcA(n // 2)

print("\nExample of Indirect Recursion:")
funcA(5)
# Output may vary based on call pattern


# ============================================================
#  10. Tail Recursion
# ============================================================
"""
  Concept:
If the recursive call is the *last* thing executed in the function,
it’s called a Tail Recursive Function.
Python doesn’t optimize tail recursion (unlike some languages),
but it’s a good concept to know.
"""

def tail_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_factorial(n - 1, n * accumulator)

print("\nTail Recursive Factorial of 5:", tail_factorial(5))
# Output: 120


# ============================================================
#  11. Advantages and Disadvantages of Recursion
# ============================================================
"""
  Advantages:
- Elegant and easy to understand for repetitive, tree-like problems
- Reduces code size
- Used in divide-and-conquer algorithms (like QuickSort, MergeSort)

  Disadvantages:
- Consumes more memory (stack frames)
- May cause stack overflow for deep recursion
- Usually slower than iteration
"""


# ============================================================
#  12. Recursion vs Iteration
# ============================================================
"""
| Feature          | Recursion                              | Iteration                        |
|------------------|----------------------------------------|----------------------------------|
| Code Structure   | Function calls itself                  | Uses loops (for/while)           |
| Memory Usage     | High (stack frames)                    | Low                              |
| Speed            | Usually slower                         | Usually faster                   |
| Base Condition   | Required (to stop recursion)            | Loop condition controls exit     |
| Example Use Case | Factorial, Tree Traversal, Fibonacci    | Counting, Repeated tasks         |
"""

# Iterative factorial (for comparison)
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("\nIterative Factorial of 5:", factorial_iterative(5))
# Output: 120


# ============================================================
#  13. Summary
# ============================================================
"""
📘 Summary of Recursion:

1️⃣ Recursion → Function calls itself.
2️⃣ Must have Base Case to avoid infinite recursion.
3️⃣ Uses Call Stack internally.
4️⃣ Common examples: Factorial, Fibonacci, Palindrome.
5️⃣ Indirect & Nested Recursion → Functions call each other or themselves multiple times.
6️⃣ Tail Recursion → Last operation in function is recursive call.
7️⃣ Compare recursion with iteration for efficiency.
"""

# ============================================================
#  END OF FILE
# ============================================================
