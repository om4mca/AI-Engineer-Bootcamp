import numpy as np

# Define 3x3 matrix
A = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

# Compute determinant
det_A = np.linalg.det(A)

print("Determinant:", round(det_A))  # Output: 1