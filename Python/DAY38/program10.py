import math
import matplotlib.pyplot as plt
import numpy as np

# 1. Setup Parameters: Binomial B(n=20, p=0.8)
n_trials = 20
p_success = 0.8
n_sims = 10_000

# Set seed for exact reproducibility
np.random.seed(42)

# 2. Simulate Binomial Data
data = np.random.binomial(n_trials, p_success, size=n_sims)

# 3. Calculate Theoretical PMF using math.comb (Pure Python)
k_values = np.arange(0, n_trials + 1)
theoretical_pmf = [
    math.comb(n_trials, int(k))
    * (p_success**k)
    * ((1 - p_success) ** (n_trials - k))
    for k in k_values
]

# 4. Plot Histogram
plt.figure(figsize=(10, 6))

# Empirical Distribution Bars
bins = np.arange(data.min() - 0.5, data.max() + 1.5, 1)
plt.hist(
    data,
    bins=bins,
    density=True,
    alpha=0.7,
    color="#2b5c8f",
    edgecolor="black",
    label="Simulated Batches (Empirical)",
)

# Theoretical PMF Overlay Line
plt.plot(
    k_values,
    theoretical_pmf,
    "ro--",
    linewidth=2,
    markersize=6,
    label=f"Theoretical PMF $B({n_trials}, {p_success})$",
)

# Titles and Formatting
plt.title(
    f"Binomial Distribution Histogram ($n={n_trials}$, $p={p_success}$, $N={n_sims:,}$)",
    fontsize=14,
    pad=15,
)
plt.xlabel("Number of Successes ($k$)", fontsize=12)
plt.ylabel("Probability Density", fontsize=12)
plt.xticks(np.arange(data.min(), data.max() + 1))
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend(fontsize=11)

plt.tight_layout()
plt.show()