#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: Custom Number Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------

class NumberIterator:
    """Custom iterator to traverse numbers with optional filtering and transformation."""

    def __init__(self, numbers, even_only=False, multiply_by=1):
        self.numbers = numbers
        self.even_only = even_only
        self.multiply_by = multiply_by
        self.index = 0

    def __iter__(self):
        # Returns the iterator object itself
        return self

    def __next__(self):
        # Keep scanning until a valid number is found or list ends
        while self.index < len(self.numbers):
            number = self.numbers[self.index]
            self.index += 1

            # If even_only is True, skip odd numbers
            if self.even_only and number % 2 != 0:
                continue

            # Apply transformation on the fly
            return number * self.multiply_by

        # Signal that all numbers have been evaluated
        raise StopIteration


# --- Test Executions ---
if __name__ == "__main__":
    raw_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("--- 1. Iterate Over All Numbers ---")
    all_nums = NumberIterator(raw_numbers)
    for num in all_nums:
        print(num, end=" ")
    print()

    print("\n--- 2. Filter Even Numbers Only ---")
    even_nums = NumberIterator(raw_numbers, even_only=True)
    for num in even_nums:
        print(num, end=" ")
    print()

    print("\n--- 3. Filter Even Numbers & Multiply by 10 ---")
    scaled_evens = NumberIterator(raw_numbers, even_only=True, multiply_by=10)
    for num in scaled_evens:
        print(num, end=" ")
    print()