#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: List Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------

numbers = [10, 20, 30]

# 1. Convert the list (iterable) into a list_iterator
num_iterator = iter(numbers)

print(type(num_iterator))  

# 2. Fetch items manually using next()
print(next(num_iterator))  
print(next(num_iterator))  
print(next(num_iterator))  

# Calling next() again raises StopIteration
# print(next(num_iterator))  # Error: StopIteration