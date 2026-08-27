import numpy as np

A = np.array([
    [2, 0],
    [0, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)

v = eigenvectors[:, 0]
lambda_value = eigenvalues[0]

print(A @ v)
print(lambda_value * v)

print(np.allclose(A @ v, lambda_value * v))