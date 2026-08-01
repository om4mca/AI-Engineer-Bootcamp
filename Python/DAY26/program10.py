import pandas as pd

# Create a Series
s = pd.Series([10, 20, 30, 40, 50])

# Calculate total sum
total_sum = s.sum()

print("Series:\n", s)
print("-" * 25)
print("Total Sum (s.sum()):", total_sum)