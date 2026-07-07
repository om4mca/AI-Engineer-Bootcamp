

# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Pattern 1
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------

# Outer loop controls the number of rows (5 rows)
for i in range(1, 6):
    # Inner loop prints the exact number of stars for that row
    for j in range(i):
        print("*", end="")
    print()  # Moves to the next line after finishing a row

#End of the program