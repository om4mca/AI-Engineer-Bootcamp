#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: Even Number Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------


class EvenNumberGeneratorIterator:
    """Custom iterator that generates even numbers starting from 0 up to a specified limit."""

    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            even_num = self.current
            self.current += 2  # Skip odd numbers by jumping by 2
            return even_num

        raise StopIteration


class EvenNumberFilterIterator:
    """Custom iterator that filters an existing collection and yields only even numbers."""

    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            num = self.numbers[self.index]
            self.index += 1

            if num % 2 == 0:  # Check for evenness
                return num

        raise StopIteration


# --- Test Executions ---
if __name__ == "__main__":
    print("--- 1. Generating Even Numbers Up To 10 ---")
    generated_evens = EvenNumberGeneratorIterator(limit=10)
    for num in generated_evens:
        print(num, end=" ")
    print()

    print("\n--- 2. Filtering Even Numbers From a List ---")
    raw_list = [13, 22, 4, 15, 8, 9, 30]
    filtered_evens = EvenNumberFilterIterator(raw_list)
    for num in filtered_evens:
        print(num, end=" ")
    print()

