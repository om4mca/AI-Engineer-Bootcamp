#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: Custom Range Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------


class CustomRangeIterator:
    """Custom iterator class that replicates Python's built-in range() behavior."""

    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("CustomRangeIterator arg 3 (step) must not be zero")

        # Support range(stop) single-argument signature: range(5) -> 0 to 5
        if stop is None:
            self.stop = start
            self.current = 0
        else:
            self.current = start
            self.stop = stop

        self.step = step

    def __iter__(self):
        # Iterator protocol: returns the iterator object itself
        return self

    def __next__(self):
        # Stop condition for forward stepping (positive step)
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration

        # Stop condition for backward stepping (negative step)
        if self.step < 0 and self.current <= self.stop:
            raise StopIteration

        value = self.current
        self.current += self.step
        return value


# --- Test Executions ---
if __name__ == "__main__":
    print("--- 1. Single Argument: CustomRangeIterator(5) ---")
    for num in CustomRangeIterator(5):
        print(num, end=" ")
    print()

    print("\n--- 2. Start & Stop: CustomRangeIterator(2, 8) ---")
    for num in CustomRangeIterator(2, 8):
        print(num, end=" ")
    print()

    print("\n--- 3. Custom Step Size: CustomRangeIterator(10, 30, 5) ---")
    for num in CustomRangeIterator(10, 30, 5):
        print(num, end=" ")
    print()

    print("\n--- 4. Negative Countdown Step: CustomRangeIterator(10, 0, -2) ---")
    for num in CustomRangeIterator(10, 0, -2):
        print(num, end=" ")
    print()