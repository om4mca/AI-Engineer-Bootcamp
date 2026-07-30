import numpy as np

# Initializing student marks array
marks = np.array([
    45, 67, 89, 34, 76,
    92, 55, 38, 81, 70
])

print("=" * 45)
print("       STUDENT MARKS ADVANCED ANALYSIS")
print("=" * 45)

# 1. Display all marks
print("1. All Marks               :", marks)

# 2. Find average marks
avg_marks = np.mean(marks)
print(f"2. Average Marks           : {avg_marks:.2f}")

# 3. Find highest marks
max_marks = np.max(marks)
print("3. Highest Marks           :", max_marks)

# 4. Find lowest marks
min_marks = np.min(marks)
print("4. Lowest Marks            :", min_marks)

# 5. Find students scoring above 75 (Boolean Indexing)
above_75 = marks[marks > 75]
print("5. Marks Above 75          :", above_75)

# 6. Find students scoring below 40 (Boolean Indexing)
below_40 = marks[marks < 40]
print("6. Marks Below 40          :", below_40)

# 7. Count students above average
above_avg_count = np.sum(marks > avg_marks)
print(f"7. Count Above Avg ({avg_marks:.1f})  :", above_avg_count)

# 8. Count students who passed (Pass mark >= 40)
pass_count = np.sum(marks >= 40)
print("8. Count Passed (>= 40)     :", pass_count)

# 9. Reshape marks into 2 x 5 matrix
reshaped_marks = marks.reshape(2, 5)
print("\n9. Reshaped Marks Matrix (2 x 5):\n", reshaped_marks)

# 10. Flatten the reshaped array
flattened_marks = reshaped_marks.flatten()
print("\n10. Flattened Array Back to 1D:", flattened_marks)