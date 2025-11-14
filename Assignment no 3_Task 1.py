# ASSIGNMENT 3:
# Module 4: Functions & Modules in Python 

# Task 1: Calculate Factorial Using a Function 
# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.

# factorial using a loop
def factorial(n):
    result=1
    for i in range(1,n+1):
         result*=i
    return result
print(factorial(5)
      
      
)
# factorial using a recursion.
def factorial(n):
     if n==0 or n==1:
          return 1
     else:
         return n*factorial(n-1)
user = int(input("enter a number you want to factorial: "))
print(f"your {user} factorial is {factorial(user)}")     





















# Expected Output:
# For example, if the function is called with 5, it should return:








