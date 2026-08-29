import numpy as np

# Define Coefficient Matrix A (2x2) and Constant Vector b (2,)
A = np.array([
    [2,  3],
    [4, -1]
], dtype=np.float64)

b = np.array([8, 2], dtype=np.float64)

# Method A: np.hstack (reshape b into 2D column first)
aug_matrix = np.hstack([A, b.reshape(-1, 1)])

# Method B: np.c_ shortcut
aug_matrix_alt = np.c_[A, b]

print("Augmented Matrix [A | b]:\n", aug_matrix)
print("Shape:", aug_matrix.shape)  # Output: (2, 3)