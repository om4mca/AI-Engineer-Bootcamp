import math
from collections import Counter


# ==============================================================================
# 1. DISCRETE CDF (Coin Flips Example: n=5, p=0.5)
# Formula: F(x) = P(X <= x) = sum_{k <= x} P(X = k)
# ==============================================================================


def binomial_pmf(k, n, p):
    """P(X = k) for binomial distribution."""
    return math.comb(n, k) * (p**k) * ((1 - p) ** (n - k))


n_flips = 5
p_head = 0.5

# Step 1: Calculate PMF
pmf = {k: binomial_pmf(k, n_flips, p_head) for k in range(n_flips + 1)}

# Step 2: Cumulative Sum to get Discrete CDF
discrete_cdf = {}
running_total = 0.0
for k in range(n_flips + 1):
    running_total += pmf[k]
    discrete_cdf[k] = running_total

print("==================================================")
print("    1. DISCRETE CDF (Heads in 5 Coin Flips)       ")
print("==================================================")
print(f"{'Heads (k)':<10} | {'PMF P(X = k)':<12} | {'CDF P(X <= k)':<12}")
print("-" * 42)
for k in range(n_flips + 1):
    print(f"{k:<10} | {pmf[k]:<12.4f} | {discrete_cdf[k]:<12.4f}")


# ==============================================================================
# 2. CONTINUOUS CDF (Normal Distribution: Mean=0, StdDev=1)
# Formula: F(x) = P(X <= x) = 0.5 * [1 + erf((x - mu) / (sigma * sqrt(2)))]
# ==============================================================================


def normal_cdf(x, mu=0.0, sigma=1.0):
    """Exact CDF for a Standard Normal Distribution using standard error function (math.erf)."""
    return 0.5 * (1.0 + math.erf((x - mu) / (sigma * math.sqrt(2.0))))


x_values = [-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0]

print("\n==================================================")
print("    2. CONTINUOUS CDF (Standard Normal N(0,1))    ")
print("==================================================")
print(f"{'Z-Score (x)':<12} | {'CDF P(X <= x)':<15} | {'Interpretation'}")
print("-" * 55)

for x in x_values:
    cdf_val = normal_cdf(x)
    print(f"{x:<12.1f} | {cdf_val:<15.4f} | {cdf_val:.2%} of data <= {x}")