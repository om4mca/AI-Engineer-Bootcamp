import numpy as np

# 1. Feature Matrix X (3 employees x 3 features)
# Columns: [Experience (years), Projects Completed, Peer Review Score (0-100)]
X = np.array([
    [2,  5, 70],  # Employee 1
    [5,  8, 85],  # Employee 2
    [8, 12, 95]   # Employee 3
])

# 2. Weight Vector w (3 weights x 1 column)
# Importance: Experience=20%, Projects=30%, Peer Review=50%
w = np.array([
    [0.2],
    [0.3],
    [0.5]
])

# 3. Calculate Scores (Matrix Multiplication)
scores = X @ w

# Display Individual Results
print("--- Weighted Scores ---")
for i, score in enumerate(scores.flatten(), start=1):
    print(f"Employee {i}: {score:.2f}")