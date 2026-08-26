import numpy as np

# 1. Define a 2x2 square matrix
A = np.array([
    [4, 7],
    [2, 6]
])

# 2. Calculate the inverse matrix
A_inv = np.linalg.inv(A)

print("Original Matrix A:\n", A)
print("\nInverse Matrix A^-1:\n", A_inv)