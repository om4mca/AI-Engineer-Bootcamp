#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Square Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

def square_numbers(limit):

    for number in range(1, limit + 1):
        yield number * number


for square in square_numbers(5):
    print(square)