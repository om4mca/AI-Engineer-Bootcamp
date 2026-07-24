
#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: Timing Decorator
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------

import time
from functools import wraps


def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        print(
            f"{function.__name__} took "
            f"{end - start:.4f} seconds"
        )

        return result

    return wrapper


@timer
def calculate_sum():
    total = sum(range(1000000))
    return total


calculate_sum()