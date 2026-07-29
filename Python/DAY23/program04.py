#--------------------------------------------
# AI Engineer Bootcamp
# Day 23
# Program:  Print shape.
# Author: Om Roy
# Date: 29-07-2026
#--------------------------------------------


import numpy as np

# 1. 1D Array (Vector)
arr_1d = np.array([10, 20, 30, 40, 50])

# 2. 2D Array (3 Rows, 4 Columns)
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# 3. 3D Array (2 Blocks, 2 Rows, 3 Columns)
arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

# Printing shape for each array
print("1D Array Shape :", arr_1d.shape)  # Output: (5,) -> 5 Elements
print("2D Array Shape :", arr_2d.shape)  # Output: (3, 4) -> 3 Rows, 4 Columns
print("3D Array Shape :", arr_3d.shape)  # Output: (2, 2, 3) -> 2 Blocks, 2 Rows, 3 Columns