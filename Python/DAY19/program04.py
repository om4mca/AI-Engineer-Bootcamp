

#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: Execution Timer
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------


import time
from functools import wraps

def time_it(func):
    """Decorator to measure and display function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Highest precision timer in Python
        
        # Execute target function
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        
        # Format time for readability (ms vs seconds)
        if execution_time < 1.0:
            formatted_time = f"{execution_time * 1000:.2f} ms"
        else:
            formatted_time = f"{execution_time:.4f} sec"
            
        print(f"⏱️ '{func.__name__}' executed in {formatted_time}")
        return result
        
    return wrapper


# --- Execution Examples ---

@time_it
def fast_task():
    """Simulates a fast operation (list processing)."""
    return sum(i * i for i in range(100_000))

@time_it
def heavy_task():
    """Simulates a heavy calculation."""
    return sum(i * i for i in range(10_000_000))

@time_it
def sleeping_task():
    """Simulates an I/O delay."""
    time.sleep(1.2)


print("=== Running Tasks ===")
fast_task()
heavy_task()
sleeping_task()