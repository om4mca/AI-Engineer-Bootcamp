import numpy as np

# 1. Dataset: Length of Stay (days) vs. Total Hospital Bill ($)
stay_days = np.array([2, 3, 4, 6], dtype=np.float64)
bill = np.array([5000, 7000, 9000, 13000], dtype=np.float64)

# 2. Build Design Matrix X (Column of 1s for Intercept + Stay Days Column)
X = np.column_stack([
    np.ones(len(stay_days)),
    stay_days
])

# 3. Solve for Linear Regression Weights (w0 = Base Cost, w1 = Daily Rate)
weights, _, rank, s = np.linalg.lstsq(X, bill, rcond=None)
w0_intercept, w1_daily_rate = weights[0], weights[1]

# 4. Predictions: y_hat = X @ w
predictions = X @ weights

# 5. Residuals: e = y - y_hat
residuals = bill - predictions

# 6. Residual Sum of Squares (RSS): sum(e_i^2)
RSS = np.sum(residuals**2)

# 7. Mean Squared Error (MSE): RSS / n
MSE = np.mean(residuals**2)

# --- DISPLAY RESULTS ---
print("=== HOSPITAL BILL REGRESSION ANALYSIS ===")
print(f"Design Matrix (X):\n{X}\n")
print(f"Target Vector (y)   : {bill}")
print(f"Fitted Model        : Bill = ${w0_intercept:.2f} + ${w1_daily_rate:.2f}/day\n")
print(f"• Predictions (ŷ)   : {predictions.round(2)}")
print(f"• Residuals (e)     : {residuals.round(2)}")
print(f"• RSS               : {RSS:.2f}")
print(f"• MSE               : {MSE:.2f}")