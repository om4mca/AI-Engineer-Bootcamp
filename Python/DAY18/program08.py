#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Fibonacci Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

def fibonacci(limit):

    a = 0
    b = 1

    for _ in range(limit):
        yield a

        a, b = b, a + b


for number in fibonacci(10):
    print(number)