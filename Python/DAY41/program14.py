import numpy as np

# Feature Vector (x): [Age, Stay_Days, Blood_Pressure]
x = np.array([65.0, 10.0, 140.0])

# Learned Weights (w): Importance assigned to each feature
w = np.array([0.05, 1.2, 0.02])

# Learned Bias (b): Base offset
b = -2.5

# Weighted Sum calculation: z = (w · x) + b
weighted_sum = np.dot(w, x) + b
# Breakdown: (65*0.05) + (10*1.2) + (140*0.02) - 2.5
#          = 3.25 + 12.0 + 2.8 - 2.5 = 15.55

print(f"Weighted Output (z): {weighted_sum:.2f}")