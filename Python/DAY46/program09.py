import numpy as np

# Define vectors spanning the subspace W
v1 = np.array([1, 2, 1])
v2 = np.array([2, 4, 2])  # Note: v2 = 2 * v1 (linearly dependent)
v3 = np.array([0, 1, 3])

# Stack as columns of matrix A
A = np.column_stack([v1, v2, v3])

# Compute dimension via matrix rank
subspace_dim = np.linalg.matrix_rank(A)

print("=== VECTOR SPACE DIMENSION ===")
print("Matrix Shape:", A.shape)
print("Subspace Dimension dim(W):", subspace_dim)
print("Geometric Type:", "2D Plane" if subspace_dim == 2 else "Other")