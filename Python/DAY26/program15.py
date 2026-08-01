import pandas as pd

# 1. Create a student marks Series with subject labels
marks = pd.Series([85, 92, 78, 65, 90, 88, 45, 98], 
                  index=['Math', 'Science', 'English', 'History', 'Art', 'Physics', 'Chemistry', 'Biology'])

# 2. Generate overall statistical summary
summary = marks.describe()

# 3. Individual key statistics
top_subject = marks.idxmax()
lowest_subject = marks.idxmin()

print("Student Marks Series:\n", marks)
print("=" * 40)
print("STATISTICAL SUMMARY (.describe()):\n", summary)
print("=" * 40)
print(f"Highest Scored Subject : {top_subject} ({marks.max()})")
print(f"Lowest Scored Subject  : {lowest_subject} ({marks.min()})")