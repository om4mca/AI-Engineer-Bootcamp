import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(A.shape)

print(A[0])
print(A[:, 1])

print(A + B)
print(A - B)

print(2 * A)

print(A.T)

I = np.eye(3)
Z = np.zeros((2, 3))

print(I)
print(Z)