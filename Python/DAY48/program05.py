import numpy as np

# 1. Inputs: Actual values (y) and Predictions (y_hat)
y = np.array([30, 35, 48, 60], dtype=np.float64)
y_hat = np.array([29.92, 35.97, 48.08, 60.18], dtype=np.float64)

# 2. Residual Vector (e = y - y_hat)
residuals = y - y_hat

# 3. Calculate RSS (Sum of Squared Residuals)
rss = np.sum(residuals**2)

# Alternative Matrix Vector Form: e.T @ e
rss_matrix = residuals.T @ residuals

print(f"Residual Vector (e) : {residuals.round(4)}")
print(f"Calculated RSS      : {rss:.4f}")
print(f"Matrix Form RSS     : {rss_matrix:.4f}")