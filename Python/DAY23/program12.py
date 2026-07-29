#--------------------------------------------
# AI Engineer Bootcamp
# Day 23
# Program:  Perform multiplication of two arrays.
# Author: Om Roy
# Date: 29-07-2026
#--------------------------------------------



import numpy as np

# ==========================================
# 1. Element-wise Multiplication (*)
# ==========================================
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

elementwise_result = a * b  # or np.multiply(a, b)

print("--- 1D Element-wise Multiplication ---")
print("Array A :", a)
print("Array B :", b)
print("Result  :", elementwise_result)


# ==========================================
# 2. 2D Matrix Multiplication (@ or np.dot)
# ==========================================
m1 = np.array([
    [1, 2],
    [3, 4]
])

m2 = np.array([
    [5, 6],
    [7, 8]
])

# Element-wise: [1*5, 2*6], [3*7, 4*8]
elem_2d = m1 * m2

# Matrix Dot Product (Row x Column)
matrix_dot = m1 @ m2  # or np.dot(m1, m2)

print("\n--- 2D Element-wise (*) vs Dot Product (@) ---")
print("Element-wise Multiplication:\n", elem_2d)
print("\nMatrix Dot Product (@):\n", matrix_dot)