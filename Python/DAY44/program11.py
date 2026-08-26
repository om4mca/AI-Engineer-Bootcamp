import numpy as np

# Define matrix A
A = np.array([
    [3, 1],
    [4, 2]
])

# Generate 2x2 Identity Matrix
I = np.eye(2)

# Compute Inverse
A_inv = np.linalg.inv(A)

# Verify relationships
print("A @ A_inv equals Identity?", np.allclose(A @ A_inv, I))  # Output: True
print("A_inv @ A equals Identity?", np.allclose(A_inv @ A, I))  # Output: True
print("Inverse of Identity is Identity?", np.allclose(np.linalg.inv(I), I))  # Output: True