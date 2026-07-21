#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: filter() Even Numbers
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)