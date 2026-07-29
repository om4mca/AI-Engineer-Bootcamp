#--------------------------------------------
# AI Engineer Bootcamp
# Day 23
# Program:  Print dtype.
# Author: Om Roy
# Date: 29-07-2026
#--------------------------------------------


import numpy as np

# 1. Integer Array
arr_int = np.array([10, 20, 30, 40])

# 2. Float Array
arr_float = np.array([1.5, 2.8, 3.14])

# 3. String Array
arr_str = np.array(["Python", "NumPy", "Pandas"])

# 4. Custom Explicit Data Type (e.g., int32)
arr_custom = np.array([1, 2, 3], dtype=np.int32)

# Printing dtype for each array
print("Integer Array dtype :", arr_int.dtype)     # Output: int64 (or int32 depending on OS)
print("Float Array dtype   :", arr_float.dtype)   # Output: float64
print("String Array dtype  :", arr_str.dtype)     # Output: <U6 (Unicode String)
print("Custom Array dtype  :", arr_custom.dtype)  # Output: int32