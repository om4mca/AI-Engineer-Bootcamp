import numpy as np

# 1. 1D Array of 5 ones
ones_1d = np.ones(5)

# 2. 2D Array (3 rows, 4 columns)
ones_2d = np.ones((3, 4))

# 3. 2D Array with Integer Data Type (default is float64)
ones_int = np.ones((2, 3), dtype=int)

print("--- 1D Ones Array ---")
print(ones_1d)

print("\n--- 2D Ones Array (Float) ---")
print(ones_2d)

print("\n--- 2D Ones Array (Integer) ---")
print(ones_int)