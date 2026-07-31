#--------------------------------------------
# AI Engineer Bootcamp
# Day 25
# Program:  Calculate variance.
# Author: Om Roy
# Date: 31-07-2026
#--------------------------------------------



import numpy as np

# 1. Variance of a 1D Array
arr_1d = np.array([10, 20, 30, 40, 50])
var_1d = np.var(arr_1d)

print("1D Array:", arr_1d)
print("Variance:", var_1d)

# 2. Variance of a 2D Matrix
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

var_overall = np.var(matrix)               # Overall variance
var_columns = np.var(matrix, axis=0)       # Down columns (axis=0)
var_rows    = np.var(matrix, axis=1)       # Across rows (axis=1)

print("\n2D Matrix:\n", matrix)
print("Overall Variance   :", var_overall)
print("Column-wise Variance:", var_columns)
print("Row-wise Variance   :", var_rows)