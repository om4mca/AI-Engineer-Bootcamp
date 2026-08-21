import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1. Generate Normal Distribution Data
np.random.seed(42)
mu, sigma = 0, 1
data = np.random.normal(loc=mu, scale=sigma, size=1000)

# 2. Create Plot
plt.figure(figsize=(8, 5))

# Draw Histogram
count, bins, ignored = plt.hist(
    data, 
    bins=30, 
    density=True, 
    alpha=0.6, 
    color='steelblue', 
    edgecolor='black',
    label='Sample Data (Hist)'
)

# Overlay Theoretical PDF
x = np.linspace(data.min(), data.max(), 200)
pdf = stats.norm.pdf(x, loc=mu, scale=sigma)
plt.plot(x, pdf, color='crimson', linewidth=2.5, label='Theoretical PDF')

# Formatting
plt.title('Normal Distribution: Histogram + Fitted PDF', fontsize=12, fontweight='bold')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()