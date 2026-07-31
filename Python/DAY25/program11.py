#--------------------------------------------
# AI Engineer Bootcamp
# Day 25
# Program:  Calculate 25th, 50th and 75th percentiles.
# Author: Om Roy
# Date: 31-07-2026
#--------------------------------------------


import numpy as np

# Sample dataset
data = np.array([10, 20, 35, 40, 50, 60, 70, 85, 90, 100])

# 1. Calculate individual percentiles
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)  # Same as np.median(data)
q3 = np.percentile(data, 75)

print("Dataset:", data)
print(f"25th Percentile (Q1): {q1}")
print(f"50th Percentile (Q2): {q2}")
print(f"75th Percentile (Q3): {q3}")