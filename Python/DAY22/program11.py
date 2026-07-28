#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program:  Missing/empty values identify
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------

patients = [
    {"id": "P101", "name": "Rajesh", "age": 45},
    {"id": "P102", "name": "Suresh", "age": None},     
    {"id": "P103", "name": "", "age": 34},            
    {"id": "P104", "name": "Amit"}                     
]

# Missing or None fields ढूँढें
incomplete_records = [
    p for p in patients 
    if not p.get("name") or p.get("age") is None
]

print("Incomplete Patient Records:")
for p in incomplete_records:
    print(p)