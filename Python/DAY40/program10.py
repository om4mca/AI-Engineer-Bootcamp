import numpy as np

# Distribution Parameters
mu = 100       # Mean (e.g., IQ score average)
sigma = 15     # Standard Deviation
n_samples = 10 # Number of generated values

# Generate continuous samples
samples = np.random.normal(loc=mu, scale=sigma, size=n_samples)

print("--- NUMPY NORMAL DISTRIBUTION SAMPLES ---")
print(np.round(samples, 2))