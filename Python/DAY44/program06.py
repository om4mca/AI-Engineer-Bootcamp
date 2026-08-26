import numpy as np

# 1. Define Matrix
A = np.array([
    [4, 7],
    [2, 6]
])

# 2. Check Determinant
det_A = np.linalg.det(A)

if not np.isclose(det_A, 0):
    # Calculate Inverse
    A_inv = np.linalg.inv(A)
    print("Matrix Inverse (A^-1):\n", A_inv)
    
    # Verify: A @ A_inv = Identity Matrix
    identity = A @ A_inv
    print("\nVerification (A @ A_inv):\n", np.round(identity, 4))
else:
    print("Matrix is singular and cannot be inverted.")