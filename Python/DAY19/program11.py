#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: Logging Decorator
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------

import logging
from functools import wraps

# Configure basic logging to console
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_call(func):
    @wraps(func)  # Preserves the original function's metadata
    def wrapper(*args, **kwargs):
        logging.info(f"Calling '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"'{func.__name__}' returned: {result}")
        return result
    return wrapper

# Usage Example
@log_call
def add_numbers(a, b):
    return a + b

add_numbers(5, 10)
