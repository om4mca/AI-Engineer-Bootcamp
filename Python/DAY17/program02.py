#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: Tuple Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------

# A tuple of department names
departments = ("Cardiology", "Neurology", "Pediatrics", "Oncology")

# 1. Get the built-in tuple_iterator
dept_iterator = iter(departments)

print(type(dept_iterator))  # <class 'tuple_iterator'>

# 2. Advance through items step-by-step
print(next(dept_iterator))  
print(next(dept_iterator))  
print(next(dept_iterator))  
print(next(dept_iterator))  

# Calling next() again raises StopIteration
# print(next(dept_iterator))  # Error: StopIteration