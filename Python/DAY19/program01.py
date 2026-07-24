#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: Simple Decorator
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------

from functools import wraps

def simple_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        
        # Execute the wrapped function and save its return value
        result = func(*args, **kwargs)
        
        print("After the function runs")
        return result
        
    return wrapper


# Applying the decorator using the @ symbol
@simple_decorator
def greet(name):
    return f"Hello, {name}!"


# Calling the decorated function
message = greet("Om")
print(message)