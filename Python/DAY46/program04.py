import numpy as np

# 1. Define Base Vectors (Columns of matrix V)
v1 = np.array([2, 1])
v2 = np.array([-1, 3])
V = np.column_stack((v1, v2))  # Matrix V (shape: 2x2)

# 2. Define Scalar Coefficient Ranges (c1, c2)
c1_range = np.linspace(-2, 2, 5)  # [-2, -1, 0, 1, 2]
c2_range = np.linspace(-2, 2, 5)  # [-2, -1, 0, 1, 2]

# 3. Generate All Pairs of Coefficients (Grid)
C1, C2 = np.meshgrid(c1_range, c2_range)
coefficients = np.vstack([C1.ravel(), C2.ravel()])  # Shape: 2x25

# 4. Generate Combination Vectors via Matrix Multiplication
# W = V @ C  =>  (2x2) @ (2x25) = (2x25)
generated_vectors = (V @ coefficients).T

print(f"Generated {len(generated_vectors)} vectors spanning the 2D plane.\n")
print("First 5 Generated Vectors [c1*v1 + c2*v2]:")
for i in range(5):
    c1, c2 = coefficients[:, i]
    w = generated_vectors[i]
    print(f"c1={c1:4.1f}, c2={c2:4.1f}  ==>  w = {w}")