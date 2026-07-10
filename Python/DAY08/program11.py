#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Factorial Function
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------

def calculate_factorial(n):
    """Calculates factorial of a number using a loop."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    return result

# Example usage:
print(calculate_factorial(5))  # Output: 120
print(calculate_factorial(0))  # Output: 1 (0! is mathematically always 1)


# end of the program