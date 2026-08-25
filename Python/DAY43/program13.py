import numpy as np

# 1. Feature Matrix X (4 patients x 3 features)
# Features: [Age (years), Length of Stay (days), Total Hospital Bill ($k)]
X = np.array([
    [65, 10, 25.0],  # Patient 1
    [28,  2,  3.5],  # Patient 2
    [72, 14, 40.0],  # Patient 3
    [45,  5, 12.0]   # Patient 4
])

# 2. Weight Vector w (3 weights x 1 column)
# Weights assigned to each feature
w = np.array([
    [0.15],  # Age weight
    [0.50],  # Stay Days weight
    [0.35]   # Bill weight
])

# 3. Calculate Scores (Matrix Multiplication)
scores = X @ w

# 4. Display Results
print("--- Patient Numerical Scores ---")
for i, score in enumerate(scores.flatten(), start=1):
    print(f"Patient {i}: {score:.2f}")