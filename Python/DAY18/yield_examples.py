
#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: yield Example
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

def demo():
    print("Start")
    yield 10

    print("Middle")
    yield 20

    print("End")
    yield 30

result = demo()

print(next(result))
print(next(result))
print(next(result))