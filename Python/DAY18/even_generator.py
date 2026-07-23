
#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Even Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

def even_numbers(limit):

    for number in range(2, limit + 1, 2):
        yield number


for number in even_numbers(20):
    print(number)