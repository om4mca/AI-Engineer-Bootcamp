import numpy as np

# Sample Dataset (8 rows, 2 features: Age, Salary)
data = np.array([
    [25, 45000],
    [30, 52000],
    [45, 85000],
    [35, 62000],
    [50, 110000],
    [23, 38000],
    [60, 140000],
    [48, 95000]
], dtype=float)

# --- 1. Custom Train/Test Split ---
np.random.seed(42)  # For reproducible splitting
test_ratio = 0.25
n_samples = len(data)
n_test = int(n_samples * test_ratio)

# Shuffle indices randomly
shuffled_indices = np.random.permutation(n_samples)
test_indices = shuffled_indices[:n_test]
train_indices = shuffled_indices[n_test:]

X_train = data[train_indices]
X_test = data[test_indices]

# --- 2. Custom Standardization (StandardScaler Equivalent) ---
# Compute mu and sigma ONLY on training data
mean_train = np.mean(X_train, axis=0)
std_train = np.std(X_train, axis=0)

# Scale both sets using training parameters
X_train_scaled = (X_train - mean_train) / std_train
X_test_scaled = (X_test - mean_train) / std_train

print("--- NUMPY TRAIN/TEST STANDARDIZATION ---")
print("Train Mean (scaled):", np.round(np.mean(X_train_scaled, axis=0), 4))
print("Train Std  (scaled):", np.round(np.std(X_train_scaled, axis=0), 4))
print("\nScaled Test Data:\n", np.round(X_test_scaled, 4))