import numpy as np

# 1. Coefficient Matrix A and Constant Vector b
A = np.array([
    [ 2,  1, -1],
    [-3, -1,  2],
    [-2,  1,  2]
], dtype=np.float64)

b = np.array([8, -11, -3], dtype=np.float64)

# 2. Solve for x, y, z
x = np.linalg.solve(A, b)

print(f"Solution Vector [x, y, z]: {x}")
print(f"x = {x[0]:.1f}, y = {x[1]:.1f}, z = {x[2]:.1f}")

# 3. Verification
print("Verified (A @ x == b)?", np.allclose(A @ x, b), "✅")