#--------------------------------------------
# AI Engineer Bootcamp
# Day 21
# Program: Generator + List
# Author: Om Roy
# Date: 27-07-2026
#--------------------------------------------

def count_down(start):
    while start > 0:
        yield start
        start -= 1

# Generate values on demand:
gen = count_down(5)

# Materialize all remaining values into an in-memory list:
numbers_list = list(gen)
print(numbers_list) 