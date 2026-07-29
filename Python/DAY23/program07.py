
#--------------------------------------------
# AI Engineer Bootcamp
# Day 23
# Program:  Print itemsize.
# Author: Om Roy
# Date: 29-07-2026
#--------------------------------------------


import numpy as np

# 1. 64-bit Float Array (8 bytes per element)
arr_float64 = np.array([1.5, 2.5, 3.5], dtype=np.float64)

# 2. 32-bit Integer Array (4 bytes per element)
arr_int32 = np.array([10, 20, 30], dtype=np.int32)

# 3. 8-bit Integer Array (1 byte per element)
arr_int8 = np.array([1, 2, 3], dtype=np.int8)

# Printing itemsize for each array
print("float64 itemsize :", arr_float64.itemsize, "bytes")  # Output: 8
print("int32 itemsize   :", arr_int32.itemsize, "bytes")    # Output: 4
print("int8 itemsize    :", arr_int8.itemsize, "bytes")     # Output: 1

