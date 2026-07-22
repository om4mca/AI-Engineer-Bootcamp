#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: next() practice
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------

readings = [98.6, 99.1, 100.2]
reading_iter = iter(readings)

print(next(reading_iter, "No more readings available"))  # 98.6
print(next(reading_iter, "No more readings available"))  # 99.1
print(next(reading_iter, "No more readings available"))  # 100.2
print(next(reading_iter, "No more readings available"))  # No more readings available