import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# 1. Element-wise Multiplication (*)
# Multiplying matching index positions directly
elem_wise = A * B
print("Element-wise (A * B):\n", elem_wise)
# Output:
# [[ 1*5  2*6 ]   --> [[ 5 12]
#  [ 3*7  4*8 ]]  -->  [21 32]]

# 2. Matrix Multiplication (@)
# Row-by-column dot products
matrix_mult = A @ B
print("\nMatrix Multiplication (A @ B):\n", matrix_mult)
# Output:
# [[ 1*5 + 2*7   1*6 + 2*8 ]   --> [[19 22]
#  [ 3*5 + 4*7   3*6 + 4*8 ]]  -->  [43 50]]