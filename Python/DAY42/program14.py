import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# 1. Element-wise Multiplication (A * B)
# Position [0,0]: 1*5=5, Position [0,1]: 2*6=12, etc.
elem_result = A * B
print("Element-wise (A * B):\n", elem_result)
# Output:
# [[ 5 12]
#  [21 32]]

# 2. Matrix Multiplication (A @ B)
# Position [0,0]: (1*5 + 2*7) = 19
# Position [0,1]: (1*6 + 2*8) = 22, etc.
mat_result = A @ B
print("Matrix Multiplication (A @ B):\n", mat_result)
# Output:
# [[19 22]
#  [43 50]]