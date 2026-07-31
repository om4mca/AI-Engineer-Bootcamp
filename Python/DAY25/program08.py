
#--------------------------------------------
# AI Engineer Bootcamp
# Day 25
# Program:  Find index of maximum using np.argmax().
# Author: Om Roy
# Date: 31-07-2026
#--------------------------------------------



import numpy as np

# 1. Index of Maximum in a 1D Array
arr_1d = np.array([45, 12, 89, 3, 67, 23])
max_index = np.argmax(arr_1d)

print("1D Array:", arr_1d)
print("Maximum Value:", arr_1d[max_index])
print("Index of Maximum Value:", max_index)