import pandas as pd

# Create a Series with custom labels
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# 1. Slice from label 'b' to 'd' (INCLUDES 'd')
slice_1 = s.loc['b':'d']

# 2. Slice from start up to label 'c'
slice_2 = s.loc[:'c']

# 3. Slice from label 'c' to the end
slice_3 = s.loc['c':]

print("Original Series:\n", s)
print("-" * 35)
print("s.loc['b':'d'] (Labels b, c, d):\n", slice_1)
print("\ns.loc[:'c']    (Labels a, b, c):\n", slice_2)
print("\ns.loc['c':]    (Labels c, d, e):\n", slice_3)