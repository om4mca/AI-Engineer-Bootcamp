#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Number Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

def numbers_gen(limit):

    for number in range(1, limit +1  , 1):
        yield number


for number in numbers_gen(20):
    print(number)