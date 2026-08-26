import numpy as np

A = np.array([
    [4, 2],
    [3, 1]
])

det_A = np.linalg.det(A)

print(det_A)

import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

A_inv = np.linalg.inv(A)

print(A_inv)

result = A @ A_inv

print(result)

print(np.allclose(A @ A_inv, np.eye(2)))

A = np.array([
    [1, 2],
    [2, 4]
])

np.linalg.inv(A)

try:
    inverse = np.linalg.inv(A)
    print(inverse)

except np.linalg.LinAlgError:
    print("Matrix is singular and cannot be inverted.")

    