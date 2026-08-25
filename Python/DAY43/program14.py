import numpy as np

# 1. Feature Matrix X (3 samples x 3 features)
X = np.array([
    [2, 5, 70],
    [5, 8, 85],
    [8, 12, 95]
])

# 2. Weight Vector w (3 features x 1 weight)
w = np.array([
    [0.2],
    [0.3],
    [0.5]
])

# 3. Bias term b (scalar baseline score)
b = 5.0

# 4. Compute Prediction Scores: (X @ w) + b
scores = (X @ w) + b

print("Prediction Scores:\n", scores)