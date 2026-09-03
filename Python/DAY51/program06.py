import numpy as np

# 1. Basic Feature Matrix (3 Samples, 4 Features)
# Features: [Age, BloodPressure, Temperature, TestScore]
X_basic = np.array([
    [45, 120, 98.6, 72],  # Sample 1
    [62, 140, 101.2, 85], # Sample 2
    [29, 115, 98.1, 60]   # Sample 3
])

print("--- 1. BASIC FEATURE MATRIX ---")
print(X_basic)
print("Shape (Samples, Features):", X_basic.shape)
print("Data Type:", X_basic.dtype)

# 2. Synthetic Feature Matrix Generation (100 Samples, 3 Features)
# Useful for generating mock ML datasets with uniform/normal distributions
np.random.seed(42)

n_samples = 100

age = np.random.randint(18, 70, size=(n_samples, 1))           # Feature 1
bmi = np.random.normal(25, 4, size=(n_samples, 1))              # Feature 2
income = np.random.uniform(20000, 100000, size=(n_samples, 1))  # Feature 3

# Combine feature columns horizontally into a 2D matrix
X_synthetic = np.hstack((age, bmi, income))

print("\n--- 2. SYNTHETIC FEATURE MATRIX ---")
print("First 5 rows:\n", X_synthetic[:5])
print("Shape:", X_synthetic.shape)

# 3. Adding a Bias Term / Intercept Column (X_0 = 1)
# Essential for manual linear regression implementation: y = X * theta
ones_column = np.ones((X_synthetic.shape[0], 1))
X_with_bias = np.hstack((ones_column, X_synthetic))

print("\n--- 3. FEATURE MATRIX WITH BIAS COLUMN ---")
print("First 3 rows:\n", X_with_bias[:3])
print("Shape:", X_with_bias.shape)

# 4. Feature Standardization (Z-Score Normalization)
# Formula: X_scaled = (X - mean) / std
mean = np.mean(X_synthetic, axis=0)
std = np.std(X_synthetic, axis=0)

X_scaled = (X_synthetic - mean) / std

print("\n--- 4. STANDARDIZED FEATURE MATRIX ---")
print("First 3 scaled rows:\n", X_scaled[:3])
print("Mean per feature (approx 0):", np.round(np.mean(X_scaled, axis=0), 2))
print("Std per feature (approx 1):", np.round(np.std(X_scaled, axis=0), 2))