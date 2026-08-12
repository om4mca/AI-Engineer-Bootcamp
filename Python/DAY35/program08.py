import numpy as np

data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

# Calculate specific percentiles (e.g., 25th, 50th, 75th, 90th)
p25 = np.percentile(data, 25)  # 1st Quartile (Q1)
p50 = np.percentile(data, 50)  # Median (Q2)
p75 = np.percentile(data, 75)  # 3rd Quartile (Q3)
p90 = np.percentile(data, 90)  # 90th Percentile

print(f"Dataset          : {data}")
print(f"25th Percentile  : {p25}")
print(f"50th (Median)    : {p50}")
print(f"75th Percentile  : {p75}")
print(f"90th Percentile  : {p90}")

# Compute multiple percentiles at once
percentiles = [10, 25, 50, 75, 90]
results = np.percentile(data, percentiles)
print(f"\nPercentiles {percentiles}: {results}")