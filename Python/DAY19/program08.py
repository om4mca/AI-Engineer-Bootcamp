#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: functools.wraps
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------
def my_decorator(func):
    def wrapper(*args, **kwargs):
        """This is the inner wrapper function."""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    """Calculates the sum of two numbers."""
    return a + b

# ❌ Loss of Identity
print(add.__name__)  # Output: wrapper (Expected: 'add')
print(add.__doc__)   # Output: This is the inner wrapper function. (Expected original docstring)