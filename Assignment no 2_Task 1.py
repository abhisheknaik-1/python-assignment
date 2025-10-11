# ASSIGNMENT 2:
# Module 3: Control Structures in Python
# Task 1: Check if a Number is Even or Odd
# Problem Statement:
# Write a Python program that takes an integer input from the user
# and checks whether the number is even or odd using an if-else statement.
# The program should display the result accordingly.

# 1. Take integer input from user
a = int(input("Enter a number: "))

# 2. Check if number is even or odd
# Using %2 to determine even/odd because even numbers are divisible by 2
if a % 2 == 0:  # ( % )→ remainder operator, ( == )→ checks equality
    print(a, "is an even number.")
else:
    print(a, "is an odd number.")

# 3. Expected Output Example:
# Enter a number: 7
# 7 is an odd number.
