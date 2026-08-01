import pandas as pd

# Create a Series with custom string indexes
marks = pd.Series([85, 92, 78, 90], index=['Math', 'Science', 'English', 'History'])

# Access elements using position-based indexer (.iloc)
first_student  = marks.iloc[0]    # 1st position (Math)
second_student = marks.iloc[1]    # 2nd position (Science)
last_student   = marks.iloc[-1]   # Last position (History)

print("Series:\n", marks)
print("-" * 30)
print("First element (iloc[0]) :", first_student)
print("Second element (iloc[1]):", second_student)
print("Last element (iloc[-1]) :", last_student)