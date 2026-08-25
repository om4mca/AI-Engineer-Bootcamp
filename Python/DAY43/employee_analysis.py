import numpy as np

# 1. Create Feature Matrix (X) [3 employees x 3 features]
# Columns: [Experience (years), Projects, Performance Score]
X = np.array([
    [2, 5, 70],
    [5, 8, 85],
    [8, 12, 95]
])

# 2. Create Weight Vector (w) [3 features x 1 weight]
# Weights: Experience=0.2, Projects=0.3, Performance=0.5
w = np.array([
    [0.2],
    [0.3],
    [0.5]
])

# 3. Validate Dimensions for Matrix Multiplication
# Matrix A (m x k) @ Matrix B (k x n) requires inner dimensions to match
rows_X, cols_X = X.shape
rows_w, cols_w = w.shape

print(f"Feature Matrix X shape: {X.shape}")
print(f"Weight Vector w shape:  {w.shape}\n")

if cols_X != rows_w:
    raise ValueError(f"Cannot multiply! Columns of X ({cols_X}) must match rows of w ({rows_w}).")

# 4. Calculate Weighted Scores (X @ w)
scores = X @ w  # Resulting shape: (3, 1)

# 5. Display Each Employee's Score
print("--- Employee Weighted Scores ---")
for i, score in enumerate(scores.flatten()):
    print(f"Employee {i + 1}: {score:.2f}")

# 6. Rank Employees Based on Score
# Get indices that would sort the array in descending order
ranked_indices = np.argsort(scores.flatten())[::-1]

print("\n--- Employee Ranking ---")
for rank, idx in enumerate(ranked_indices, start=1):
    print(f"Rank {rank}: Employee {idx + 1} (Score: {scores[idx][0]:.2f})")