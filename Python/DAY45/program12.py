import numpy as np

# Define Employee Feature Matrix
A = np.array([
    [8.0, 4.0, 7.0],
    [4.0, 9.0, 5.0],
    [7.0, 5.0, 8.0]
])

# Calculate eigenvalues
eigenvalues = np.linalg.eigvals(A)

# Display calculated eigenvalues sorted descending
sorted_evals = np.sort(eigenvalues)[::-1]

print("=== Employee Matrix Eigenvalues ===")
for i, val in enumerate(sorted_evals, start=1):
    print(f"λ_{i} = {val:.4f}")