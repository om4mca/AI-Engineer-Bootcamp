#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Range Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

def my_range(start, stop=None, step=1):
    """Generates a sequence of integers like built-in range()."""
    # Handle single argument case: my_range(5) -> my_range(0, 5)
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("my_range() step argument must not be zero")

    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:  # Negative step (counting down)
        while current > stop:
            yield current
            current += step

print("=== Single Argument: my_range(5) ===")
print(list(my_range(5)))            