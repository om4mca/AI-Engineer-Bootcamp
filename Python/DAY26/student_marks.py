import pandas as pd

# Create the Series
marks = pd.Series(
    [78, 85, 92, 67, 88, 74, 95, 81],
    index=[
        "Amit",
        "Rahul",
        "Priya",
        "Neha",
        "Rohan",
        "Sneha",
        "Ankit",
        "Pooja"
    ]
)

# 1. Display all marks
print("--- 1. All Marks ---")
print(marks)

# 2. Display student names
print("\n--- 2. Student Names ---")
print(list(marks.index))

# 3. Display marks only
print("\n--- 3. Marks Only ---")
print(marks.values)

# Calculations
avg_marks = marks.mean()
max_marks = marks.max()
min_marks = marks.min()
median_marks = marks.median()
std_dev = marks.std()

# Filtering students
above_80 = marks[marks > 80]
below_70 = marks[marks < 70]

# Formatting lists for report
above_80_str = "\n".join([f"- {name}: {score}" for name, score in above_80.items()])
below_70_str = "\n".join([f"- {name}: {score}" for name, score in below_70.items()])

# Generate Report
report = f"""
====== STUDENT MARKS ANALYSIS ======

Total Students: {len(marks)}
Average Marks: {avg_marks:.2f}
Highest Marks: {max_marks}
Lowest Marks: {min_marks}
Median Marks: {median_marks:.2f}
Standard Deviation: {std_dev:.2f}

Students Above 80:
{above_80_str}

Students Below 70:
{below_70_str}
"""

print(report)