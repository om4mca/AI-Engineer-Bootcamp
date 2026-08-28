import numpy as np

A = np.array([
    [1, 2],
    [2, 4]
])

rank = np.linalg.matrix_rank(A)

print(rank)

B = np.array([
    [1, 2],
    [3, 4]
])

print(np.linalg.matrix_rank(B))