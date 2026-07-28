#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program:  List Process Dictionary Data
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------

student_data = {
    "Aarav": 85,
    "Vihaan": 92,
    "Ananya": 78,
    "Diya": 88
}


names = list(student_data.keys())
print(f"Names: {names}")


marks = list(student_data.values())
print(f"Marks: {marks}")


pairs = list(student_data.items())
print(f"Pairs: {pairs}")
