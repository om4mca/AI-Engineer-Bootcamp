import numpy as np

# 1. 1D Array of 5 zeros
zeros_1d = np.zeros(5)

# 2. 2D Array (3 rows, 4 columns)
zeros_2d = np.zeros((3, 4))

# 3. 2D Array with Integer Data Type (default is float64)
zeros_int = np.zeros((2, 3), dtype=int)

print("--- 1D Zero Array ---")
print(zeros_1d)

print("\n--- 2D Zero Array (Float) ---")
print(zeros_2d)

print("\n--- 2D Zero Array (Integer) ---")
print(zeros_int)