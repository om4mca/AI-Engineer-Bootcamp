import numpy as np

# System Coefficients and Constants
A = np.array([
    [2, -1,  3],
    [4,  2, -1],
    [-1, 3,  2]
], dtype=np.float64)

b = np.array([5, 9, 1], dtype=np.float64)

# Form Augmented Matrix [A | b]
augmented_matrix = np.hstack([A, b.reshape(-1, 1)])

print("Coefficient Matrix A:\n", A)
print("\nConstant Vector b:\n", b)
print("\nAugmented Matrix [A | b]:\n", augmented_matrix)