#--------------------------------------------
# AI Engineer Bootcamp
# Day 23
# Program:  Create a 2D NumPy array.
# Author: Om Roy
# Date: 29-07-2026
#--------------------------------------------

import numpy as np


matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

arr_2d = np.array(matrix_data)


print("====== 2D NUMPY ARRAY (MATRIX) ======")
print("Array Elements:\n", arr_2d)
print("\n--- Properties ---")
print("Dimensions (ndim) :", arr_2d.ndim)   # Output: 2
print("Shape (rows, cols):", arr_2d.shape)  # Output: (3, 3)
print("Total Size        :", arr_2d.size)   # Output: 9
print("Data Type         :", arr_2d.dtype)  # Output: int64