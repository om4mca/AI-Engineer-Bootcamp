import numpy as np

# 1. Dataset setup
X = np.array([
    [1.0, 1.5, 3.0],
    [1.0, 3.0, 4.0],
    [1.0, 4.5, 3.5],
    [1.0, 6.0, 5.0],
    [1.0, 8.0, 4.5]
])
y = np.array([45.0, 58.0, 65.0, 88.0, 95.0])

# 2. Compute Least Squares Fit
weights, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
y_hat = X @ weights

# 3. Calculate Error Arrays
residuals = y - y_hat
abs_pct_error = np.abs(residuals / y) * 100

# 4. Tabular Summary Output
print(f"{'Sample':^8}|{'Actual (y)':^12}|{'Pred (ŷ)':^12}|{'Residual (e)':^14}|{'Abs Error %':^12}")
print("-" * 60)
for i in range(len(y)):
    print(f"{i+1:^8}|{y[i]:^12.2f}|{y_hat[i]:^12.2f}|{residuals[i]:^14.4f}|{abs_pct_error[i]:^12.2f}%")
print("-" * 60)

# Summary Evaluation
rmse = np.sqrt(np.mean(residuals**2))
mape = np.mean(abs_pct_error)
print(f"Root Mean Squared Error (RMSE) : {rmse:.4f}")
print(f"Mean Abs Percentage Error (MAPE): {mape:.2f}%")