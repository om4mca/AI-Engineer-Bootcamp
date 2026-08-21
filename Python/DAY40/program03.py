import numpy as np

# Sample dataset (e.g., test scores out of 100)
scores = np.array([45, 55, 60, 65, 70, 75, 80, 85, 90, 95, 99])

# Single Percentile (e.g., 90th percentile)
p90 = np.percentile(scores, 90)

# Multiple Percentiles at once (Quartiles: 25th, 50th, 75th)
q1, median, q3 = np.percentile(scores, [25, 50, 75])

print("--- NUMPY PERCENTILE RESULTS ---")
print(f"25th Percentile (Q1):     {q1:.2f}")
print(f"50th Percentile (Median): {median:.2f}")
print(f"75th Percentile (Q3):     {q3:.2f}")
print(f"90th Percentile:          {p90:.2f}")