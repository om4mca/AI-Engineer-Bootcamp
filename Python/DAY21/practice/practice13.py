#--------------------------------------------
# AI Engineer Bootcamp
# Day 21
# Program: Decorator + Exception Handling
# Author: Om Roy
# Date: 27-07-2026
#--------------------------------------------

import functools

def safe_execute(default_value=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"⚠️ Exception in '{func.__name__}': {e}. Returning default.")
                return default_value
        return wrapper
    return decorator

@safe_execute(default_value=0)
def parse_int(val):
    return int(val)

print(parse_int("123"))   
print(parse_int("invalid")) 