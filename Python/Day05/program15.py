# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Multiplication Tables (1–10)
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------

print("--- Multiplication Grid (1 to 10) ---\n")

for i in range(1, 11):
    for j in range(1, 11):
        # \t keeps the columns perfectly aligned
        print(f"{i * j}\t", end="")
    print()  # Moves to the next row

#End of the Program