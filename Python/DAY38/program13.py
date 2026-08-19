import math

# ==============================================================================
# 1. DISCRETE DISTRIBUTION STANDARD DEVIATION
# Formula: sigma = sqrt(sum((x - E[X])^2 * P(X = x)))
# ==============================================================================

def discrete_std_dev(outcomes, probabilities):
    """Calculates Mean, Variance, and Standard Deviation for a discrete PMF."""
    if not math.isclose(sum(probabilities), 1.0, abs_tol=1e-5):
        raise ValueError("Probabilities must sum to 1.0")

    # Step 1: Expected Value E[X]
    e_x = sum(x * p for x, p in zip(outcomes, probabilities))

    # Step 2: Variance Var(X) = sum((x - E[X])^2 * P(X = x))
    variance = sum(((x - e_x) ** 2) * p for x, p in zip(outcomes, probabilities))

    # Step 3: Standard Deviation sigma = sqrt(Var(X))
    std_dev = math.sqrt(variance)

    return e_x, variance, std_dev


# Example: Rolling a single fair 6-sided die
outcomes = [1, 2, 3, 4, 5, 6]
probs = [1 / 6] * 6

mean_d, var_d, std_d = discrete_std_dev(outcomes, probs)

print("==================================================")
print("   1. DISCRETE STANDARD DEVIATION (Fair Die)      ")
print("==================================================")
print(f"Mean E[X]        : {mean_d:.4f}")
print(f"Variance Var(X)  : {var_d:.4f}")
print(f"Std Dev (Sigma)  : {std_d:.4f}\n")


# ==============================================================================
# 2. CONTINUOUS DISTRIBUTION STANDARD DEVIATION
# Formula: sigma = sqrt(integral((x - E[X])^2 * f(x) dx)) via Numerical Integration
# ==============================================================================

def continuous_std_dev(pdf_func, lower_bound, upper_bound, steps=10_000):
    """Calculates Mean, Variance, and Standard Deviation for a continuous PDF using Trapezoidal Integration."""
    dx = (upper_bound - lower_bound) / steps
    x_vals = [lower_bound + i * dx for i in range(steps + 1)]

    # Step 1: Compute Mean E[X] = integral(x * f(x) dx)
    y_mean = [x * pdf_func(x) for x in x_vals]
    e_x = (0.5 * y_mean[0] + sum(y_mean[1:-1]) + 0.5 * y_mean[-1]) * dx

    # Step 2: Compute Variance Var(X) = integral((x - E[X])^2 * f(x) dx)
    y_var = [((x - e_x) ** 2) * pdf_func(x) for x in x_vals]
    variance = (0.5 * y_var[0] + sum(y_var[1:-1]) + 0.5 * y_var[-1]) * dx

    # Step 3: Standard Deviation sigma = sqrt(Var(X))
    std_dev = math.sqrt(variance)

    return e_x, variance, std_dev


# Example: Uniform Distribution [0, 30] minutes (Bus wait time)
pdf_bus = lambda x: 1.0 / 30.0 if 0 <= x <= 30 else 0.0

mean_c, var_c, std_c = continuous_std_dev(pdf_bus, lower_bound=0, upper_bound=30)

print("==================================================")
print("  2. CONTINUOUS STANDARD DEVIATION (Bus Wait)     ")
print("==================================================")
print(f"Mean E[X]        : {mean_c:.4f} minutes")
print(f"Variance Var(X)  : {var_c:.4f}")
print(f"Std Dev (Sigma)  : {std_c:.4f} minutes")
print("==================================================")