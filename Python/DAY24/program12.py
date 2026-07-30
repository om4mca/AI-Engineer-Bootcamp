import numpy as np

# 1. Create a 2D array (3 rows x 3 columns)
matrix_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original 2D Matrix:\n", matrix_2d)

# 2. Ravel into 1D (View)
array_1d = matrix_2d.ravel()
print("\nRaveled 1D Array:\n", array_1d)

# 3. Verify that modifying the raveled array alters the original matrix
array_1d[0] = 999
print("\nAfter modifying index 0 of raveled array to 999:")
print("Raveled Array   :", array_1d)
print("Original Matrix (Modified!):\n", matrix_2d)