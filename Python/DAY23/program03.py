#--------------------------------------------
# AI Engineer Bootcamp
# Day 23
# Program:  Print ndim.
# Author: Om Roy
# Date: 29-07-2026
#--------------------------------------------

import numpy as np

# 1. 1D Array
arr_1d = np.array([10, 20, 30])

# 2. 2D Array
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 3. 3D Array
arr_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

# Printing ndim for each array
print("1D Array ndim:", arr_1d.ndim)  # Output: 1
print("2D Array ndim:", arr_2d.ndim)  # Output: 2
print("3D Array ndim:", arr_3d.ndim)  # Output: 3