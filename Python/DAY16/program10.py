#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: filter() Odd Numbers
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = list(
    filter(lambda x: x % 2 != 0, numbers)
)

print(odd_numbers)