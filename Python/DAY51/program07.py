import numpy as np

# 1. Target Vector for Regression (Continuous Numerical Values)
# Example: House prices (in thousands of dollars) or Salaries
y_regression = np.array([350.5, 420.0, 210.8, 510.2, 315.0])

print("--- 1. REGRESSION TARGET VECTOR ---")
print("Vector:", y_regression)
print("Shape :", y_regression.shape)  # 1D array with shape (N,)
print("Dtype :", y_regression.dtype)


# 2. Target Vector for Binary Classification (0 or 1)
# Example: Email Spam (1 = Spam, 0 = Not Spam)
y_binary = np.array([1, 0, 0, 1, 0])

print("\n--- 2. BINARY CLASSIFICATION TARGET VECTOR ---")
print("Vector:", y_binary)
print("Unique Classes:", np.unique(y_binary))


# 3. Target Vector for Multi-Class Classification (Encoded Labels)
# Example: Patient Risk Level (0 = Low, 1 = Medium, 2 = High)
y_multiclass = np.array([0, 2, 1, 0, 2, 1, 1, 0])

print("\n--- 3. MULTI-CLASS TARGET VECTOR ---")
print("Vector:", y_multiclass)
print("Unique Classes:", np.unique(y_multiclass))


# 4. Generating a Synthetic Target Vector using a Math Relationship
# Formula: y = 2*X1 + 3*X2 + noise (Linear Regression Ground Truth)
np.random.seed(42)
n_samples = 5

# Synthetic 2-feature matrix X
X = np.random.rand(n_samples, 2)

# True weights and bias
weights = np.array([2.0, 3.0])
bias = 5.0
noise = np.random.normal(0, 0.1, size=n_samples)

# Matrix-vector multiplication to compute synthetic target y
y_synthetic = (X @ weights) + bias + noise

print("\n--- 4. SYNTHETIC MATHEMATICAL TARGET VECTOR ---")
print("Features X:\n", np.round(X, 2))
print("Target y  :", np.round(y_synthetic, 2))
print("y Shape   :", y_synthetic.shape)