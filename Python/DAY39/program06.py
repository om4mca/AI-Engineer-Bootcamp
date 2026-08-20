import math
import statistics

# ==============================================================================
# 1. PURE PYTHON FORMULA FUNCTION
# Formula: Z = (X - mu) / sigma
# ==============================================================================


def calculate_z_score(value, mean, std_dev):
    """Calculates Z-score for a single value given population/sample mean and std dev."""
    if std_dev == 0:
        raise ValueError("Standard deviation cannot be zero.")
    return (value - mean) / std_dev


# ==============================================================================
# 2. DATASET Z-SCORE CALCULATOR (Pure Python)
# ==============================================================================


def standardize_dataset(data):
    """Computes Z-scores for every element in a dataset list."""
    n = len(data)
    if n < 2:
        raise ValueError(
            "Dataset must contain at least 2 elements to calculate Z-scores."
        )

    mean_val = sum(data) / n
    variance = sum((x - mean_val) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)

    z_scores = [(x - mean_val) / std_dev for x in data]
    return mean_val, std_dev, z_scores


# Sample Data
scores = [65, 70, 75, 80, 85, 90, 95]

mean, std_dev, z_list = standardize_dataset(scores)

print("==================================================")
print("          PURE PYTHON Z-SCORE CALCULATION         ")
print("==================================================")
print(f"Mean (mu)           : {mean:.2f}")
print(f"Std Dev (sigma)     : {std_dev:.2f}\n")
print(f"{'Value (X)':<12} | {'Z-Score':<10} | Interpretation")
print("-" * 50)

for x, z in zip(scores, z_list):
    if z > 0:
        interp = f"{abs(z):.2f} std dev ABOVE mean"
    elif z < 0:
        interp = f"{abs(z):.2f} std dev BELOW mean"
    else:
        interp = "EXACTLY at the mean"

    print(f"{x:<12} | {z:<+10.2f} | {interp}")
print()


# ==============================================================================
# 3. USING SCIPY & NUMPY (For Data Science Pipeline)
# ==============================================================================
import numpy as np
from scipy import stats

np_data = np.array(scores)

# scipy.stats.zscore automatically calculates Z-scores across arrays
scipy_z_scores = stats.zscore(np_data)

print("==================================================")
print("             SCIPY / NUMPY Z-SCORES               ")
print("==================================================")
print(f"SciPy Z-Scores Array : {np.round(scipy_z_scores, 2)}")
print("==================================================")