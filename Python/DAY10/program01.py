#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Handle ValueError
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------

try:
    num = int(input("Enter Number: "))
    result = 100 / num
    print(result)

except ValueError:
    print("Invalid number.")


# end of the program    