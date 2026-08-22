import numpy as np

v = np.array([3.0, 4.0, 12.0])

# 1. Using np.linalg.norm()
magnitude = np.linalg.norm(v)

# 2. Manual calculation using dot product
magnitude_manual = np.sqrt(np.dot(v, v))

print("Vector Magnitude (norm):", magnitude)         # Output: 13.0
print("Vector Magnitude (manual):", magnitude_manual) # Output: 13.0