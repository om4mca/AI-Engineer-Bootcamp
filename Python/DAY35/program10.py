import numpy as np

data = [12, 15, 18, 22, 25, 28, 30, 35, 40, 42, 85]

# Compute 25th (Q1) and 75th (Q3) percentiles
q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1

print(f"Q1 (25th Percentile) : {q1}")
print(f"Q3 (75th Percentile) : {q3}")
print(f"IQR (Q3 - Q1)        : {iqr}")