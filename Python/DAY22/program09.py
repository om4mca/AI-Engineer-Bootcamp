#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program:  Find Patient List of Special Disease
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------

patients = [
    {"id": "P101", "name": "Rajesh", "age": 45, "disease": "Diabetes"},
    {"id": "P102", "name": "Suresh", "age": 52, "disease": "Hypertension"},
    {"id": "P103", "name": "Priya", "age": 34, "disease": "Diabetes"},
    {"id": "P104", "name": "Amit", "age": 29, "disease": "Asthma"},
    {"id": "P105", "name": "Neha", "age": 61, "disease": "Diabetes"}
]

target_disease = "Diabetes"


matching_patients = [
    p for p in patients 
    if p["disease"].lower() == target_disease.lower()
]

print(f"--- Patients diagnosed with '{target_disease}' ---")
for p in matching_patients:
    print(f"ID: {p['id']} | Name: {p['name']} | Age: {p['age']}")