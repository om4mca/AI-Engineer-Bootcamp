import numpy as np

# =====================================================================
# 1. EXACT SOLUTION (Consistent System: 2 Equations, 2 Unknowns)
# System: A * x = b  -->  Exact fit with zero residual error
# =====================================================================
A_exact = np.array([
    [2, 1],
    [1, 3]
], dtype=np.float64)

b_exact = np.array([5, 10], dtype=np.float64)

# Solve exactly using direct inversion or np.linalg.solve
x_exact = np.linalg.solve(A_exact, b_exact)
residual_exact = b_exact - (A_exact @ x_exact)

print("=== 1. EXACT SOLUTION ===")
print(f"Matrix A:\n{A_exact}")
print(f"Vector b         : {b_exact}")
print(f"Exact Solution x : {x_exact}")
print(f"Residual Vector  : {residual_exact}")
print(f"Residual Norm    : {np.linalg.norm(residual_exact):.4f} (Zero error)\n")


# =====================================================================
# 2. APPROXIMATE SOLUTION (Overdetermined System: 4 Equations, 2 Unknowns)
# System: X * w ≈ y  --> No exact solution exists due to noise/data mismatch
# =====================================================================
X_overdetermined = np.array([
    [1, 2],
    [1, 3],
    [1, 5],
    [1, 7]
], dtype=np.float64)

y_noisy = np.array([30, 35, 48, 60], dtype=np.float64)

# Solve for optimal weights using Least Squares (SVD-based)
w_approx, rss, rank, s = np.linalg.lstsq(X_overdetermined, y_noisy, rcond=None)

# Compute predictions and residual vector
y_pred = X_overdetermined @ w_approx
residual_approx = y_noisy - y_pred
rss_calc = np.sum(residual_approx**2)

print("=== 2. APPROXIMATE SOLUTION (LEAST SQUARES) ===")
print(f"Design Matrix X:\n{X_overdetermined}")
print(f"Target Vector y        : {y_noisy}")
print(f"Approx Weights w       : {w_approx.round(4)}")
print(f"Predictions ŷ          : {y_pred.round(2)}")
print(f"Residual Vector (y - ŷ): {residual_approx.round(4)}")
print(f"RSS (Error Squared)    : {rss_calc:.4f} (Non-zero minimal error)")