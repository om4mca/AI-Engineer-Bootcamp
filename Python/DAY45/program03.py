import numpy as np

A = np.array([
    [4, 2],
    [1, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

for i in range(len(eigenvalues)):
    print(f"Eigenvalue λ = {eigenvalues[i]:.1f}")
    print(f"Normalized Eigenvector v = {np.round(eigenvectors[:, i], 4)}\n")