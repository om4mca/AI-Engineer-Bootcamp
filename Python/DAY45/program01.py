import numpy as np

# 1. Standard Array Definition
A = np.array([
    [4, 7],
    [2, 6]
])

# 2. 2x2 Identity Matrix
I = np.eye(2)

# 3. 2x2 Zero Matrix
Z = np.zeros((2, 2))

# 4. 2x2 Random Matrix
R = np.random.randn(2, 2)

print("Matrix A:\n", A)