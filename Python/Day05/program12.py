
# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Pattern 2
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------

# Outer loop counts down row sizes: 5, 4, 3, 2, 1
for i in range(5, 0, -1):
    # Inner loop prints exactly 'i' stars on the current line
    for j in range(i):
        print("*", end="")
    print()  # Moves to the next line after the row is done


#End of the program