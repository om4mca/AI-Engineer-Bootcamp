#--------------------------------------------
# AI Engineer Bootcamp
# Day 16
# Program: filter() Age > 18
# Author: Om Roy
# Date: 21-07-2026
#--------------------------------------------

students = [
    {"id": 101, "name": "Om", "age": 42},
    {"id": 102, "name": "Rahul", "age": 15},
    {"id": 103, "name": "Priya", "age": 18},
    {"id": 104, "name": "Amit", "age": 50}
]

students_over_18 = list(filter(lambda p: p["age"] > 18, students))

print(students_over_18)