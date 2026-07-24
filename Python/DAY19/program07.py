#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: *args + **kwargs Decorator
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------

def my_decorator(function):

    def wrapper(*args, **kwargs):

        print("Function Started")

        result = function(*args, **kwargs)

        print("Function Finished")

        return result

    return wrapper

@my_decorator
def add(a, b):
    return a + b


print(add(10, 20))