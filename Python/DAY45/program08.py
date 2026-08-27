import numpy as np

A = np.array([
    [4, 2],
    [1, 3]
], dtype=float)

eigenvalues, eigenvectors = np.linalg.eig(A)

# Extract the second eigenvalue and second eigenvector (Column 1)
second_eigenvalue = eigenvalues[1]
second_eigenvector = eigenvectors[:, 1]

print(f"Second Eigenvalue (λ_2)  : {second_eigenvalue:.4f}")
print(f"Second Eigenvector (v_2) : {np.round(second_eigenvector, 4)}")