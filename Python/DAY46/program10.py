import numpy as np

# Define matrix A
A = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [0, 1, 5]
])

# Compute Matrix Rank
rank = np.linalg.matrix_rank(A)

print("Matrix A:\n", A)
print(f"Matrix Rank: {rank}")  # Output: 2