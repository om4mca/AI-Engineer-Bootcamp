import numpy as np

A = np.array([
    [2, 3],
    [4, -1]
])

b = np.array([10, 6])

solution = np.linalg.solve(A, b)

print(solution)

print(A @ solution)

print(b)

print(np.allclose(A @ solution, b))