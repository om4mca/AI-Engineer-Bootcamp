# ==============================================================================
# 1. PURE PYTHON (Manual Step-by-Step)
# Formula: Mean = Sum(x) / N
# ==============================================================================
def calculate_mean_manual(data):
    if not data:
        raise ValueError("Cannot calculate mean of an empty list.")

    total_sum = 0
    count = 0
    for value in data:
        total_sum += value
        count += 1

    return total_sum / count


# ==============================================================================
# 2. USING PYTHON BUILT-INS (sum() and len())
# ==============================================================================
def calculate_mean_builtin(data):
    if not data:
        raise ValueError("Cannot calculate mean of an empty list.")
    return sum(data) / len(data)


# Example Data
numbers = [12, 45, 67, 89, 34, 23, 56, 78]

print("==================================================")
print("             MEAN CALCULATION RESULTS             ")
print("==================================================")
print(f"Data Set        : {numbers}")
print(f"1. Manual Loop  : {calculate_mean_manual(numbers):.2f}")
print(f"2. Built-in     : {calculate_mean_builtin(numbers):.2f}")


# ==============================================================================
# 3. USING STANDARD LIBRARY (statistics module)
# ==============================================================================
import statistics

stat_mean = statistics.mean(numbers)
print(f"3. statistics   : {stat_mean:.2f}")


# ==============================================================================
# 4. USING NUMPY (for arrays / matrices)
# ==============================================================================
import numpy as np

np_arr = np.array(numbers)
np_mean = np.mean(np_arr)
print(f"4. NumPy mean   : {np_mean:.2f}")
print("==================================================")