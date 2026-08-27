import numpy as np

# Define Matrix
A = np.array([
    [4.0, 2.0],
    [1.0, 3.0]
])

# Compute Decomposition
eigenvalues, eigenvectors = np.linalg.eig(A)

# Loop through and verify each eigenpair
print("=== EIGENPAIR VERIFICATION ===")
for i in range(len(eigenvalues)):
    lam = eigenvalues[i]
    v = eigenvectors[:, i]  # Extract i-th column vector
    
    left_side = A @ v        # Matrix-vector product
    right_side = lam * v     # Scalar-vector product
    
    # Numerical tolerance check
    is_equal = np.allclose(left_side, right_side)
    
    print(f"\nEigenpair #{i+1} (λ = {lam:.4f}):")
    print(f"  Left Side  (A @ v) : {left_side}")
    print(f"  Right Side (λ * v) : {right_side}")
    print(f"  Equal (np.allclose): {'PASSED ✅' if is_equal else 'FAILED ❌'}")