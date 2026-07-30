import numpy as np

# 1. Create a 1D array with 12 elements (0 to 11)
arr_1d = np.arange(12)
print("Original 1D Array:\n", arr_1d)

# 2. Reshape 1D (12 elements) into 2D (3 rows x 4 columns)
arr_2d = arr_1d.reshape(3, 4)
print("\nReshaped 2D Array (3x4):\n", arr_2d)

# 3. Reshape using -1 (NumPy automatically calculates the missing dimension)
# Here, 2 rows are specified, so columns = 12 / 2 = 6
arr_auto = arr_1d.reshape(2, -1)
print("\nReshaped 2D Array with -1 (2x6):\n", arr_auto)