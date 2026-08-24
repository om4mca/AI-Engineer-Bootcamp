import numpy as np

# Create a 3x4 matrix (3 rows, 4 columns)
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# Find the shape
dimensions = matrix.shape

print("Matrix shape:", dimensions)  # Output: (3, 4)
print("Number of rows:", dimensions[0])  # Output: 3
print("Number of columns:", dimensions[1])  # Output: 4