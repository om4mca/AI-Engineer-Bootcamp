import numpy as np

A = np.array([
    [4, 2],
    [1, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvector Matrix (Raw 2D Array):")
print(eigenvectors)

print("\nExtracted Eigenvectors (as vectors):")
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    print(f"v_{i+1} (for λ = {eigenvalues[i]:.1f}) = {v}")