#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: String Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------

code = "NARAYAN"

# 1. Get the built-in string iterator
char_iterator = iter(code)

print(type(char_iterator))  # <class 'str_iterator'>

# 2. Extract characters step-by-step
print(next(char_iterator))  
print(next(char_iterator))  
print(next(char_iterator))  
print(next(char_iterator))  
print(next(char_iterator))  
print(next(char_iterator))
print(next(char_iterator))  

# Calling next() again raises StopIteration
# print(next(char_iterator))  # Error: StopIteration