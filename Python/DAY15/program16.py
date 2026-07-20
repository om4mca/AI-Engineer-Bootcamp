#--------------------------------------------
# AI Engineer Bootcamp
# Day 15
# Program: Error handling
# Author: Om Roy
# Date: 20-07-2026
#--------------------------------------------

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")

except ValueError:
    print("⚠️ Invalid input! Please enter a valid integer.")

except ZeroDivisionError:
    print("⚠️ Cannot divide by zero!")