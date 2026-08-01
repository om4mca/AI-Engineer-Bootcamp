import pandas as pd

# Create a Series
s = pd.Series([10, 20, 30, 40, 50])

# Multiply every element by 2
result_mult = s * 2

# Alternative: using the .mul() method
result_method = s.mul(2)

print("Original Series:\n", s)
print("-" * 30)
print("After multiplying by 2 (s * 2):\n", result_mult)