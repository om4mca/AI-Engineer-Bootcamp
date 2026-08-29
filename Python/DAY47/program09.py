import numpy as np

# 1. Define Coefficient Matrix A and Constant Vector b
A = np.array([
    [2,  3],
    [4, -1]
], dtype=np.float64)

b = np.array([8, 2], dtype=np.float64)

# 2. Solve the linear system
x_calc = np.linalg.solve(A, b)

# 3. Compute predicted b using matrix multiplication (@ operator)
b_pred = A @ x_calc

# 4. Verify solution with np.allclose()
is_valid = np.allclose(b_pred, b)

print("Calculated x :", x_calc)
print("Predicted b  :", b_pred)
print("Original b   :", b)
print("Is Verified? :", is_valid, "✅")