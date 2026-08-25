import numpy as np

A = np.array([[1, 2], 
              [3, 4]])  # (2 x 2)

B = np.array([[5, 6], 
              [7, 8]])  # (2 x 2)

# Matrix Multiplication using the @ operator
C = A @ B

print("Result:\n", C)
# Position [0,0]: (1*5 + 2*7) = 19
# Position [0,1]: (1*6 + 2*8) = 22
# Position [1,0]: (3*5 + 4*7) = 43
# Position [1,1]: (3*6 + 4*8) = 50