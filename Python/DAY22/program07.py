#--------------------------------------------
# AI Engineer Bootcamp
# Day 22
# Program:  Students average  marks    
# Author: Om Roy
# Date: 28-07-2026
#--------------------------------------------

student_marks = {
    "Aarav": 85,
    "Vihaan": 92,
    "Ananya": 78,
    "Diya": 88,
    "Kabir": 95
}


total_marks = sum(student_marks.values())
num_students = len(student_marks)

# Average Calculation
average = total_marks / num_students

print(f"Total Students: {num_students}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {round(average, 2)}")