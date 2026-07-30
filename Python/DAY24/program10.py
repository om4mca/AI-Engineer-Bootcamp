import numpy as np

# Create a 1D array with 12 elements (0 to 11)
arr = np.arange(12)
print("Original 1D Array:\n", arr)

# -------------------------------------------------------------
# 1. Specify 3 rows, let NumPy infer columns: -1 => 12 / 3 = 4
# -------------------------------------------------------------
res_cols = arr.reshape(3, -1)
print("\n1. Fixed 3 Rows -> Auto-calculated 4 Columns:\n", res_cols)

# -------------------------------------------------------------
# 2. Specify 2 columns, let NumPy infer rows: -1 => 12 / 2 = 6
# -------------------------------------------------------------
res_rows = arr.reshape(-1, 2)
print("\n2. Auto-calculated 6 Rows -> Fixed 2 Columns:\n", res_rows)

# -------------------------------------------------------------
# 3. Convert 1D array into a 2D Column Vector (12 x 1)
# -------------------------------------------------------------
col_vec = arr.reshape(-1, 1)
print("\n3. Reshape to Column Vector (-1, 1):\n", col_vec)

# -------------------------------------------------------------
# 4. Flatten any multi-dimensional array to 1D using reshape(-1)
# -------------------------------------------------------------
flat_arr = res_cols.reshape(-1)
print("\n4. Flatten back to 1D using reshape(-1):\n", flat_arr)