#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program:  Student List   marks  > 50   
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------

students = [
    {"name": "Aarav", "marks": 85},
    {"name": "Vihaan", "marks": 42},
    {"name": "Ananya", "marks": 78},
    {"name": "Diya", "marks": 35},
    {"name": "Kabir", "marks": 52}
]


passed_students = [student for student in students if student["marks"] > 50]

print("--- Students with Marks > 50 ---")
for student in passed_students:
    print(f"Name: {student['name']} | Marks: {student['marks']}")