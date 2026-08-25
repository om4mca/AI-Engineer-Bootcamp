import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

result = A @ B

print(result)

result = np.matmul(A, B)

print(result)

X = np.array([
    [2, 3],
    [4, 5]
])

w = np.array([10, 20])

result = X @ w

print(result)


import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Element-wise:")
print(A * B)

print("Matrix multiplication:")
print(A @ B)

print("Using matmul:")
print(np.matmul(A, B))

print("Transpose:")
print(A.T)