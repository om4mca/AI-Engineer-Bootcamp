#--------------------------------------------
# AI Engineer Bootcamp
# Day 25
# Program:  Sort an array.
# Author: Om Roy
# Date: 31-07-2026
#--------------------------------------------


import numpy as np

# 1. Sort a 1D Array
arr_1d = np.array([42, 12, 89, 3, 67, 23])

sorted_copy = np.sort(arr_1d)       # Returns a new sorted array
print("Original Array:", arr_1d)
print("Sorted Copy    :", sorted_copy)