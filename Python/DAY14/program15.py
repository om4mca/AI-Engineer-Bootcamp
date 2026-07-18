#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: ---Doctor Class---
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def add(self, x: float, y: float) -> float:
        """Return the sum of x and y."""
        return x + y

    def subtract(self, x: float, y: float) -> float:
        """Return the difference of x and y."""
        return x - y

    def multiply(self, x: float, y: float) -> float:
        """Return the product of x and y."""
        return x * y

    def divide(self, x: float, y: float) -> float | str:
        """Return the quotient of x and y, handling division by zero."""
        if y == 0:
            return "Error: Cannot divide by zero."
        return x / y

# --- Example Usage ---
# Instantiate the class
calc = Calculator()

# Call the methods
print("Addition (5 + 3):", calc.add(5, 3))         # Output: 8
print("Subtraction (10 - 4):", calc.subtract(10, 4)) # Output: 6
print("Multiplication (4 * 2.5):", calc.multiply(4, 2.5)) # Output: 10.0
print("Division (9 / 3):", calc.divide(9, 3))       # Output: 3.0
print("Division by Zero (5 / 0):", calc.divide(5, 0)) # Output: Error: Cannot divide by zero.
