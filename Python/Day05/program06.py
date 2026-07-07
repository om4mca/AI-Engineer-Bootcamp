# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Factorial
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------


import math

number = int(input("Enter Number:- "))

# Ensure the number isn't negative (factorial isn't defined for negative numbers)
if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    result = math.factorial(number)
    print(f"The factorial of {number} is : {result}")


#End of the program