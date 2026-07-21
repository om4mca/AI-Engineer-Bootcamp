#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: reduce() Sum
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

from functools import reduce
numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda x, y: x + y,
    numbers
)

print(total)