#--------------------------------------------
# AI Engineer Bootcamp
# Day 18
# Program: Senior Patient Generator
# Author: Om Roy
# Date: 23-07-2026
#--------------------------------------------

patients = [
    {"id": 101, "name": "Om", "age": 42},
    {"id": 102, "name": "Rahul", "age": 35},
    {"id": 103, "name": "Priya", "age": 28},
    {"id": 104, "name": "Amit", "age": 50}
]





def senior_patient_generator(patients):

    for patient in patients:

        if patient["age"] > 40:
            yield patient    



print("\n--- Senior Patients (Age > 40) ---")
for senior in senior_patient_generator(patients):
    print(f"ID: {senior['id']} | Name: {senior['name']} | Age: {senior['age']}")            