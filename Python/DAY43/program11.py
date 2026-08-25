import numpy as np

A = np.array([[1, 2]])      # (1, 2)
B = np.array([[3, 4], 
              [5, 6]])      # (2, 2)
C = np.array([[1], 
              [2]])         # (2, 1)

# Chain multiplication using @ operator
result = A @ B @ C

print("Result:\n", result)  # [[45]]
print("Shape:", result.shape) # (1, 1)