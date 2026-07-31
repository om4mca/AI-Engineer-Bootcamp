#--------------------------------------------
# AI Engineer Bootcamp
# Day 25
# Program:  Perform row-wise and column-wise aggregation using axis.
# Author: Om Roy
# Date: 31-07-2026
#--------------------------------------------



import numpy as np

# Sample 2D Matrix (3 rows x 3 columns)
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Matrix:\n", matrix)
print("-" * 40)

# 1. Sum across axes
col_sum = np.sum(matrix, axis=0)  # [10+40+70, 20+50+80, 30+60+90]
row_sum = np.sum(matrix, axis=1)  # [10+20+30, 40+50+60, 70+80+90]

print("Column-wise Sum (axis=0):", col_sum)
print("Row-wise Sum    (axis=1):", row_sum)

# 2. Mean across axes
col_mean = np.mean(matrix, axis=0)
row_mean = np.mean(matrix, axis=1)

print("\nColumn-wise Mean (axis=0):", col_mean)
print("Row-wise Mean    (axis=1):", row_mean)

# 3. Min/Max across axes
col_max = np.max(matrix, axis=0)
row_min = np.min(matrix, axis=1)

print("\nColumn-wise Max (axis=0):", col_max)
print("Row-wise Min    (axis=1):", row_min)