import numpy as np

# Step 1: Define the Dataset
# Features (excluding EmployeeID): [Age, Experience (yrs), Projects, Performance (1-5), Salary ($)]
X = np.array([
    [25, 2, 4, 3, 45000],
    [32, 7, 9, 5, 82000],
    [28, 4, 6, 4, 60000],
    [40, 15, 12, 5, 110000],
    [23, 1, 2, 2, 38000]
])

print("Feature Matrix X:\n", X)
print("-" * 50)

# 1. Number of employees (Rows)
num_employees = X.shape[0]
print("Number of employees:", num_employees)

# 2. Number of features (Columns)
num_features = X.shape[1]
print("Number of features:", num_features)

# 3. Matrix shape
print("Matrix shape:", X.shape)

# 4. First row (First employee's features)
print("First row:", X[0])

# 5. First column (Ages of all employees)
print("First column:", X[:, 0])

# 6. Selected rows (e.g., Row index 1 to 3 -> Employees 2, 3, and 4)
print("Selected rows (Rows 1 to 3):\n", X[1:4])

# 7. Selected columns (e.g., Columns 0, 1, 4 -> Age, Experience, Salary)
print("Selected columns (Age, Experience, Salary):\n", X[:, [0, 1, 4]])

# 8. Transpose of Matrix X
X_transpose = X.T
print("Transpose (X^T):\n", X_transpose)

# 9. Matrix Addition (Adding a dummy bonus/update matrix B of same shape)
B = np.ones((5, 5)) * 10  # Matrix filled with 10s
matrix_sum = X + B
print("Matrix Addition (X + B):\n", matrix_sum)

# 10. Scalar Multiplication (e.g., Scaling all features by 1.1)
scalar_mult = X * 1.1
print("Scalar Multiplication (X * 1.1):\n", scalar_mult)