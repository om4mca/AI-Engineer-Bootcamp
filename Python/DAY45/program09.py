import numpy as np

# 1. Define Matrix
A = np.array([
    [4, 2],
    [1, 3]
], dtype=float)

# 2. Compute Eigen-Decomposition
eigenvalues, eigenvectors = np.linalg.eig(A)

# 3. Match and Display Pairs
print("=== Matched Eigenpairs ===")
for i in range(len(eigenvalues)):
    lam = eigenvalues[i]
    # Extract the i-th column vector
    v = eigenvectors[:, i]
    
    print(f"\nEigenpair #{i+1}:")
    print(f"  Eigenvalue  (λ) : {lam:.4f}")
    print(f"  Eigenvector (v) : {np.round(v, 4)}")