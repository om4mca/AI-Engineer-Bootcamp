#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: Hospital Patient Data Processing System
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

patients = [
    {"id": 101, "name": "Om", "age": 42, "bill": 5000},
    {"id": 102, "name": "Rahul", "age": 35, "bill": 7000},
    {"id": 103, "name": "Priya", "age": 28, "bill": 4500},
    {"id": 104, "name": "Amit", "age": 50, "bill": 9000}
]

# Task 1
# Find patients whose age is greater than 40. using filter()
print()
print("******* patients whose age is greater than 40 ***********")
patients_over_40 = list(filter(lambda p: p["age"] > 40, patients))

print(patients_over_40)

# Task 2
# Create a list containing only patient names. using map()
print()
print("******* Create a list containing only patient names ***********")
patient_names = list(map(lambda p: p["name"], patients))

print(patient_names)

# Task 3
# Sort patients by bill amount. using sort()
print()
print("******* Sort patients by bill amount ***********")
patients.sort(
    key=lambda patient: patient["bill"]
)

print(patients)

# Task 4
# Calculate total hospital revenue.. using reduce()
print()
print("***** Total Hospital Revenue ***** ")
from functools import reduce
total_revenue = reduce(lambda acc, p: acc + p["bill"], patients, 0)

print("Total Hospital Revenue:", total_revenue)