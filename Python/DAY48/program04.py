import numpy as np

# 1. Input actual targets (y) and predictions (y_hat)
y = np.array([30, 35, 48, 60], dtype=np.float64)
y_hat = np.array([29.92, 35.97, 48.08, 60.18], dtype=np.float64)

# 2. Calculate Residuals
residuals = y - y_hat

# 3. Calculate Squared Errors
squared_errors = residuals ** 2

# 4. Calculate Aggregated Metrics (RSS & MSE)
rss = np.sum(squared_errors)
mse = np.mean(squared_errors)

print("Actual Values (y)        :", y)
print("Predicted Values (ŷ)     :", y_hat)
print("Residuals (e = y - ŷ)    :", residuals.round(4))
print("Squared Errors (e²)      :", squared_errors.round(4))
print(f"\nRSS (Sum of Squared Errors) : {rss:.4f}")
print(f"MSE (Mean Squared Error)    : {mse:.4f}")