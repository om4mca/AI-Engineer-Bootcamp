import numpy as np

# 1. Create a 2D array (3 rows x 3 columns)
matrix_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original 2D Matrix:\n", matrix_2d)

# 2. Flatten into 1D
array_1d = matrix_2d.flatten()
print("\nFlattened 1D Array:\n", array_1d)

# 3. Verify that flatten() created an independent copy
array_1d[0] = 999
print("\nAfter modifying index 0 of flattened array to 999:")
print("Flattened Array :", array_1d)
print("Original Matrix (Unchanged):\n", matrix_2d)