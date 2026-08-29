import numpy as np

# Create Coefficient Matrix A (3x3)
A = np.array([
    [ 3,  2, -1],
    [-1,  0,  5],
    [ 2, -4,  1]
], dtype=np.float64)

print("Coefficient Matrix A:\n", A)
print("Shape:", A.shape)  # Output: (3, 3)