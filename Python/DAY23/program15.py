#--------------------------------------------
# AI Engineer Bootcamp
# Day 23
# Program:  Create a complete Student Marks Analysis using NumPy.
# Author: Om Roy
# Date: 29-07-2026
#--------------------------------------------


import numpy as np

# 1. Dataset Setup
students = np.array(["Rahul", "Priya", "Amit", "Sneha", "Rohan"])
subjects = np.array(["Math", "Physics", "Chemistry", "English"])

# 2D Array: Rows = Students (5), Columns = Subjects (4)
marks = np.array([
    [85, 78, 92, 88],  # Rahul
    [95, 90, 88, 92],  # Priya
    [65, 70, 58, 75],  # Amit
    [88, 92, 95, 90],  # Sneha
    [45, 52, 48, 60]   # Rohan
])

print("====== STUDENT MARKS MATRIX ======")
print("          ", "  ".join(f"{s:>9}" for s in subjects))
for student, mark_row in zip(students, marks):
    print(f"{student:<10}", "  ".join(f"{m:>9}" for m in mark_row))

# ==========================================
# 2. Total & Percentage per Student
# ==========================================
total_marks = np.sum(marks, axis=1)  # Row-wise sum
percentages = (total_marks / 400) * 100

print("\n====== STUDENT PERFORMANCE ======")
for s, t, p in zip(students, total_marks, percentages):
    print(f"{s:<10} | Total Marks: {t}/400 | Percentage: {p:.2f}%")

# ==========================================
# 3. Subject-wise Analysis
# ==========================================
subject_avg = np.mean(marks, axis=0)  # Column-wise mean
subject_max = np.max(marks, axis=0)   # Column-wise max

print("\n====== SUBJECT ANALYSIS ======")
for sub, avg, mx in zip(subjects, subject_avg, subject_max):
    print(f"{sub:<10} | Average: {avg:.2f} | Highest Mark: {mx}")

# ==========================================
# 4. Topper Identification
# ==========================================
top_student_idx = np.argmax(total_marks)
print(f"\n🏆 Class Topper: {students[top_student_idx]} ({percentages[top_student_idx]:.2f}%)")

# ==========================================
# 5. Filtering: Distinction Students (>85% Avg)
# ==========================================
distinction_mask = percentages >= 85.0
print("\n🌟 Distinction Students (>= 85%):", students[distinction_mask])