import pandas as pd

# Create a Series
s = pd.Series([10, 20, 30, 40, 50])

# Add 5 to every element
result_add = s + 5

# Alternative: using the .add() method
result_method = s.add(5)

print("Original Series:\n", s)
print("-" * 30)
print("After adding 5 (s + 5):\n", result_add)