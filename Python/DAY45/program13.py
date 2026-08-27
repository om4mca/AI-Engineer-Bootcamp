import numpy as np

# Employee Feature Matrix
A = np.array([
    [8.0, 4.0, 7.0],
    [4.0, 9.0, 5.0],
    [7.0, 5.0, 8.0]
])

# Compute Eigen-Decomposition
eigenvalues, eigenvectors = np.linalg.eig(A)

# Sort descending
idx = np.argsort(eigenvalues)[::-1]
evals = eigenvalues[idx]
evecs = eigenvectors[:, idx]

print("=== Employee Matrix Eigenvectors ===")
for i in range(len(evals)):
    print(f"\nEigenpair #{i+1}:")
    print(f"  Eigenvalue  (λ_{i+1}) : {evals[i]:.4f}")
    print(f"  Eigenvector (v_{i+1}) : {np.round(evecs[:, i], 4)}")