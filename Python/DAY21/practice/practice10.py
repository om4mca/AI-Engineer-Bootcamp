#--------------------------------------------
# AI Engineer Bootcamp
# Day 21
# Program: Decorator + Function
# Author: Om Roy
# Date: 27-07-2026
#--------------------------------------------

def my_decorator(func):
    def wrapper():
        print("1. Action before original function execution.")
        func()  # Call original function
        print("2. Action after original function execution.")
    return wrapper

def say_hello():
    print("Hello!")

# Manual decorator application:
decorated_hello = my_decorator(say_hello)
decorated_hello()

