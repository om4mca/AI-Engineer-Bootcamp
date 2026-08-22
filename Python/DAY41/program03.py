import numpy as np

# 5D feature vector
v = np.array([25, 175.5, 70.0, 120, 45000])

# 1. Total components/elements in the vector (Spatial Dimension)
vector_dimension = v.size          # Output: 5
# OR using shape
vector_dimension_shape = v.shape[0] # Output: 5

# 2. Tensor rank / array dimension (confirms it is 1D)
array_dim = v.ndim                 # Output: 1

print("--- NUMPY VECTOR DIMENSION ---")
print(f"Vector: {v}")
print(f"Vector Dimension (Number of features/elements): {vector_dimension}")
print(f"Array Structural Dimension: {array_dim}D array")