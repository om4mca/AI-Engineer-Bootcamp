#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Count Lines 
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

with open("myfile.txt", "r") as f:
    line_count = sum(1 for line in f)

print(f"Total lines: {line_count}")

# end of the program