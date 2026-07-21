#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: reduce() Product
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Multiply all numbers together using reduce()
product = reduce(lambda acc, x: acc * x, numbers)

print("Product:", product)