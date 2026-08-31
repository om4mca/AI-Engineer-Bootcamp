import numpy as np

# 1. Dataset: Features (x1, x2) and Target (y)
x1 = np.array([1, 2, 3, 4, 5], dtype=np.float64)
x2 = np.array([2, 1, 4, 2, 5], dtype=np.float64)
y  = np.array([7, 8, 14, 11, 19], dtype=np.float64)

# 2. Build Design Matrix X (Bias column + Features)
X = np.column_stack([np.ones(len(x1)), x1, x2])

# 3. Solve Least Squares
weights, rss_lstsq, rank, s = np.linalg.lstsq(X, y, rcond=None)

# 4. Compute Predictions, Residuals, and Metrics
y_hat = X @ weights
residuals = y - y_hat
rss = np.sum(residuals**2)
mse = np.mean(residuals**2)

# --- Output Results ---
print(f"Design Matrix Shape : {X.shape}")
print(f"Matrix Rank         : {rank}")
print(f"Weights (w0, w1, w2): {weights.round(4)}")
print(f"Predictions (ŷ)    : {y_hat.round(2)}")
print(f"Residuals (e)       : {residuals.round(4)}")
print(f"RSS                 : {rss:.4f}")
print(f"MSE                 : {mse:.4f}")