import numpy as np

# Matrix A (3x2)
A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

# Vector x (2x1)
x = np.array([
    [10],
    [20]
])

# Matrix-vector multiplication using @
result = A @ x

print("Result:\n", result)
# Output shape: (3, 1)
# [[1*10 + 2*20]   --> [[ 50]
#  [3*10 + 4*20]   -->  [110]
#  [5*10 + 6*20]]  -->  [170]]