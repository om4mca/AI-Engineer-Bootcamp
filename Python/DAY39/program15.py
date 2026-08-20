import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate sample data for two normal distributions
np.random.seed(42)
dist_A = np.random.normal(loc=100, scale=15, size=1000)  # Mean = 100, Std = 15
dist_B = np.random.normal(loc=110, scale=10, size=1000)  # Mean = 110, Std = 10

# Summary statistics comparison
summary_df = pd.DataFrame({
    'Metric': ['Mean', 'Std Dev', 'Variance', 'Median', 'IQR'],
    'Distribution A': [np.mean(dist_A), np.std(dist_A), np.var(dist_A), np.median(dist_A), stats.iqr(dist_A)],
    'Distribution B': [np.mean(dist_B), np.std(dist_B), np.var(dist_B), np.median(dist_B), stats.iqr(dist_B)]
})

print("--- SUMMARY STATISTICS ---")
print(summary_df.round(2).to_string(index=False))

# Visualization
plt.figure(figsize=(10, 5))
plt.hist(dist_A, bins=30, alpha=0.5, label='Dist A (μ=100, σ=15)', color='blue', density=True)
plt.hist(dist_B, bins=30, alpha=0.5, label='Dist B (μ=110, σ=10)', color='green', density=True)
plt.title('Comparison of Two Normal Distributions')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()