#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: *args Decorator
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------
from functools import wraps

def args_only_decorator(func):
    @wraps(func)
    def wrapper(*args):
        # 1. Action before calling the target function
        print(f"Captured {len(args)} positional argument(s): {args}")
        
        # 2. Pass positional arguments to the original function
        result = func(*args)
        
        # 3. Action after calling the target function
        print("Execution completed.")
        return result
        
    return wrapper


# --- Example Usage ---

@args_only_decorator
def multiply_all(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

@args_only_decorator
def greet(firstname, lastname):
    return f"Hello, {firstname} {lastname}!"


# --- Execution ---

result1 = multiply_all(2, 3, 4, 5)
print(f"Result: {result1}\n")

result2 = greet("Om", "Prakash")
print(f"Result: {result2}")