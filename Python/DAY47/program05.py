import numpy as np

# Method A: Standard 1D Array (commonly used in solvers like np.linalg.solve)
b_1d = np.array([7, 4, -1], dtype=np.float64)

# Method B: 2D Column Vector (m x 1 matrix shape)
b_column = np.array([[7], [4], [-1]], dtype=np.float64)

print("1D Vector b:", b_1d, "Shape:", b_1d.shape)        # Shape: (3,)
print("\n2D Column Vector b:\n", b_column)
print("Shape:", b_column.shape)                          # Shape: (3, 1)