#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Cube Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

def cube_numbers(limit):

    for number in range(1, limit + 1):
        yield number * number * number


for cube in cube_numbers(5):
    print(cube)