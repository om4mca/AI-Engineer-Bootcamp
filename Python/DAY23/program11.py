
#--------------------------------------------
# AI Engineer Bootcamp
# Day 23
# Program:  Perform addition of two arrays.
# Author: Om Roy
# Date: 29-07-2026
#--------------------------------------------



import numpy as np

# ==========================================
# 1. 1D Array Addition
# ==========================================
a_1d = np.array([10, 20, 30, 40])
b_1d = np.array([1, 2, 3, 4])

# Method 1: Using '+' operator
sum_1d_op = a_1d + b_1d

# Method 2: Using np.add()
sum_1d_fn = np.add(a_1d, b_1d)

print("--- 1D Array Addition ---")
print("Array A :", a_1d)
print("Array B :", b_1d)
print("Result  :", sum_1d_op)


# ==========================================
# 2. 2D Array Addition (Matrix Addition)
# ==========================================
a_2d = np.array([
    [1, 2],
    [3, 4]
])

b_2d = np.array([
    [10, 20],
    [30, 40]
])

sum_2d = a_2d + b_2d

print("\n--- 2D Array Addition ---")
print("Matrix A:\n", a_2d)
print("Matrix B:\n", b_2d)
print("Sum Matrix:\n", sum_2d)