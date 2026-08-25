import numpy as np

# 2x2 Matrix A
A = np.array([
    [4, 7],
    [2, 9]
])

# 2x2 Identity Matrix I
I = np.eye(2)

# Multiply A by I
result_right = A @ I
result_left = I @ A

print("A @ I:\n", result_right)
print("I @ A:\n", result_left)
# Both outputs are identical to matrix A:
# [[4 7]
#  [2 9]]