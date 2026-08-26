import numpy as np

A = np.array([[4, 7], [2, 6]])
A_inv = np.linalg.inv(A)

product = A @ A_inv
identity = np.eye(2)

# Direct equality fails due to floating-point representation limits
print(np.array_equal(product, identity))  # Output: False

# np.allclose handles floating-point noise correctly
print(np.allclose(product, identity))     # Output: True