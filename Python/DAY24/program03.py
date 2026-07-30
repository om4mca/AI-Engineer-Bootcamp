import numpy as np

# 1. 1D Array of 5 elements, filled with 7
full_1d = np.full(5, fill_value=7)

# 2. 2D Array (3 rows, 4 columns), filled with 99
full_2d = np.full((3, 4), fill_value=99)

# 3. 2D Array filled with a float value
full_float = np.full((2, 3), fill_value=3.14)

print("--- 1D Full Array ---")
print(full_1d)

print("\n--- 2D Full Array (Integers) ---")
print(full_2d)

print("\n--- 2D Full Array (Floats) ---")
print(full_float)