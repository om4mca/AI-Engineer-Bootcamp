import pandas as pd

# Create a Series with custom labels
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# 1. Slice from index position 1 to 4 (excludes index 4)
slice_1 = s.iloc[1:4]

# 2. Slice from start up to index position 3 (excludes index 3)
slice_2 = s.iloc[:3]

# 3. Slice using negative indices (last 2 elements)
slice_3 = s.iloc[-2:]

print("Original Series:\n", s)
print("-" * 35)
print("s.iloc[1:4]  (Positions 1, 2, 3):\n", slice_1)
print("\ns.iloc[:3]   (Positions 0, 1, 2):\n", slice_2)
print("\ns.iloc[-2:]  (Last 2 elements):\n", slice_3)