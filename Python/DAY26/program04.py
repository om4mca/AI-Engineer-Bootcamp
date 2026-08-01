import pandas as pd

# Create a Series with custom string indexes
marks = pd.Series([85, 92, 78, 90], index=['Math', 'Science', 'English', 'History'])

# Access elements using label-based indexer (.loc)
math_mark    = marks.loc['Math']
science_mark = marks.loc['Science']

print("Series:\n", marks)
print("-" * 30)
print("Mark for Math    (loc['Math'])   :", math_mark)
print("Mark for Science (loc['Science']) :", science_mark)