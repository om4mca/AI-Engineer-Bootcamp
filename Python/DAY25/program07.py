#--------------------------------------------
# AI Engineer Bootcamp
# Day 25
# Program:  Find index of minimum using np.argmin().
# Author: Om Roy
# Date: 31-07-2026
#--------------------------------------------




import numpy as np

# 1. Index of Minimum in a 1D Array
arr_1d = np.array([45, 12, 89, 3, 67, 23])
min_index = np.argmin(arr_1d)

print("1D Array:", arr_1d)
print("Minimum Value:", arr_1d[min_index])
print("Index of Minimum Value:", min_index)