#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Odd Number Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

def odd_numbers(limit):

    for number in range(1, limit + 1, 2):
        yield number


for number in odd_numbers(20):
    print(number)
