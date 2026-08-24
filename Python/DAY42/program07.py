import numpy as np

# Sample Matrix (3 rows x 5 columns)
matrix = np.array([
    [10, 20, 30, 40, 50],  # Row 0
    [11, 21, 31, 41, 51],  # Row 1
    [12, 22, 32, 42, 52]   # Row 2
])

# 1. Select consecutive columns (Columns 1 and 2)
middle_cols = matrix[:, 1:3]
print("Columns 1 to 2:\n", middle_cols)

# 2. Select first 3 columns (Columns 0, 1, 2)
first_three_cols = matrix[:, :3]
print("First 3 columns:\n", first_three_cols)

# 3. Select last 2 columns (Columns 3, 4)
last_two_cols = matrix[:, -2:]
print("Last 2 columns:\n", last_two_cols)