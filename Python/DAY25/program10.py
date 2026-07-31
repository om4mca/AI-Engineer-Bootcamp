#--------------------------------------------
# AI Engineer Bootcamp
# Day 25
# Program:  Calculate cumulative product.
# Author: Om Roy
# Date: 31-07-2026
#--------------------------------------------


import numpy as np

# 1. Cumulative Product of a 1D Array
arr_1d = np.array([1, 2, 3, 4, 5])
cumprod_1d = np.cumprod(arr_1d)

print("1D Array:", arr_1d)
print("Cumulative Product:", cumprod_1d)