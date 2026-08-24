import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])  # Shape: (2, 3)

# Transpose using .T attribute
A_transposed = A.T

print("Transposed Matrix:\n", A_transposed)
# Output shape: (3, 2)
# [[1 4]
#  [2 5]
#  [3 6]]