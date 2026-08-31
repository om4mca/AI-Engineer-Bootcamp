import numpy as np

# Actual target values (y) and Design Matrix (X)
y = np.array([30, 35, 48, 60], dtype=np.float64)
X = np.array([
    [1, 2],
    [1, 3],
    [1, 5],
    [1, 7]
], dtype=np.float64)

# 1. Compute Least Squares Weights
weights, _, _, _ = np.linalg.lstsq(X, y, rcond=None)

# 2. Compute Predictions (y_hat = X @ w)
y_hat = X @ weights

# 3. Compute Residual Vector (e = y - y_hat)
residuals = y - y_hat

# 4. Compute Summary Metrics (RSS and MSE)
rss = np.sum(residuals**2)
mse = np.mean(residuals**2)

print("Actual Values (y)     :", y)
print("Predicted Values (ŷ)  :", y_hat.round(2))
print("Residuals (e = y - ŷ) :", residuals.round(4))
print(f"RSS (Sum of Squares)  : {rss:.4f}")
print(f"MSE (Mean Sq Error)   : {mse:.4f}")