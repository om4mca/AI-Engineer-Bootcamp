#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Read Line by Line
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

file = open("student.txt")

for line in file:
    print(line.strip())

file.close()

# end of the program