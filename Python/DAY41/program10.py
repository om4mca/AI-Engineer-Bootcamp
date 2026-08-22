import numpy as np

v = np.array([3.0, 4.0, 12.0])

# 1. Compute magnitude
magnitude = np.linalg.norm(v)  # ||v|| = sqrt(9 + 16 + 144) = 13.0

# 2. Divide vector by magnitude
v_unit = v / magnitude

print("Original Vector:", v)
print("Normalized Unit Vector (v_hat):", np.round(v_unit, 4))
print("Magnitude of Unit Vector:", np.linalg.norm(v_unit))  # Always 1.0