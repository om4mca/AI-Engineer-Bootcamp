import pandas as pd

# Create a Series
s = pd.Series([12, 45, 68, 23, 89, 54, 31], index=['A', 'B', 'C', 'D', 'E', 'F', 'G'])

# Filter values greater than 50
filtered_s = s[s > 50]

print("Original Series:\n", s)
print("-" * 30)
print("Filtered Series (values > 50):\n", filtered_s)