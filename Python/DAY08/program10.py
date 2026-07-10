#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Function for Maximum Number
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------

def find_max_of_two(num1, num2):
    """Returns the larger of two numbers."""
    if num1 > num2:
        return num1
    else:
        return num2

# Example Usage:
largest = find_max_of_two(14, 27)
print(f"The maximum number is: {largest}")  
# Output: The maximum number is: 27

# end of the program