import numpy as np

# ---------------------------------------------------------
# 1. Full-Rank Hospital Feature Matrix
# Features: [Age, Stay Days, Bill ($k), Visits]
# ---------------------------------------------------------
patient_matrix_full = np.array([
    [45,  3,  4.5, 2],
    [62, 10, 15.0, 5],
    [29,  1,  1.8, 1],
    [75,  7, 11.2, 4]
])

shape_full = patient_matrix_full.shape
num_features_full = shape_full[1]
rank_full = np.linalg.matrix_rank(patient_matrix_full)

print("=== FULL-RANK MATRIX ===")
print("Feature Matrix:\n", patient_matrix_full)
print(f"Shape         : {shape_full}")
print(f"Feature Count : {num_features_full}")
print(f"Rank          : {rank_full}\n")

# ---------------------------------------------------------
# 2. Rank-Deficient Hospital Feature Matrix
# We add a 5th column: "Daily_Avg_Bill" = Bill / Stay Days
# Features: [Age, Stay Days, Bill ($k), Visits, Daily_Avg_Bill]
# ---------------------------------------------------------
# Creating exact linear redundancy: Col 5 = Col 3 / Col 2
daily_avg = (patient_matrix_full[:, 2] / patient_matrix_full[:, 1]).reshape(-1, 1)
patient_matrix_redundant = np.hstack([patient_matrix_full, daily_avg])

shape_red = patient_matrix_redundant.shape
num_features_red = shape_red[1]
rank_red = np.linalg.matrix_rank(patient_matrix_redundant)

print("=== REDUNDANT MATRIX ===")
print("Feature Matrix (Rounded):\n", np.round(patient_matrix_redundant, 2))
print(f"Shape         : {shape_red}")
print(f"Feature Count : {num_features_red}")
print(f"Rank          : {rank_red}")