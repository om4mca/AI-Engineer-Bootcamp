import math
import random
import numpy as np

# Set seed for exact reproducibility
np.random.seed(42)
random.seed(42)

# 1. Generate Simulation Data
n_trials = 20      # Employees per batch
p_success = 0.8    # Pass probability
n_sims = 5000      # Batches simulated

# Generated vector of successful employees per batch
results = np.random.binomial(n_trials, p_success, size=n_sims)

# Convert to standard Python list for standard math operations
data = list(results)
N = len(data)

# 2. Pure Math Metric Calculations
# Mean
mean_val = sum(data) / N

# Median
sorted_data = sorted(data)
if N % 2 == 1:
    median_val = float(sorted_data[N // 2])
else:
    median_val = (sorted_data[N // 2 - 1] + sorted_data[N // 2]) / 2.0

# Mode (Most Frequent)
freq_dict = {}
for val in data:
    freq_dict[val] = freq_dict.get(val, 0) + 1

mode_val = max(freq_dict, key=freq_dict.get)
mode_count = freq_dict[mode_val]

# Standard Deviation (Population / N)
variance = sum((x - mean_val) ** 2 for x in data) / N
std_val = math.sqrt(variance)

# Min & Max
min_val = min(data)
max_val = max(data)

# Theoretical Binomial Values
theoretical_mean = n_trials * p_success
theoretical_std = math.sqrt(n_trials * p_success * (1 - p_success))

# 3. Print Statistical Summary
print("==================================================")
print("     EMPLOYEE TRAINING SUCCESS SIMULATION         ")
print("==================================================")
print(f"Most Frequent (Mode) : {mode_val} employees ({mode_count}/{N} batches)")
print(f"Mean Successes       : {mean_val:.4f} (Theoretical: {theoretical_mean:.1f})")
print(f"Median Successes     : {median_val:.1f}")
print(f"Standard Deviation   : {std_val:.4f} (Theoretical: {theoretical_std:.4f})")
print(f"Minimum Successes    : {min_val} employees")
print(f"Maximum Successes    : {max_val} employees")
print("==================================================\n")

# 4. Text-Based ASCII Distribution Visualization
print("==================================================")
print("     DISTRIBUTION VISUALIZATION (FREQUENCY)       ")
print("==================================================")
max_bar_length = 40
max_freq = max(freq_dict.values())

for count in range(min_val, max_val + 1):
    freq = freq_dict.get(count, 0)
    pct = (freq / N) * 100
    bar = "█" * int((freq / max_freq) * max_bar_length)
    print(f"{count:2d} passes | {bar:<40} | {freq:4d} batches ({pct:5.2f}%)")
print("==================================================")