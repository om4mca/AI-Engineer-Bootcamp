import numpy as np

# Create a 2x3 matrix
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Transpose using .T property
A_T = A.T

print("Original Shape:", A.shape)  # (2, 3)
print("Transposed Shape:", A_T.shape)  # (3, 2)
print("Transposed Matrix:\n", A_T)