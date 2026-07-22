#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: Custom Counter Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------

class CounterIterator:
    """Custom iterator that generates numbers from `start` to `end` with a specified `step`."""

    def __init__(self, start, end, step=1):
        if step == 0:
            raise ValueError("Step size cannot be zero.")

        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        # Returns the iterator object itself
        return self

    def __next__(self):
        # Stop condition for forward counting (positive step)
        if self.step > 0 and self.current >= self.end:
            raise StopIteration

        # Stop condition for backward counting (negative step)
        if self.step < 0 and self.current <= self.end:
            raise StopIteration

        value = self.current
        self.current += self.step
        return value


# --- Test Executions ---
if __name__ == "__main__":
    print("--- 1. Forward Counter (1 to 5) ---")
    forward_counter = CounterIterator(start=1, end=6, step=1)
    for num in forward_counter:
        print(num, end=" ")
    print()

    print("\n--- 2. Custom Step Counter (10 to 30 by 5) ---")
    step_counter = CounterIterator(start=10, end=31, step=5)
    for num in step_counter:
        print(num, end=" ")
    print()

    print("\n--- 3. Countdown Counter (5 down to 1) ---")
    countdown = CounterIterator(start=5, end=0, step=-1)
    for num in countdown:
        print(num, end=" ")
    print()