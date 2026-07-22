#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: iter() practice
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------
vitals = [98.6, 120, 80, 95]

# 1. Create iterator
vitals_iter = iter(vitals)

# 2. Manual iteration loop
while True:
    try:
        val = next(vitals_iter)
        print("Reading:", val)
    except StopIteration:
        print("Done iterating!")
        break