#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Hospital Patient Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

patients = [
    {"id": 101, "name": "Om", "age": 42},
    {"id": 102, "name": "Rahul", "age": 35},
    {"id": 103, "name": "Priya", "age": 28},
    {"id": 104, "name": "Amit", "age": 50}
]

def patient_generator(patients):

    for patient in patients:
        yield patient

print("--- All Patients ---")
for patient in patient_generator(patients):
    print(patient)        