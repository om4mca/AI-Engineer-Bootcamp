#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Multiplication Table Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

# 1. Single Number Table Generator
def table_generator(number, count=10):
    """Yields formatted string lines for a multiplication table."""
    for i in range(1, count + 1):
        yield f"{number} x {i:2d} = {number * i}"


# 2. Raw Values Generator (Yields tuples: (number, multiplier, result))
def table_values_generator(number, count=10):
    """Yields raw math data tuples for flexible use."""
    for i in range(1, count + 1):
        yield (number, i, number * i)


# 3. Multi-Table Generator (Multiple tables at once)
def multi_table_generator(start_num, end_num, count=10):
    """Yields tables for a range of numbers."""
    for num in range(start_num, end_num + 1):
        yield num, table_generator(num, count)


# --- Execution Examples ---

print("=== Single Table (Table of 7) ===")
for line in table_generator(7):
    print(line)

print("\n=== One-Liner Table of 5 (Generator Expression) ===")
table_of_5 = (f"5 x {i} = {5 * i}" for i in range(1, 11))
for line in table_of_5:
    print(line)

print("\n=== Multiple Tables (Tables 2 to 4) ===")
for num, table in multi_table_generator(2, 4, count=5):
    print(f"\n--- Table of {num} ---")
    for line in table:
        print(line)