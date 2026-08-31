import numpy as np

# 1. Inputs: Actual values (y) and Predictions (y_hat)
y = np.array([30, 35, 48, 60], dtype=np.float64)
y_hat = np.array([29.92, 35.97, 48.08, 60.18], dtype=np.float64)

# 2. Compute Residuals & Squared Errors
residuals = y - y_hat
squared_errors = residuals ** 2

# 3. Calculate MSE
rss = np.sum(squared_errors)
mse = np.mean(squared_errors)  # Equivalent to rss / len(y)

print(f"Residual Vector (e) : {residuals.round(4)}")
print(f"Squared Errors (e²) : {squared_errors.round(4)}")
print(f"RSS                 : {rss:.4f}")
print(f"Calculated MSE      : {mse:.4f}")