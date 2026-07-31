#--------------------------------------------
# AI Engineer Bootcamp
# Day 25
# Program:  Find unique values with their frequencies.
# Author: Om Roy
# Date: 31-07-2026
#--------------------------------------------


import numpy as np

# Sample array with duplicate values
arr = np.array(['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'kiwi'])

# Get unique values and their frequencies
values, counts = np.unique(arr, return_counts=True)

print("Original Array:", arr)
print("-" * 30)
print("Unique Values :", values)
print("Frequencies   :", counts)