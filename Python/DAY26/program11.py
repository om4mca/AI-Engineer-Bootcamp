import pandas as pd

# Create a Series
s = pd.Series([10, 20, 30, 40, 50])

# Calculate average/mean
series_mean = s.mean()

print("Series:\n", s)
print("-" * 25)
print("Mean (s.mean()):", series_mean)