import numpy as np

u = np.array([2, 4, 5])
v = np.array([3, -1, 2])

# Element-wise multiplication (Hadamard product)
hadamard_product = u * v
# Equivalent explicit function: np.multiply(u, v)

print("Hadamard Product (u * v):", hadamard_product)  # Output: [ 6 -4 10]