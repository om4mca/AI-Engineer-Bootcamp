import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Set seed for exact reproducibility
np.random.seed(42)

# ==============================================================================
# 1. GENERATE NORMALLY DISTRIBUTED DATA
# ==============================================================================
mean = 100.0  # Mean (mu)
std_dev = 15.0  # Standard Deviation (sigma)
sample_size = 10000  # Number of samples

# Generate sample array following N(100, 15^2)
data = np.random.normal(loc=mean, scale=std_dev, size=sample_size)

# Calculate summary metrics
sample_mean = np.mean(data)
sample_std = np.std(data)

print("==================================================")
print("          GENERATED DATA SUMMARY METRICS          ")
print("==================================================")
print(f"Target Mean      : {mean:.2f}")
print(f"Sample Mean      : {sample_mean:.2f}")
print(f"Target Std Dev   : {std_dev:.2f}")
print(f"Sample Std Dev   : {sample_std:.2f}\n")

# ==============================================================================
# 2. STANDARDIZATION & PROBABILITY CALCULATION (SciPy)
# ==============================================================================
# Z-Score transformation: Z = (X - mu) / sigma
z_scores = (data - sample_mean) / sample_std

# Calculate cumulative probability: P(X <= 115)
p_less_115 = stats.norm.cdf(115, loc=mean, scale=std_dev)

# Calculate 95th percentile value
val_95th = stats.norm.ppf(0.95, loc=mean, scale=std_dev)

print("--------------------------------------------------")
print("             SCIPY PROBABILITY CHECKS             ")
print("--------------------------------------------------")
print(f"P(X <= 115)       : {p_less_115:.2%}")
print(f"95th Percentile   : {val_95th:.2f}")
print("==================================================\n")

# ==============================================================================
# 3. VISUALIZATION (Matplotlib)
# ==============================================================================
plt.figure(figsize=(10, 6))

# Plot Empirical Histogram
count, bins, ignored = plt.hist(
    data,
    bins=50,
    density=True,
    alpha=0.6,
    color="#2b5c8f",
    edgecolor="black",
    label="Sample Histogram",
)

# Plot Theoretical Bell Curve (PDF)
x_pdf = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 1000)
y_pdf = stats.norm.pdf(x_pdf, loc=mean, scale=std_dev)
plt.plot(
    x_pdf,
    y_pdf,
    color="red",
    linewidth=2.5,
    label=f"Theoretical PDF $\\mathcal{{N}}({int(mean)}, {int(std_dev)}^2)$",
)

# Vertical line for mean
plt.axvline(
    sample_mean,
    color="black",
    linestyle="--",
    linewidth=1.5,
    label=f"Mean = {sample_mean:.1f}",
)

# Formatting
plt.title(
    f"Normal Distribution Simulation ($N={sample_size:,}$, $\\mu={int(mean)}$, $\\sigma={int(std_dev)}$)",
    fontsize=14,
    pad=15,
)
plt.xlabel("Value ($X$)", fontsize=12)
plt.ylabel("Probability Density", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend(fontsize=11)

plt.tight_layout()
plt.show()