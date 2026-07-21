#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: Sort Patients by Age
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

patients = [
    {"id": 101, "name": "Om", "age": 42, "bill": 5000},
    {"id": 102, "name": "Rahul", "age": 35, "bill": 7000},
    {"id": 103, "name": "Priya", "age": 28, "bill": 4500},
    {"id": 104, "name": "Amit", "age": 50, "bill": 9000}
]

patients.sort(
    key=lambda patient: patient["age"]
)

print(patients)