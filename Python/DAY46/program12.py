import numpy as np

# 1. Define Employee Feature Matrix [Experience, Projects, Performance, Training]
X_full = np.array([
    [2,  5, 70, 3],
    [4,  8, 80, 5],
    [6, 10, 90, 7],
    [8, 12, 95, 9]
])

# 2. Add exact redundant feature: "Project_Rate" = Projects / Experience
project_rate = (X_full[:, 1] / X_full[:, 0]).reshape(-1, 1)
X_redundant = np.hstack([X_full, project_rate])

# 3. Compute Ranks
rank_full = np.linalg.matrix_rank(X_full)
rank_red = np.linalg.matrix_rank(X_redundant)

print("=== EMPLOYEE FEATURE MATRIX RANK ANALYSIS ===")
print(f"Original Matrix Shape : {X_full.shape}  | Rank: {rank_full} / {X_full.shape[1]}")
print(f"Redundant Matrix Shape: {X_redundant.shape}  | Rank: {rank_red} / {X_redundant.shape[1]}")