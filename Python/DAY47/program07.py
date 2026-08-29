import numpy as np

# System of equations:
# 2x + 3y = 8
# 4x - 1y = 2

# 1. Define Coefficient Matrix A and Constant Vector b
A = np.array([
    [2,  3],
    [4, -1]
], dtype=np.float64)

b = np.array([8, 2], dtype=np.float64)

# 2. Solve for variable vector x
x = np.linalg.solve(A, b)

# 3. Output and Verification
print("=== NUMPY LINEAR SYSTEM SOLVER ===")
print(f"Solution Vector x: {x}")  # Output: [1.  2.]
print(f"x = {x[0]:.2f}, y = {x[1]:.2f}")

# Verify solution (A @ x should equal b)
is_valid = np.allclose(A @ x, b)
print(f"Solution Verified (A @ x == b): {is_valid} ✅")