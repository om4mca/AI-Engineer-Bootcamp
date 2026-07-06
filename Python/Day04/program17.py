# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program: Marriage Eligibility
# Author: Om Roy
# Date: 06-07-2026
# ------------------------------------------

# Marriage Eligibility Checker
gender = input("Enter gender (M/F): ").strip().upper()
age = int(input("Enter age: "))

if gender == "M":
    if age >= 21: print("Eligible for marriage.")
    else: print("Not eligible (Min age 21 for males).")
elif gender == "F":
    if age >= 18: print("Eligible for marriage.")
    else: print("Not eligible (Min age 18 for females).")
else:
    print("Invalid gender input.")

#End of the program