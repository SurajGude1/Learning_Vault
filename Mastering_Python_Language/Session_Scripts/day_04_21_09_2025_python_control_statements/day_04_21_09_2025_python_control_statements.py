# ============================
# 3. Python Control Statements 
# ============================ 

# ======================================
# 3.1 Python If-Else
# ======================================

# 1. if-else is used to execute code based on conditions.
# 2. The condition must evaluate to True or False.
# 3. elif allows multiple conditions to be checked sequentially.
# 4. Nested if means one if inside another.
# 5. Indentation is mandatory in Python if-else blocks.

# Example 1: Simple If-Else
# age = 18
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible")

# Example 2: If-Elif-Else
# marks = 101
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 60:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# else:
#     print("Invalid entry")

# Example 3: Nested If
# num = 1
# if num >= 0:
#     if num == 0:
#         print("Zero")
#     elif num == 1:
#         print("One")        
#     else:
#         print("Positive")
# else:
#     print("Negative")

# Example 4: Multiple Conditions with 'and'
# salary = 50000
# experience = 3
# if salary > 40000 and experience >= 2:
#     print("Eligible for promotion")
# else:
#     print("Not eligible")
 
# Invalid Scenarios
# if without colon → SyntaxError
# if age >= 18
#     print("Eligible")

# Misleading truthy/falsy check
# if 5:
#     print("Runs because 5 → True")

# if "":
#     print("Does not run because '' → False")


# ---------------------------------------------------------------------------------------------

# ======================================
# 3.2 Python Loops 
# ======================================


# 1. Loops are used to repeat a block of code multiple times.
# 2. Python supports two main types of loops: for loop and while loop.
# 3. for loop → Iterates over sequences (list, tuple, string, range, etc.).
# 4. while loop → Executes as long as a condition is True.
# 5. Loops can be controlled using break, continue, and pass.
# 6. Infinite loops occur if the condition never becomes False.
# 7. Loops improve efficiency by avoiding repeated code writing.


# ---------------------------------------------------------------------------------------------


# ======================================
# 3.3 Python For Loop
# ======================================


# 1. A for loop iterates through each element in a sequence.
# 2. Works with iterables: list, tuple, dictionary, string, set, range().
# 3. Syntax: for variable in sequence:  # block of code
# 4. range() is commonly used to generate sequences of numbers.
# 5. range(start, stop, step) → start is inclusive, stop is exclusive, step defines increment.
# 6. Nested for loops are allowed.
# 7. Non-iterable objects (like int) will raise an error.

# Example 1: Using range(stop)
# for i in range(5):  # 0 to 4
#     print(i)   

# Example 2: Using range(start, stop)
# for i in range(2, 6):  # 2 to 5
#     print(i)

# Example 3: Using range(start, stop, step)
# for i in range(1, 10, 4):  # Odd numbers from 1 to 9
#     print(i)

# for i in range(5, 0, -1):
#     print(i)

# Example 4: Nested For Loops
# for i in range(1, 4):
#     for j in range(1, 3):
#         print(f"i={i}, j={j}")

# Example 5: Comparing Two Strings Character by Character
# str1 = "Python"
# str2 = "Python"

# print(len(str1), len(str2))

# # # Both should be of same length for index-based comparison
# if len(str1) == len(str2):
#     for i in range(len(str1)):
#         if str1[i] == str2[i]:
#             print(f"Position {i}: Match → {str1[i]}")
#         else:
#             print(f"Position {i}: Mismatch → {str1[i]} vs {str2[i]}")
# else:
#     print("Strings are of different lengths, cannot compare fully.")

# Invalid Scenario
# for x in 123:     # TypeError: 'int' object is not iterable
#     print(x)

# Incorrect use of range
# for i in range(1):  # TypeError: range expected at least 1 argument
#     print(i)


# ---------------------------------------------------------------------------------------------


# ======================================
# 3.4 Python While Loop
# ======================================


# 1. A while loop executes a block of code repeatedly as long as a condition is True.
# 2. Syntax:
#       while condition:
#           # block of code
# 3. The condition is checked before each iteration.
# 4. If the condition becomes False, the loop ends.
# 5. Updating loop variables is important to avoid infinite loops.
# 6. While loops are useful when the number of iterations is unknown.

# Example 1: Counting Numbers 1 to 5
# num = 1
# while num <= 5:
#     print(num)
#     num += 1

# Example 2: Printing Even Numbers up to 10
# n = 1
# while n <= 10:
#     print(n)
#     n += 2

# Example 3: Iterating Over a String
# word = "Python"
# index = 0
# while index < len(word):
#     print(word[index])
#     index += 1

# Example 4: Reverse Iteration Over a String
# text = "Hello"
# i = len(text) - 1
# while i >= 0:
#     print(text[i])
#     i -= 1

# text = "Hello"
# length = len(text) - 1
# i = 0
# while i <= length:
#     print(text[i])
#     i += 1    

# Invalid Example 1: Infinite Loop
# count = 1
# while count <= 5:
#     print(count)   # No increment → loop never ends

# Invalid Example 2: Condition False at Start
# x = 10
# while x < 5:
#     print(x)   # Will not run


# ---------------------------------------------------------------------------------------------


# ======================================
# 3.5 Python Continue
# ======================================

# 1. The 'continue' statement skips the current iteration and moves to the next iteration of the loop.
# 2. Useful when certain conditions should be ignored without breaking the loop completely.
# 3. Works with both for loops and while loops.
# 4. Only skips one iteration; loop continues executing further.

# Example 1: Skip printing number 3
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i, end=" ")
    

# Example 2: Print even numbers only
# for i in range(1, 8):
#     if i % 2 != 0:
#         continue
#     print(i)


# Example 3: Skip vowels in a string
# text = "Python"
# for char in text:
#     if char in "aeiouAEIOU":
#         continue
#     print(char)

# Example 4: While loop skipping specific value
# num = 0
# while num < 5:
#     num += 1
#     if num == 2:
#         continue
#     print(num)

# Example 5: If-else inside loop
# for i in range(1, 6):
#     if i == 4:
#         continue
#     else:
#         print("Allowed:", i)

# Invalid Example:
# Using continue outside loop → SyntaxError
# if True:
#     continue   # invalid


# ---------------------------------------------------------------------------------------------


# ======================================
# 3.6 Python Break
# ======================================


# 1. The 'break' statement ends the loop entirely, regardless of the loop condition.
# 2. Once break executes, the loop terminates and control moves to the next statement outside the loop.
# 3. Useful for stopping when a specific condition is met.
# 4. Works in both for and while loops.

# Example 1: Stop loop at number 4
# for i in range(1, 100):
#     if i == 4:
#         break
#     print(i)

# Example 2: Stop at first vowel
# text = "Python"
# for char in text:
#     if char in "aeiouAEIOU":
#         break
#     print(char)

# Example 3: While loop with break
# count = 1
# while count <= 10:
#     if count == 6:
#         break
#     print(count)
#     count += 1

# Example 4: Search character in string
# word = "Programming"
# for c in word:
#     if c == "g":
#         print("Found 'g'")
#         break

# Example 5: If-else with break
# for i in range(1, 6):
#     if i == 3:
#         print("Stopping at 3")
#         break
#     else:
#         print("Running:", i)

# Invalid Example:
# Break outside loop → SyntaxError
# if True:
#     break   # invalid


# ---------------------------------------------------------------------------------------------



# ======================================
# 3.7 Python Pass
# ======================================

# 1. The 'pass' statement does nothing; it is a null operation.
# 2. It is used as a placeholder where a statement is syntactically required but no action is needed.
# 3. Useful for defining empty functions, loops, or conditional blocks temporarily.
# 4. Works in for, while, if-else, functions, classes, and other places where a statement is required.

# Example 1: Empty loop using pass
# for i in range(1, 6):
#     if i % 2 == 0:
#         pass   # do nothing for even numbers
#     else:
#         print(i)

# Example 2: Placeholder function
# def my_function():
#     pass   # function not implemented yet

# Example 3: Empty conditional block
# x = 7
# if x > 5:
#     pass   # nothing happens if condition is true
# else:
#     print("x is 5 or less")

# Example 4: Using pass in a class
# class MyClass:
#     pass   # empty class, can be implemented later

# Example 5: Using pass to skip in nested loops
# for i in range(1, 4):
#     for j in range(1, 4):
#         if i == j:
#             pass   # skip this iteration, do nothing
#         else:
#             print("This is i: ", i, " " + "This is j: ", j)


# ---------------------------------------------------------------------------------------------


# ======================================
# 3.8 Difference between Break and Continue
# ======================================

# 1. 'break' ends the entire loop immediately, whereas 'continue' skips only the current iteration and moves to the next iteration.
# 2. 'break' is used when you want to stop looping completely once a condition is met.
# 3. 'continue' is used when you want to skip some iterations but continue looping.
# 4. Both work in for and while loops.

# Example 1: Using break
# for i in range(1, 6):
#     if i == 3:
#         break   # stop the loop completely
#     print(i)
# Output: 1 2

# Example 2: Using continue
# for i in range(1, 6):
#     if i == 3:
#         continue   # skip only this iteration
#     print(i)
# Output: 1 2 4 5

# Key points:
# - break exits the loop entirely.
# - continue skips the current iteration but the loop continues.
# - Use break to stop early, continue to skip unwanted cases.


# ---------------------------------------------------------------------------------------------


# ======================================
# 3.9 Difference Between For Loop and While Loop in Python
# ======================================

# 1. A 'for' loop is used to iterate over a sequence (like a list, string, or range) for a fixed number of times.
# 2. A 'while' loop runs as long as a condition is true, and is used when the number of iterations is not known beforehand.
# 3. 'for' loop automatically handles the iteration, while 'while' loop requires manual control of the loop variable.
# 4. Both can use 'break', 'continue', and 'pass' statements inside them.

# Example 1: For loop
# for i in range(1, 6):
#     print(i)
# Output: 1 2 3 4 5

# Example 2: While loop
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# Output: 1 2 3 4 5

# Key points:
# - Use 'for' loop when you know the number of iterations or iterate over a sequence.
# - Use 'while' loop when you want to continue until a condition becomes false.


# ---------------------------------------------------------------------------------------------


# ======================================
# 3.10 Control Statements in Python
# ======================================

# 1. Control statements change the normal flow of execution in loops or conditional blocks.
# 2. Python has three main control statements: break, continue, and pass.
# 3. 'break' stops the loop entirely.
# 4. 'continue' skips the current iteration and continues with the next one.
# 5. 'pass' does nothing and acts as a placeholder.

# Example 1: Using break
# for i in range(1, 6):
#     if i == 4:
#         break
#     print(i)
# Output: 1 2 3

# Example 2: Using continue
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)
# Output: 1 2 4 5

# Example 3: Using pass
# for i in range(1, 4):
#     pass   # loop does nothing
# print("Loop finished")
# Output: Loop finished


# ---------------------------------------------------------------------------------------------


# Q1. Write a program to check if a number is positive, negative, or zero.
# Q2. Print all numbers from 1 to 20, but skip multiples of 3.
# Q3. Keep taking input from user until they type "exit".
# Q4. Print characters of a string, but stop if 'x' is found.
# Q5. Use while loop to calculate factorial of a number.
# Q6. Demonstrate pass inside an if condition.
# Q7. Write a loop to print only vowels from a given string.
# Q8. Show difference between break and continue with range(1,10).
# Q9. Compare for and while loops to print first 5 natural numbers.
# Q10. Write a program using if-else to check whether a year is leap year.