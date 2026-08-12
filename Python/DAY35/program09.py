import numpy as np

data = [12, 15, 18, 22, 25, 28, 30, 35, 40, 42, 85]

# Using np.percentile (0 to 100)
q1, q2, q3 = np.percentile(data, [25, 50, 75])
iqr = q3 - q1

print(f"Q1 (25th %) : {q1}")
print(f"Q2 (Median) : {q2}")
print(f"Q3 (75th %) : {q3}")
print(f"IQR (Q3-Q1) : {iqr}")