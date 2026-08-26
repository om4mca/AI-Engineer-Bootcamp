import numpy as np

# Synthetic Dataset: 100 samples, 2 features
np.random.seed(42)
X = np.random.randn(100, 2)
# Add intercept column (ones)
X_b = np.c_[np.ones((100, 1)), X] 
y = 3 + 1.5 * X[:, 0:1] + 2.5 * X[:, 1:2] + np.random.randn(100, 1) * 0.1

# Compute parameters via Normal Equation using matrix inverse
theta_best = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

print("Estimated Weights [Intercept, w1, w2]:\n", theta_best.ravel())