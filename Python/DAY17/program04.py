#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: Set Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------


# A set of unique hospital departments
departments = {"Cardiology", "Neurology", "Pediatrics", "Oncology"}

# 1. Get the built-in set_iterator
dept_iterator = iter(departments)

print(type(dept_iterator))  # <class 'set_iterator'>

# 2. Extract unique items one-by-one
print(next(dept_iterator))  # Cardiology
print(next(dept_iterator))  # Neurology
print(next(dept_iterator))  # Pediatrics
print(next(dept_iterator))  # Oncology

# Calling next() again raises StopIteration
# print(next(dept_iterator))  # Error: StopIteration