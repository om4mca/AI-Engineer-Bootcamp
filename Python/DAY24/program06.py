import numpy as np

# Set seed for reproducible results
np.random.seed(42)

# 1. 1D Array of 5 random floats between 0.0 and 1.0
rand_1d = np.random.rand(5)

# 2. 2D Array (3 rows, 4 columns) of random floats between 0.0 and 1.0
rand_2d = np.random.rand(3, 4)

# 3. Custom Range: Random floats between 10.0 and 50.0
rand_custom = np.random.uniform(low=10.0, high=50.0, size=(2, 3))

print("--- 1D Random Floats [0.0, 1.0) ---")
print(rand_1d)

print("\n--- 2D Random Floats (3x4) ---")
print(rand_2d)

print("\n--- Custom Range [10.0, 50.0) ---")
print(rand_custom)