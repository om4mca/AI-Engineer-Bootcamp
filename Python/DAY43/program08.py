import numpy as np

# Row vector x (1x2)
x = np.array([[2, 3]])

# Matrix A (2x3)
A = np.array([
    [1, 0, 4],
    [2, 5, 1]
])

# Vector-matrix multiplication using @
result = x @ A

print("Result:\n", result)
# Output shape: (1, 3)
# [[ (2*1 + 3*2)  (2*0 + 3*5)  (2*4 + 3*1) ]]
# -> [[ 8 15 11 ]]