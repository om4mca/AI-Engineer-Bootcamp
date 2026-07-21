#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: Sort Numbers
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

numbers = [42, 12, 88, 3, 25]

# Ascending order (default)
asc = sorted(numbers)
print(asc)  # [3, 12, 25, 42, 88]

# Descending order
desc = sorted(numbers, reverse=True)
print(desc) # [88, 42, 25, 12, 3]