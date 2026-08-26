import numpy as np

# 1. Create a 3x3 Non-Singular Matrix
A = np.array([
    [3, 0, 2],
    [2, 0, -2],
    [0, 1, 1]
])

# 2. Compute Inverse
A_inv = np.linalg.inv(A)

# 3. Multiply A and A_inv
product = A @ A_inv

# 4. Generate Target Identity Matrix
I = np.eye(3)

# 5. Check Direct Equality vs np.allclose()
exact_match = np.array_equal(product, I)  # Might fail (False)
close_match = np.allclose(product, I)      # Robust check (True)

print("Product A @ A^-1:\n", product)
print("\nExact Equality Check (== / array_equal):", exact_match)
print("np.allclose() Verification Check:", close_match)