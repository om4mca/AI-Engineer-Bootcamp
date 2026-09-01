import numpy as np

# =====================================================================
# STEP 1 — VECTOR OPERATIONS
# =====================================================================
v1 = np.array([1, 2, 3], dtype=np.float64)
v2 = np.array([4, 5, 6], dtype=np.float64)

v_add = v1 + v2
v_sub = v1 - v2
v_dot = np.dot(v1, v2)
v1_norm = np.linalg.norm(v1)
v2_norm = np.linalg.norm(v2)

print("=" * 60)
print("              STEP 1: VECTOR OPERATIONS")
print("=" * 60)
print(f"Vector v1              : {v1}")
print(f"Vector v2              : {v2}")
print(f"Addition (v1 + v2)     : {v_add}")
print(f"Subtraction (v1 - v2)  : {v_sub}")
print(f"Dot Product (v1 · v2)  : {v_dot:.4f}")
print(f"Norm of v1 (||v1||)    : {v1_norm:.4f}")
print(f"Norm of v2 (||v2||)    : {v2_norm:.4f}\n")


# =====================================================================
# STEP 2 — MATRIX PROPERTIES
# =====================================================================
A = np.array([
    [2, 1],
    [1, 3]
], dtype=np.float64)

A_shape = A.shape
A_transpose = A.T
A_det = np.linalg.det(A)
A_inv = np.linalg.inv(A)
A_rank = np.linalg.matrix_rank(A)
eigenvalues, eigenvectors = np.linalg.eig(A)

print("=" * 60)
print("              STEP 2: MATRIX PROPERTIES")
print("=" * 60)
print(f"Matrix A:\n{A}")
print(f"Shape                 : {A_shape}")
print(f"Transpose (A^T):\n{A_transpose}")
print(f"Determinant det(A)    : {A_det:.4f}")
print(f"Inverse (A^-1):\n{A_inv.round(4)}")
print(f"Rank                  : {A_rank}")
print(f"Eigenvalues           : {eigenvalues.round(4)}")
print(f"Eigenvectors Matrix:\n{eigenvectors.round(4)}\n")


# =====================================================================
# STEP 3 — SOLVE A LINEAR SYSTEM
# =====================================================================
b = np.array([5, 7], dtype=np.float64)

# Solve A * x = b for x
solution = np.linalg.solve(A, b)
verification = np.allclose(A @ solution, b)

print("=" * 60)
print("              STEP 3: SYSTEM SOLVER")
print("=" * 60)
print(f"System Matrix A:\n{A}")
print(f"Vector b               : {b}")
print(f"Solution x             : {solution.round(4)}")
print(f"Verification A @ x == b: {verification}\n")


# =====================================================================
# STEP 4 — LEAST SQUARES REGRESSION
# =====================================================================
X = np.array([
    [1, 1],
    [1, 2],
    [1, 3],
    [1, 4]
], dtype=np.float64)

y = np.array([2, 4, 5, 8], dtype=np.float64)

# Solve overdetermined system X * w ≈ y
weights, residuals_lstsq, rank_X, singular_vals = np.linalg.lstsq(X, y, rcond=None)

# Compute predictions and residual analytics
predictions = X @ weights
residuals = y - predictions
rss = np.sum(residuals**2)
mse = np.mean(residuals**2)

print("=" * 60)
print("              STEP 4: LEAST SQUARES REGRESSION")
print("=" * 60)
print(f"Design Matrix X:\n{X}")
print(f"Target Vector y        : {y}")
print(f"Learned Weights (w)    : {weights.round(4)}")
print(f"Predictions (ŷ)        : {predictions.round(4)}")
print(f"Residual Vector (e)    : {residuals.round(4)}")
print(f"RSS (Sum Sq Errors)    : {rss:.4f}")
print(f"MSE (Mean Sq Error)    : {mse:.4f}")
print("=" * 60)