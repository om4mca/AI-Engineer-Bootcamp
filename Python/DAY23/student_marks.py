import numpy as np

# Input Data
marks = np.array([78, 85, 92, 67, 88, 74, 95])

# ======================================================
# NumPy Calculations
# ======================================================

# 1. Total Marks
total_marks = np.sum(marks)

# 2. Average Marks
average_marks = np.mean(marks)

# 3. Highest Marks
highest_marks = np.max(marks)

# 4. Lowest Marks
lowest_marks = np.min(marks)

# 5. Number of Students
total_students = marks.size  # or len(marks) / np.count_nonzero(marks)

# 6. Students Above Average (Boolean Masking)
above_average_count = np.sum(marks > average_marks)

# 7. Students Below Average (Boolean Masking)
below_average_count = np.sum(marks < average_marks)


# ======================================================
# Display Output
# ======================================================

print("====== STUDENT MARKS ANALYSIS ======")
print()
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")
print(f"Total Students: {total_students}")
print(f"Above Average: {above_average_count}")
print(f"Below Average: {below_average_count}")