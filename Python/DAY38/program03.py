import numpy as np

# ==============================================================================
# 1. DISCRETE RANDOM VARIABLE
# Scenario: Sum of rolling two standard 6-sided dice
# ==============================================================================

# Defined possible values (2 through 12)
x_values = np.arange(2, 13)

# Outcomes count for each sum: [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
outcomes_count = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])
pmf_probabilities = outcomes_count / 36.0  # Sum of probabilities = 1.0

# Expected Value E[X] = sum(x * P(X = x))
expected_value_discrete = np.sum(x_values * pmf_probabilities)

# Variance Var(X) = sum((x - E[X])^2 * P(X = x))
variance_discrete = np.sum(
    ((x_values - expected_value_discrete) ** 2) * pmf_probabilities
)

# Probability P(X = 7) directly from PMF
p_exact_7 = pmf_probabilities[np.where(x_values == 7)][0]

print("==================================================")
print("   1. DISCRETE RANDOM VARIABLE (Two Dice Sum)     ")
print("==================================================")
print(f"Possible Values : {list(x_values)}")
print(f"P(X = 7)        : {p_exact_7:.4f} ({p_exact_7:.2%})")
print(f"Expected Value  : {expected_value_discrete:.2f}")
print(f"Variance        : {variance_discrete:.4f}\n")


# ==============================================================================
# 2. CONTINUOUS RANDOM VARIABLE
# Scenario: Uniformly distributed bus wait time between 0 and 30 minutes
# ==============================================================================

a, b = 0.0, 30.0  # Lower and upper bounds (minutes)

# Probability Density Function (PDF) height: f(y) = 1 / (b - a)
pdf_height = 1.0 / (b - a)

# Expected Value E[Y] = (a + b) / 2
expected_value_continuous = (a + b) / 2.0

# Variance Var(Y) = (b - a)^2 / 12
variance_continuous = ((b - a) ** 2) / 12.0


# Cumulative Distribution Function CDF: F(y) = P(Y <= y)
def uniform_cdf(y, low, high):
    if y < low:
        return 0.0
    elif y > high:
        return 1.0
    else:
        return (y - low) / (high - low)


# Interval Probability P(5 <= Y <= 15) = CDF(15) - CDF(5)
p_interval = uniform_cdf(15, a, b) - uniform_cdf(5, a, b)

print("==================================================")
print("   2. CONTINUOUS RANDOM VARIABLE (Bus Wait Time)  ")
print("==================================================")
print(f"Interval Bounds : [{a:.0f}, {b:.0f}] minutes")
print(f"P(Y = 10)       : 0.0000 (Exact point probability is strictly 0)")
print(f"Density f(10)   : {pdf_height:.4f} (PDF height, NOT probability)")
print(f"P(5 <= Y <= 15) : {p_interval:.4f} ({p_interval:.2%})")
print(f"Expected Value  : {expected_value_continuous:.2f} minutes")
print(f"Variance        : {variance_continuous:.4f}")
print("==================================================")