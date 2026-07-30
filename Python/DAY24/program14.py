import numpy as np

# 1. Splitting a 1D Array into 3 equal parts
arr_1d = np.array([10, 20, 30, 40, 50, 60])
parts_1d = np.split(arr_1d, 3)

print("--- 1D Array Split into 3 Parts ---")
for i, part in enumerate(parts_1d):
    print(f"Part {i+1}: {part}")

# 2. Creating a 2D Matrix (4 rows x 4 columns)
matrix_2d = np.arange(16).reshape(4, 4)
print("\nOriginal 2D Matrix (4x4):\n", matrix_2d)

# Row-wise / Vertical Split (axis=0) -> Splits 4 rows into 2 sub-matrices (2x4 each)
upper, lower = np.split(matrix_2d, 2, axis=0)

print("\n--- Row-Wise Split (axis=0) ---")
print("Upper Half:\n", upper)
print("Lower Half:\n", lower)

# Column-wise / Horizontal Split (axis=1) -> Splits 4 columns into 2 sub-matrices (4x2 each)
left, right = np.split(matrix_2d, 2, axis=1)

print("\n--- Column-Wise Split (axis=1) ---")
print("Left Half:\n", left)
print("Right Half:\n", right)