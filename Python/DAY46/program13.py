import numpy as np

# 1. Base Hospital Feature Matrix: [Age, Stay Days, Total Bill ($k), Visits]
H_base = np.array([
    [45,  3,  4.5, 2],
    [62, 10, 15.0, 5],
    [29,  1,  1.8, 1],
    [75,  7, 11.2, 4]
], dtype=np.float64)

# 2. Add Redundant Feature: Daily Average Bill = Total Bill / Stay Days
daily_avg = (H_base[:, 2] / H_base[:, 1]).reshape(-1, 1)
H_redundant = np.hstack([H_base, daily_avg])

# 3. Compute Matrix Metrics
rank_base = np.linalg.matrix_rank(H_base)
rank_redundant = np.linalg.matrix_rank(H_redundant)
cond_base = np.linalg.cond(H_base)
cond_redundant = np.linalg.cond(H_redundant)

print("=== HOSPITAL FEATURE MATRIX ANALYSIS ===")
print(f"Base Matrix Shape      : {H_base.shape}  | Rank: {rank_base} / {H_base.shape[1]}")
print(f"Redundant Matrix Shape : {H_redundant.shape}  | Rank: {rank_redundant} / {H_redundant.shape[1]}")
print(f"Base Condition Number  : {cond_base:.2f}")
print(f"Redundant Condition No : {cond_redundant:.2f} (High instability)")