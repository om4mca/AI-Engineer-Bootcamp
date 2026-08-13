import matplotlib.pyplot as plt
import numpy as np
import math

# Set up grid layout
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Normal Distribution (Continuous PDF)
mu, sigma = 0, 1
x_norm = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y_norm = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_norm - mu) / sigma)**2)

axes[0, 0].plot(x_norm, y_norm, 'b-', lw=2, label=f'μ={mu}, σ={sigma}')
axes[0, 0].fill_between(x_norm, y_norm, alpha=0.2, color='blue')
axes[0, 0].set_title('Normal Distribution (Continuous PDF)', fontweight='bold')
axes[0, 0].set_xlabel('Value (x)')
axes[0, 0].set_ylabel('Probability Density')
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].legend()

# 2. Binomial Distribution (Discrete PMF)
n, p = 20, 0.5
x_bin = np.arange(0, n + 1)
y_bin = np.array([math.comb(n, k) * (p**k) * ((1 - p)**(n - k)) for k in x_bin])

axes[0, 1].bar(x_bin, y_bin, color='green', alpha=0.7, edgecolor='black', width=0.6)
axes[0, 1].set_title(f'Binomial Distribution (n={n}, p={p})', fontweight='bold')
axes[0, 1].set_xlabel('Successes (k)')
axes[0, 1].set_ylabel('Probability')
axes[0, 1].grid(True, alpha=0.3)

# 3. Poisson Distribution (Discrete PMF)
lambda_param = 4
x_poi = np.arange(0, 15)
y_poi = np.array([(lambda_param**k * np.exp(-lambda_param)) / math.factorial(k) for k in x_poi])

axes[1, 0].stem(x_poi, y_poi, linefmt='r-', markerfmt='ro', basefmt='k-')
axes[1, 0].set_title(f'Poisson Distribution (λ={lambda_param})', fontweight='bold')
axes[1, 0].set_xlabel('Event Count (k)')
axes[1, 0].set_ylabel('Probability')
axes[1, 0].grid(True, alpha=0.3)

# 4. Exponential Distribution (Continuous PDF)
scale = 1.5  # beta = 1/lambda
x_exp = np.linspace(0, 8, 1000)
y_exp = (1 / scale) * np.exp(-x_exp / scale)

axes[1, 1].plot(x_exp, y_exp, color='purple', lw=2, label=f'scale={scale}')
axes[1, 1].fill_between(x_exp, y_exp, alpha=0.2, color='purple')
axes[1, 1].set_title('Exponential Distribution (Continuous PDF)', fontweight='bold')
axes[1, 1].set_xlabel('Time / Interval (x)')
axes[1, 1].set_ylabel('Probability Density')
axes[1, 1].grid(True, alpha=0.3)
axes[1, 1].legend()

plt.tight_layout()
plt.savefig('distributions_no_scipy.png')
print("Plots generated successfully without scipy.")