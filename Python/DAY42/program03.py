import numpy as np

# Create a matrix with 4 rows and 2 columns
matrix = np.array([
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80]
])

# Option 1: Using matrix.shape[0] (Recommended)
row_count = matrix.shape[0]

# Option 2: Using len()
len_count = len(matrix)

print("Number of rows:", row_count)  # Output: 4