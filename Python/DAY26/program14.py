import pandas as pd

# Create a Series with custom labels
s = pd.Series([10.5, 20.0, 30.2, 40.8, 50.1], index=['A', 'B', 'C', 'D', 'E'])

print("Series:\n", s)
print("=" * 40)

# Inspect Series metadata
print("s.index :", s.index)
print("s.values:", s.values)
print("s.dtype :", s.dtype)
print("s.shape :", s.shape)
print("s.size  :", s.size)