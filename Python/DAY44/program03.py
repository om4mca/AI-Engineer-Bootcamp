import numpy as np

# 1. Define a 2x2 square matrix
A = np.array([
    [4, 7],
    [2, 9]
])

# 2. Compute determinant
det_A = np.linalg.det(A)

# Print raw float vs rounded value
print("Raw Determinant:", det_A)
print("Rounded Determinant:", round(det_A))