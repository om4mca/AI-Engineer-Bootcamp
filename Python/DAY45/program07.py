import numpy as np

A = np.array([
    [4, 2],
    [1, 3]
], dtype=float)

eigenvalues, eigenvectors = np.linalg.eig(A)

# Extract the first eigenvalue and first eigenvector (Column 0)
first_eigenvalue = eigenvalues[0]
first_eigenvector = eigenvectors[:, 0]

print(f"First Eigenvalue (λ_1)  : {first_eigenvalue:.4f}")
print(f"First Eigenvector (v_1) : {np.round(first_eigenvector, 4)}")