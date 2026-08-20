import math
import random

# Set random seed for reproducibility
random.seed(42)


def verify_mean_median_symmetry(data, tolerance_pct=2.0):
    """Calculates Mean and Median, checks symmetry, and assesses distribution skewness.

    - tolerance_pct: Acceptable percentage difference relative to standard deviation.
    """
    n = len(data)
    if n == 0:
        raise ValueError("Data array cannot be empty.")

    # 1. Calculate Mean
    mean_val = sum(data) / n

    # 2. Calculate Median
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        median_val = (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
    else:
        median_val = float(sorted_data[mid])

    # 3. Calculate Standard Deviation (for scale-independent comparison)
    variance = sum((x - mean_val) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)

    # 4. Compute Absolute & Relative Difference
    abs_diff = abs(mean_val - median_val)
    # Normalized difference relative to Standard Deviation
    norm_diff_pct = (abs_diff / std_dev) * 100 if std_dev > 0 else 0.0

    is_symmetric = norm_diff_pct <= tolerance_pct

    return {
        "Mean": mean_val,
        "Median": median_val,
        "Std Dev": std_dev,
        "Abs Difference": abs_diff,
        "Relative Diff (% of StdDev)": norm_diff_pct,
        "Is Mean ≈ Median": is_symmetric,
    }


# ==============================================================================
# TEST CASE 1: Symmetric / Normally Distributed Data (Target: Mean ≈ Median)
# ==============================================================================
symmetric_data = [random.gauss(mu=100, sigma=15) for _ in range(5000)]
res_sym = verify_mean_median_symmetry(symmetric_data)

print("==================================================")
print("  TEST 1: SYMMETRIC DISTRIBUTION (Normal Curve)   ")
print("==================================================")
print(f"Mean                  : {res_sym['Mean']:.2f}")
print(f"Median                : {res_sym['Median']:.2f}")
print(f"Abs Difference        : {res_sym['Abs Difference']:.2f}")
print(f"Diff as % of StdDev   : {res_sym['Relative Diff (% of StdDev)']:.2f}%")
print(f"Verdict (Mean ≈ Median): {res_sym['Is Mean ≈ Median']}\n")


# ==============================================================================
# TEST CASE 2: Right-Skewed Data (Income/Pareto - Target: Mean > Median)
# ==============================================================================
skewed_data = [random.paretovariate(alpha=2.5) * 50000 for _ in range(5000)]
res_skew = verify_mean_median_symmetry(skewed_data)

print("==================================================")
print("  TEST 2: SKEWED DISTRIBUTION (Pareto / Income)   ")
print("==================================================")
print(f"Mean                  : ${res_skew['Mean']:,.2f}")
print(f"Median                : ${res_skew['Median']:,.2f}")
print(f"Abs Difference        : ${res_skew['Abs Difference']:,.2f}")
print(f"Diff as % of StdDev   : {res_skew['Relative Diff (% of StdDev)']:.2f}%")
print(f"Verdict (Mean ≈ Median): {res_skew['Is Mean ≈ Median']}")
print("==================================================")