import numpy as np

# 1. Define Square Matrix
A = np.array([
    [4.0, 2.0],
    [1.0, 3.0]
])

# 2. Compute Eigen-Decomposition
eigenvalues, eigenvectors = np.linalg.eig(A)

# 3. Verify All Eigenpairs Simultaneously
all_passed = True

print("=== VERIFYING Av ≈ λv WITH np.allclose() ===")
for i in range(len(eigenvalues)):
    lam = eigenvalues[i]
    v = eigenvectors[:, i]  # Column vector slice
    
    left = A @ v      # Matrix-vector multiplication
    right = lam * v   # Scalar-vector multiplication
    
    # Check floating-point equality (rtol=1e-05, atol=1e-08 by default)
    passed = np.allclose(left, right)
    
    if not passed:
        all_passed = False
        
    print(f"Eigenpair #{i+1} (λ = {lam:.4f}): {'PASSED ✅' if passed else 'FAILED ❌'}")

print(f"\nOverall System Verification: {'ALL PASSED ✅' if all_passed else 'FAILED ❌'}")