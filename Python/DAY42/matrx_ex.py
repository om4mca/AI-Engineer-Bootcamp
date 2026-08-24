import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A)

print(A.shape)

rows, columns = A.shape

print("Rows:", rows)
print("Columns:", columns)

I = np.eye(3)

print(I)

Z = np.zeros((2, 3))

print(Z)