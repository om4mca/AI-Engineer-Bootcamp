
#--------------------------------------------
# AI Engineer Bootcamp
# Day 23
# Program:  Access elements using negative indexing.
# Author: Om Roy
# Date: 29-07-2026
#--------------------------------------------


import numpy as np

# ==========================================
# 1. 1D Array Negative Indexing
# ==========================================
arr_1d = np.array([10, 20, 30, 40, 50])

print("--- 1D Negative Indexing ---")
print("Array                :", arr_1d)
print("Last element   (-1)  :", arr_1d[-1])  # Output: 50
print("2nd last element (-2):", arr_1d[-2])  # Output: 40
print("First element  (-5)  :", arr_1d[-5])  # Output: 10


# ==========================================
# 2. 2D Array Negative Indexing: [row, col]
# ==========================================
arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n--- 2D Negative Indexing ---")
print("Last row, last column   [-1, -1] :", arr_2d[-1, -1])  # Output: 90
print("First row, last column  [ 0, -1] :", arr_2d[0, -1])   # Output: 30
print("Last row, first column  [-1,  0] :", arr_2d[-1, 0])   # Output: 70
print("2nd last row & column   [-2, -2] :", arr_2d[-2, -2])  # Output: 50