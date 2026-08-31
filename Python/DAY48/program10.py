import numpy as np

# 1. Setup Sample Data & Design Matrix X
X = np.array([
    [1.0, 1.5, 3.0],
    [1.0, 3.0, 4.0],
    [1.0, 4.5, 3.5],
    [1.0, 6.0, 5.0],
    [1.0, 8.0, 4.5]
])
y = np.array([45.0, 58.0, 65.0, 88.0, 95.0])

# 2. Compute Least Squares Weights
weights, _, _, _ = np.linalg.lstsq(X, y, rcond=None)

# 3. Model Predictions & Residuals
y_hat = X @ weights
residuals = y - y_hat

# --- VERIFICATION CHECKS ---
# Check 1: Point-by-point row calculations match vector predictions
row_by_row_preds = np.array([np.dot(row, weights) for row in X])
pred_check = np.allclose(y_hat, row_by_row_preds)

# Check 2: Sum of residuals is zero (within numerical precision)
sum_residuals = np.sum(residuals)
zero_sum_check = np.isclose(sum_residuals, 0.0, atol=1e-10)

# Check 3: Orthogonality (X^T @ e == 0)
orthogonality = X.T @ residuals
ortho_check = np.allclose(orthogonality, 0.0, atol=1e-10)

# --- OUTPUT DISPLAY ---
print("==================================================")
print("           PREDICTION VERIFICATION REPORT         ")
print("==================================================")
print(f"Computed Weights (w)       : {weights.round(4)}")
print(f"Actual Targets (y)         : {y}")
print(f"Predicted Targets (ŷ)      : {y_hat.round(4)}")
print(f"Residuals (y - ŷ)          : {residuals.round(4)}")
print("--------------------------------------------------")
print(f"1. Vectorized == Row-wise  : {'PASSED' if pred_check else 'FAILED'}")
print(f"2. Sum of Residuals ≈ 0    : {'PASSED' if zero_sum_check else 'FAILED'} (Sum = {sum_residuals:.4e})")
print(f"3. Orthogonality X^T @ e = 0: {'PASSED' if ortho_check else 'FAILED'} (Max dot = {np.max(np.abs(orthogonality)):.4e})")