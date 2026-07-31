
#--------------------------------------------
# AI Engineer Bootcamp
# Day 25
# Program:  Find median using np.median().
# Author: Om Roy
# Date: 31-07-2026
#--------------------------------------------


import numpy as np

# 1. Median of a 1D array
arr_1d = np.array([10, 50, 20, 40, 30])  # Sorted: [10, 20, 30, 40, 50]
median_1d = np.median(arr_1d)

print("1D Array:", arr_1d)
print("Median  :", median_1d)