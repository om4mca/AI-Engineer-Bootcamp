import numpy as np

# Define two 2x2 matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Matrix multiplication using @
C = A @ B

print("Result of A @ B:\n", C)
# Output:
# [[19 22]
#  [43 50]]