import numpy as np

# 1. Input Features
experience = np.array([2, 5, 8], dtype=np.float64)
education = np.array([1, 2, 3], dtype=np.float64)

# 2. Create Column of Ones (m rows, 1 column)
bias_column = np.ones(len(experience))

# 3. Stack into Design Matrix (X)
X = np.column_stack([bias_column, experience, education])

print("Design Matrix X:")
print(X)
print(f"Shape: {X.shape} (samples x parameters)")