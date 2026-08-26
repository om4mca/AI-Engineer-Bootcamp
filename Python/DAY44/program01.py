import numpy as np

# 1. Manual Calculation
a, b, c, d = 4, 7, 2, 9
det_manual = (a * d) - (b * c)

# 2. NumPy Calculation
A = np.array([[4, 7], 
              [2, 9]])
det_numpy = np.linalg.det(A)

print("Manual Determinant:", det_manual)
print("NumPy Determinant:", round(det_numpy))