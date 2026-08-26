import numpy as np

# 1. Define Matrix A
A = np.array([
    [4, 7],
    [2, 6]
])

# 2. Compute Inverse
A_inv = np.linalg.inv(A)

# 3. Compute Product
product = A @ A_inv
identity = np.eye(A.shape[0])

# 4. Verification Check
is_verified = np.allclose(product, identity)

print("Product A @ A^-1:\n", np.round(product, 4))
print("\nIs Verified Identity Matrix?", is_verified)