import numpy as np

# Define Employee Feature Matrix (Rows: Employees, Columns: Features)
employee_data = np.array([
    [2, 5, 70, 3],
    [4, 8, 80, 5],
    [6, 10, 90, 7],
    [8, 12, 95, 9]
])

# 1. Compute Matrix Shape
shape = employee_data.shape

# 2. Compute Matrix Rank
rank = np.linalg.matrix_rank(employee_data)

# 3. Compute Number of Features (Columns)
num_features = shape[1]

# Display Results
print(f"Matrix Shape       : {shape} ({shape[0]} employees, {shape[1]} features)")
print(f"Number of Features : {num_features}")
print(f"Matrix Rank        : {rank}")