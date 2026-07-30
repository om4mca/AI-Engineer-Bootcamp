import numpy as np

# Set seed for reproducible results
np.random.seed(42)

# 1. Single random integer between 1 and 100
single_int = np.random.randint(1, 100)

# 2. 1D Array of 5 random integers between 10 and 50
ints_1d = np.random.randint(10, 50, size=5)

# 3. 2D Array (3 rows, 4 columns) of random integers between 1 and 10
ints_2d = np.random.randint(1, 10, size=(3, 4))

print("Single Random Integer   :", single_int)
print("\n--- 1D Random Integers ---")
print(ints_1d)

print("\n--- 2D Random Integers (3x4) ---")
print(ints_2d)