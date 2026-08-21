import numpy as np

# Sample dataset
data = np.array([10, 12, 23, 23, 16, 23, 21, 16])

# Mean
mean = np.mean(data)

# Population Standard Deviation (ddof=0) -> divides by N
std_pop = np.std(data, ddof=0)

# Sample Standard Deviation (ddof=1) -> divides by N - 1
std_sample = np.std(data, ddof=1)

print("--- NUMPY STANDARD DEVIATION ---")
print(f"Mean:                       {mean:.2f}")
print(f"Population Std Dev (ddof=0): {std_pop:.2f}")
print(f"Sample Std Dev (ddof=1):     {std_sample:.2f}")