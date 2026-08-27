import numpy as np

# Hospital Operational Matrix [ER, ICU, OR]
A = np.array([
    [12.0, 4.0, 6.0],
    [4.0, 10.0, 2.0],
    [6.0, 2.0, 8.0]
])

# Compute Eigen-Decomposition
eigenvalues, eigenvectors = np.linalg.eig(A)

# Sort descending
idx = np.argsort(eigenvalues)[::-1]
evals = eigenvalues[idx]
evecs = eigenvectors[:, idx]

print("=== HOSPITAL MATRIX EIGEN ANALYSIS ===")
for i in range(len(evals)):
    lam = evals[i]
    v = evecs[:, i]
    
    # Verification using np.allclose
    verified = np.allclose(A @ v, lam * v)
    
    print(f"\nEigenpair #{i+1}:")
    print(f"  Eigenvalue (λ_{i+1})  : {lam:.4f}")
    print(f"  Eigenvector (v_{i+1}) : {np.round(v, 4)}")
    print(f"  Av = λv Verification: {'PASSED ✅' if verified else 'FAILED ❌'}")