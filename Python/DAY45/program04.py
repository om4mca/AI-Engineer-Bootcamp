import numpy as np

# Define a square matrix
A = np.array([
    [4, 2],
    [1, 3]
], dtype=float)

# Compute eigen-decomposition
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues (1D Array):\n", eigenvalues)
print("\nEigenvectors (2D Array - Columns):\n", eigenvectors)