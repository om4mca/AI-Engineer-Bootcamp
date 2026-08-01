import pandas as pd

# Create a Series with custom labels
s = pd.Series([45, 12, 89, 34, 67], index=['A', 'B', 'C', 'D', 'E'])

# Find min and max values
min_val = s.min()
max_val = s.max()

# Find the labels corresponding to min and max
min_label = s.idxmin()
max_label = s.idxmax()

print("Series:\n", s)
print("-" * 35)
print("Minimum Value (s.min())     :", min_val)
print("Min Value Index (s.idxmin()):", min_label)
print("\nMaximum Value (s.max())     :", max_val)
print("Max Value Index (s.idxmax()):", max_label)