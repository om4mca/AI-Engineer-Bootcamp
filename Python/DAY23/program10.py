#--------------------------------------------
# AI Engineer Bootcamp
# Day 23
# Program:  Perform array slicing.
# Author: Om Roy
# Date: 29-07-2026
#--------------------------------------------


import numpy as np

# ==========================================
# 1. 1D Array Slicing
# ==========================================
arr_1d = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("--- 1D Slicing ---")
print("Original Array        :", arr_1d)
print("Index 1 to 4 [1:5]    :", arr_1d[1:5])      # [20, 30, 40, 50]
print("First 4 elements [:4] :", arr_1d[:4])       # [10, 20, 30, 40]
print("From index 4 [4:]     :", arr_1d[4:])       # [50, 60, 70, 80]
print("Every 2nd element [::2]:", arr_1d[::2])     # [10, 30, 50, 70]
print("Reversed Array [::-1]  :", arr_1d[::-1])    # [80, 70, 60, 50, 40, 30, 20, 10]


# ==========================================
# 2. 2D Array Slicing
# ==========================================
arr_2d = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("\n--- 2D Slicing ---")
print("Original 2D Array:\n", arr_2d)

# Extract first 2 rows and columns 1 to 2
print("\nFirst 2 rows, cols 1-2 [0:2, 1:3]:\n", arr_2d[0:2, 1:3])

# Extract all rows, only column 0
print("\nFirst column of all rows [:, 0]:", arr_2d[:, 0])

# Extract row 1, all columns
print("Second row [1, :]:", arr_2d[1, :])