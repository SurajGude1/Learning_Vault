# ============================================================
# 5. Python Functions
# ============================================================

# -------------------------------
# 5.1 Python Functions (Concept)
# -------------------------------
# A function is a block of reusable code that performs a specific task.
# Why use functions?
# 1. Avoid code repetition.
# 2. Break large programs into smaller, manageable pieces.
# 3. Make code reusable and readable.
# 4. Can return results or perform actions.

# Syntax:
# def function_name(parameters):
#     """docstring (optional)"""
#     body of the function
#     return value (optional)

# Example 1: Simple Function
def greet():
    print("Hello, welcome to Python Functions!")
greet()  # Output: Hello, welcome to Python Functions!

# Example 2: Function with Parameters
def add(a, b):
    return a + b
print(add(5, 3))  # Output: 8

# Example 3: Function with Default Parameters
def introduce(name="User"):
    print("Hello,", name)
introduce()              # Output: Hello, User
introduce("Alice")       # Output: Hello, Alice

# Example 4: Function Returning Multiple Values
def math_operations(a, b):
    return a+b, a-b, a*b, a/b
print(math_operations(10, 2))  # Output: (12, 8, 20, 5.0)

# Example 5: Docstring Example
def square(n):
    """This function returns the square of a number"""
    return n*n
print(square(4))   # Output: 16
print(square.__doc__)  # Output: This function returns the square of a number


# -----------------------------------
# 5.2 Python Built-in Functions
# -----------------------------------
# Python provides many built-in functions to perform common tasks.
# These are pre-defined and can be used directly.
# Categories: Numeric, Type conversion, Iteration, String, etc.

# Example 1: Numeric Functions
print(abs(-10))   # Output: 10
print(pow(2, 3))  # Output: 8

# Example 2: Type Conversion Functions
print(int(3.7))    # Output: 3
print(float("5"))  # Output: 5.0

# Example 3: Iteration Functions
numbers = [1, 2, 3, 4]
print(len(numbers))       # Output: 4
print(sum(numbers))       # Output: 10
print(max(numbers))       # Output: 4
print(min(numbers))       # Output: 1

# Example 4: String Functions
print(chr(65))  # Output: 'A'
print(ord("A")) # Output: 65

# Example 5: Miscellaneous Functions
print(type(5))        # Output: <class 'int'>
print(isinstance(5, int))  # Output: True


# -----------------------------------
# 5.3 Python Lambda Functions
# -----------------------------------
# A lambda function is a small anonymous function defined with 'lambda' keyword.
# Syntax: lambda arguments: expression
# Key points:
# 1. Can have multiple arguments but only one expression.
# 2. Expression is automatically returned.
# 3. Useful for short, simple functions.

# Example 1: Simple Lambda
square = lambda x: x * x
print(square(5))  # Output: 25

# Example 2: Lambda with Two Arguments
add = lambda a, b: a + b
print(add(10, 20))  # Output: 30

# Example 3: Using Lambda in Sorting
data = [(1, "apple"), (3, "banana"), (2, "cherry")]
data.sort(key=lambda x: x[0])
print(data)  # Output: [(1, 'apple'), (2, 'cherry'), (3, 'banana')]

# Example 4: Lambda with filter()
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4, 6]

# Example 5: Lambda with map()
squares = list(map(lambda x: x*x, nums))
print(squares)  # Output: [1, 4, 9, 16, 25, 36]


# -----------------------------------
# 5.4 def Function in Python
# -----------------------------------
# The 'def' keyword is used to define a function in Python.
# Functions defined with def can:
# - Take parameters (optional)
# - Return values (optional)
# - Contain multiple statements

# Example 1: Defining and Calling
def say_hello():
    print("Hello World!")
say_hello()  # Output: Hello World!

# Example 2: Function with Arguments
def multiply(a, b):
    return a * b
print(multiply(4, 5))  # Output: 20

# Example 3: Function with Return Statement
def cube(x):
    return x**3
print(cube(3))  # Output: 27

# Example 4: Nested Functions
def outer():
    def inner():
        return "Inner Function"
    return inner()
print(outer())  # Output: Inner Function

# Example 5: Function with Keyword and Default Arguments
def person_info(name, age=18):
    return f"Name: {name}, Age: {age}"
print(person_info("Alice"))            # Output: Name: Alice, Age: 18
print(person_info("Bob", age=25))      # Output: Name: Bob, Age: 25
