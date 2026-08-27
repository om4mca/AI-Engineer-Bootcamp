import numpy as np

A = np.array([
    [4, 2],
    [1, 3]
])

eigenvalues, _ = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)