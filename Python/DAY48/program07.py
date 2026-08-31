import numpy as np

# Data: 4 samples, 2 features (x1, x2)
x1 = np.array([2, 3, 5, 7], dtype=np.float64)
x2 = np.array([35, 45, 52, 60], dtype=np.float64)
y = np.array([30, 35, 48, 60], dtype=np.float64)

# 1. Build Design Matrix X (Column of 1s + Features)
X = np.column_stack([np.ones(len(x1)), x1, x2])

# 2. Solve for Weights analytically using Normal Equation: w = (X^T X)^(-1) X^T y
weights = np.linalg.inv(X.T @ X) @ X.T @ y

# 3. Vectorized Predictions & Residuals
y_hat = X @ weights
residuals = y - y_hat
rss = residuals.T @ residuals
mse = np.mean(residuals**2)

print(f"Design Matrix (X) Shape : {X.shape}")
print(f"Weights (w0, w1, w2)    : {weights.round(4)}")
print(f"Predictions (ŷ)         : {y_hat.round(2)}")
print(f"RSS                     : {rss:.4f}")
print(f"MSE                     : {mse:.4f}")