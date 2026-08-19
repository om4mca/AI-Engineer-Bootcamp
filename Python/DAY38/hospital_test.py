import math
import random
import numpy as np

# Set seed for exact reproducibility
np.random.seed(42)
random.seed(42)

# Parameters
n_patients = 20  # Patients per batch
p_positive = 0.2  # Probability of positive test
n_batches = 5000  # Number of simulated batches

# 1. Generate Simulation Data
data = list(np.random.binomial(n_patients, p_positive, size=n_batches))
N = len(data)

# 2. Statistical Calculations
# Mean
mean_val = sum(data) / N

# Median
sorted_data = sorted(data)
median_val = (
    (sorted_data[N // 2 - 1] + sorted_data[N // 2]) / 2.0
    if N % 2 == 0
    else float(sorted_data[N // 2])
)

# Mode (Most Frequent Outcome)
freq_dict = {}
for val in data:
    freq_dict[val] = freq_dict.get(val, 0) + 1

mode_val = max(freq_dict, key=freq_dict.get)
mode_count = freq_dict[mode_val]

# Standard Deviation
variance = sum((x - mean_val) ** 2 for x in data) / N
std_val = math.sqrt(variance)

# Min & Max
min_val = min(data)
max_val = max(data)

# Print Summary
print("==================================================")
print("       HOSPITAL TEST PROBABILITY SUMMARY          ")
print("==================================================")
print(
    f"Most Frequent (Mode) : {mode_val} positive tests ({mode_count}/{N} batches)"
)
print(f"Mean                 : {mean_val:.4f} (Theoretical: {n_patients * p_positive:.1f})")
print(f"Median               : {median_val:.1f}")
print(
    f"Standard Deviation   : {std_val:.4f} (Theoretical: {math.sqrt(n_patients * p_positive * (1 - p_positive)):.4f})"
)
print(f"Minimum              : {min_val} positive tests")
print(f"Maximum              : {max_val} positive tests")
print("==================================================")