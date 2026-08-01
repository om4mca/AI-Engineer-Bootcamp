import pandas as pd

# Create a Series
s = pd.Series([10, 20, 30, 40, 50, 60, 70])

# Calculate median and standard deviation
series_median = s.median()
series_std = s.std()

print("Series:\n", s)
print("-" * 35)
print("Median (s.median())             :", series_median)
print(f"Standard Deviation (s.std())    : {series_std:.2f}")