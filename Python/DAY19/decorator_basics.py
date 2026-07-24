#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: Decorator Basic
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------

def my_decorator(function):

    def wrapper():
        print("Before Function")

        function()

        print("After Function")

    return wrapper


def greet():
    print("Hello Om")


decorated_function = my_decorator(greet)

decorated_function()

## @decorator Syntax
@my_decorator
def greet():
    print("Hello Om")

    greet()