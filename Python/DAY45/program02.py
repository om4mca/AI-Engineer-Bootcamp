import numpy as np

# Define Matrix
A = np.array([
    [4, 2],
    [1, 3]
])

# Compute Eigenvalues
eigenvalues = np.linalg.eigvals(A)

print("Eigenvalues:", eigenvalues)