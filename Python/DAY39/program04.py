import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# 1. Define Parameters: Mean (mu) and Standard Deviation (sigma)
mu = 100.0
sigma = 15.0

# 2. Generate x-axis values (covering +/- 4 standard deviations)
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
# Calculate corresponding PDF (Probability Density Function) values
y = stats.norm.pdf(x, loc=mu, scale=sigma)

# 3. Create Plot
plt.figure(figsize=(10, 6))

# Main Bell Curve Line
plt.plot(
    x,
    y,
    color="#1f77b4",
    linewidth=2.5,
    label=f"Normal Curve $\\mathcal{{N}}(\\mu={int(mu)}, \\sigma={int(sigma)})$",
)

# 4. Fill Standard Deviation Regions (68-95-99.7 Rule)
# Region +/- 1 Sigma (68.27%)
x_1sig = np.linspace(mu - sigma, mu + sigma, 200)
plt.fill_between(
    x_1sig,
    stats.norm.pdf(x_1sig, mu, sigma),
    color="#1f77b4",
    alpha=0.4,
    label="$\\pm 1\\sigma$ (~68.3%)",
)

# Region +/- 2 Sigma (95.45%)
x_2sig_left = np.linspace(mu - 2 * sigma, mu - sigma, 200)
x_2sig_right = np.linspace(mu + sigma, mu + 2 * sigma, 200)
plt.fill_between(
    x_2sig_left,
    stats.norm.pdf(x_2sig_left, mu, sigma),
    color="#1f77b4",
    alpha=0.25,
)
plt.fill_between(
    x_2sig_right,
    stats.norm.pdf(x_2sig_right, mu, sigma),
    color="#1f77b4",
    alpha=0.25,
    label="$\\pm 2\\sigma$ (~95.5%)",
)

# Region +/- 3 Sigma (99.73%)
x_3sig_left = np.linspace(mu - 3 * sigma, mu - 2 * sigma, 200)
x_3sig_right = np.linspace(mu + 2 * sigma, mu + 3 * sigma, 200)
plt.fill_between(
    x_3sig_left,
    stats.norm.pdf(x_3sig_left, mu, sigma),
    color="#1f77b4",
    alpha=0.1,
)
plt.fill_between(
    x_3sig_right,
    stats.norm.pdf(x_3sig_right, mu, sigma),
    color="#1f77b4",
    alpha=0.1,
    label="$\\pm 3\\sigma$ (~99.7%)",
)

# 5. Add Reference Lines & X-Ticks
plt.axvline(
    mu, color="red", linestyle="--", linewidth=1.5, label=f"Mean (\\mu) = {mu}"
)

# Custom X-axis labels to explicitly show values and Z-scores
xticks = [mu + i * sigma for i in range(-3, 4)]
xtick_labels = [
    f"{val:.0f}\n(Z={i:+d})" if i != 0 else f"{val:.0f}\n(Z=0)"
    for i, val in zip(range(-3, 4), xticks)
]
plt.xticks(xticks, xtick_labels)

# 6. Title and Formatting
plt.title(
    "Standard Bell Curve (Normal Distribution)", fontsize=14, pad=15, weight="bold"
)
plt.xlabel("Value ($X$) & Standard Deviations ($Z$)", fontsize=12)
plt.ylabel("Probability Density", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend(fontsize=10, loc="upper right")

plt.tight_layout()
plt.show()