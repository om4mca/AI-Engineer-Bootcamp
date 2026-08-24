import numpy as np

# Sample Matrix (5 rows x 3 columns)
matrix = np.array([
    [10, 11, 12],  # Row 0
    [20, 21, 22],  # Row 1
    [30, 31, 32],  # Row 2
    [40, 41, 42],  # Row 3
    [50, 51, 52]   # Row 4
])

# 1. Select consecutive rows (Rows 1 and 2)
middle_rows = matrix[1:3, :]
print("Rows 1 to 2:\n", middle_rows)

# 2. Select first 3 rows (Rows 0, 1, 2)
first_three = matrix[:3, :]
print("First 3 rows:\n", first_three)

# 3. Select last 2 rows (Rows 3, 4)
last_two = matrix[-2:, :]
print("Last 2 rows:\n", last_two)