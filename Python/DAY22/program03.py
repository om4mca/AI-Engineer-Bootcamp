#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program: List से odd numbers filter करें।
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Odd numbers filter 
odd_numbers = [num for num in numbers if num % 2 != 0]

print(f"Odd Numbers: {odd_numbers}")
