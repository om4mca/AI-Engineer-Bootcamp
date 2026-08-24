import numpy as np

# Sample Matrix (3 rows x 3 columns)
matrix = np.array([
    [10, 20, 30],  # Row 0
    [40, 50, 60],  # Row 1
    [70, 80, 90]   # Row 2
])

# 1. Single Element (Row 1, Column 2) -> 60
element = matrix[1, 2]

# 2. Entire Row (Row 0) -> [10, 20, 30]
first_row = matrix[0, :]

# 3. Entire Column (Column 1) -> [20, 50, 80]
middle_col = matrix[:, 1]