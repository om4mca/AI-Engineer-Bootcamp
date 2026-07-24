#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: functools.wraps
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------

from functools import wraps


def my_decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        return function(*args, **kwargs)

    return wrapper