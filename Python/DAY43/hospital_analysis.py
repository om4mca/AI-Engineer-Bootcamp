import numpy as np

# 1. Create Patient Feature Matrix (X) [4 patients x 3 features]
# Columns: [Age (years), StayDays (days), Bill (in thousands $)]
X = np.array([
    [65, 10, 25.0],  # Patient 1
    [28,  2,  3.5],  # Patient 2
    [72, 14, 40.0],  # Patient 3
    [45,  5, 12.0]   # Patient 4
])

# 2. Create Weight Vector (w) [3 features x 1 weight]
# Weights: Age=0.15, StayDays=0.50, Bill=0.35
w = np.array([
    [0.15],
    [0.50],
    [0.35]
])

# 3. Validate Dimensions
print(f"Matrix X shape: {X.shape}")
print(f"Vector w shape: {w.shape}\n")

if X.shape[1] != w.shape[0]:
    raise ValueError("Dimension mismatch! Columns of X must equal rows of w.")

# 4. Calculate Risk Scores (X @ w)
scores = X @ w

# 5. Display Individual Patient Scores
print("--- Patient Numerical Risk Scores ---")
for i, score in enumerate(scores.flatten()):
    print(f"Patient {i + 1}: {score:.2f}")

# 6. Rank Patients (Highest to Lowest)
# Sort indices in descending order based on score
ranked_indices = np.argsort(scores.flatten())[::-1]

print("\n--- Patient Priority Ranking ---")
for rank, idx in enumerate(ranked_indices, start=1):
    print(f"Rank {rank}: Patient {idx + 1} (Score: {scores[idx][0]:.2f})")