import math

# ==============================================================================
# 1. DISCRETE DISTRIBUTION VARIANCE
# Formula: Var(X) = sum((x - E[X])^2 * P(X = x))
# ==============================================================================


def discrete_variance(outcomes, probabilities):
    """Calculates Expected Value, Variance, and Standard Deviation for a discrete PMF."""
    # Axiom Check: Probabilities must sum to 1.0
    if not math.isclose(sum(probabilities), 1.0, abs_tol=1e-5):
        raise ValueError("Probabilities must sum to 1.0")

    # Step 1: Calculate Expected Value E[X]
    e_x = sum(x * p for x, p in zip(outcomes, probabilities))

    # Step 2: Calculate Variance Var(X) = sum((x - E[X])^2 * P(X = x))
    variance = sum(((x - e_x) ** 2) * p for x, p in zip(outcomes, probabilities))

    # Step 3: Calculate Standard Deviation sigma = sqrt(Var(X))
    std_dev = math.sqrt(variance)

    return e_x, variance, std_dev


# Example: Rolling a fair 6-sided die
die_outcomes = [1, 2, 3, 4, 5, 6]
die_probs = [1 / 6] * 6

mean_d, var_d, std_d = discrete_variance(die_outcomes, die_probs)

print("==================================================")
print("     1. DISCRETE VARIANCE (Single Fair Die)       ")
print("==================================================")
print(f"Mean E[X]        : {mean_d:.4f}")
print(f"Variance Var(X)  : {var_d:.4f}")
print(f"Std Dev (Sigma)  : {std_d:.4f}\n")


# ==============================================================================
# 2. CONTINUOUS DISTRIBUTION VARIANCE
# Formula: Var(X) = integral((x - E[X])^2 * f(x) dx) via Numerical Integration
# ==============================================================================


def continuous_variance(pdf_func, lower_bound, upper_bound, steps=10_000):
    """Calculates Var(X) for a continuous variable over [a, b] using Trapezoidal Rule."""
    dx = (upper_bound - lower_bound) / steps

    # Step 1: Compute E[X] = integral(x * f(x) dx)
    x_vals = [lower_bound + i * dx for i in range(steps + 1)]
    y_mean = [x * pdf_func(x) for x in x_vals]
    e_x = (0.5 * y_mean[0] + sum(y_mean[1:-1]) + 0.5 * y_mean[-1]) * dx

    # Step 2: Compute Var(X) = integral((x - E[X])^2 * f(x) dx)
    y_var = [((x - e_x) ** 2) * pdf_func(x) for x in x_vals]
    variance = (0.5 * y_var[0] + sum(y_var[1:-1]) + 0.5 * y_var[-1]) * dx

    std_dev = math.sqrt(variance)

    return e_x, variance, std_dev


# Example: Uniform Distribution over [0, 30] (Bus wait time)
# PDF f(x) = 1/30 for 0 <= x <= 30
pdf_bus = lambda x: 1.0 / 30.0 if 0 <= x <= 30 else 0.0

mean_c, var_c, std_c = continuous_variance(
    pdf_bus, lower_bound=0, upper_bound=30
)

print("==================================================")
print("    2. CONTINUOUS VARIANCE (Bus Wait Time [0,30]) ")
print("==================================================")
print(f"Mean E[X]        : {mean_c:.4f} minutes")
print(f"Variance Var(X)  : {var_c:.4f}")
print(f"Std Dev (Sigma)  : {std_c:.4f} minutes")
print("==================================================")