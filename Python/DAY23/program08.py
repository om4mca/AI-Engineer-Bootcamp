#--------------------------------------------
# AI Engineer Bootcamp
# Day 23
# Program:  Access elements using indexing.
# Author: Om Roy
# Date: 29-07-2026
#--------------------------------------------



import numpy as np

# ==========================================
# 1. 1D Array Indexing
# ==========================================
arr_1d = np.array([10, 20, 30, 40, 50])

print("--- 1D Indexing ---")
print("First Element  (index 0)  :", arr_1d[0])   # Output: 10
print("Third Element  (index 2)  :", arr_1d[2])   # Output: 30
print("Last Element   (index -1) :", arr_1d[-1])  # Output: 50 (Negative Indexing)


# ==========================================
# 2. 2D Array Indexing: [row, column]
# ==========================================
arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n--- 2D Indexing ---")
print("Row 0, Col 0 (Top-Left)     :", arr_2d[0, 0])   # Output: 10
print("Row 1, Col 2 (Middle-Right) :", arr_2d[1, 2])   # Output: 60
print("Row 2, Col 1 (Bottom-Mid)   :", arr_2d[2, 1])   # Output: 80
print("Last Row, Last Col          :", arr_2d[-1, -1]) # Output: 90