import numpy as np

# Define Coefficient Matrix A and Constant Vector b
A = np.array([
    [2,  3],
    [4, -1]
], dtype=np.float64)

b = np.array([8, 2], dtype=np.float64)

# 1. Compute Solution Vector x
x_calc = np.linalg.solve(A, b)

# 2. Recompute constant vector using matrix multiplication (@ operator)
b_recomputed = A @ x_calc

# 3. Method A: Verify using np.allclose (Tolerance Check)
is_valid_close = np.allclose(b_recomputed, b)

# 4. Method B: Verify using Residual Norm ||A x - b||
residual_norm = np.linalg.norm(b_recomputed - b)
is_valid_norm = residual_norm < 1e-10

print("Calculated x         :", x_calc)
print("Recomputed b (A @ x) :", b_recomputed)
print("Original b           :", b)
print("Residual Norm        :", residual_norm)
print("Is Solution Valid?   :", is_valid_close, "✅")