

# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program: Driving License Eligibility
# Author: Om Roy
# Date: 06-07-2026

name = input("Enter your name: ")
age = int(input("Enter your age: "))

minimum_age=18


# Determine eligibility
if age >= minimum_age:
    print(f"Hello {name}, you are ELIGIBLE to apply for a driver's license.")
else:
    years_left = minimum_age - age
    print(f"Sorry {name}, you are NOT eligible. Please apply in {years_left} year(s).")



#End of the program