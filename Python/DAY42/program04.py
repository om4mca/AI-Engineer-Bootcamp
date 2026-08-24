import numpy as np

# Create a matrix with 3 rows and 5 columns
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
])

# Option 1: Using matrix.shape[1] (Recommended)
col_count = matrix.shape[1]

# Option 2: Using shape on a single row
col_count_row = len(matrix[0])

print("Number of columns:", col_count)  # Output: 5