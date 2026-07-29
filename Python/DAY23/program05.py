#--------------------------------------------
# AI Engineer Bootcamp
# Day 23
# Program:  Print size.
# Author: Om Roy
# Date: 29-07-2026
#--------------------------------------------


import numpy as np

# 1. 1D Array (5 Elements)
arr_1d = np.array([10, 20, 30, 40, 50])

# 2. 2D Array (3 Rows x 4 Columns = 12 Elements)
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# 3. 3D Array (2 Blocks x 2 Rows x 3 Columns = 12 Elements)
arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

# Printing size for each array
print("1D Array Total Size :", arr_1d.size)  # Output: 5
print("2D Array Total Size :", arr_2d.size)  # Output: 12
print("3D Array Total Size :", arr_3d.size)  # Output: 12