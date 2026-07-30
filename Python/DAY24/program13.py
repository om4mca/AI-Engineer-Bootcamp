import numpy as np

# Create two 2D arrays (2x3 each)
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

# 1. Vertical Concatenation (axis=0) -> Results in a 4x3 array
concat_v = np.concatenate((a, b), axis=0)

# 2. Horizontal Concatenation (axis=1) -> Results in a 2x6 array
concat_h = np.concatenate((a, b), axis=1)

print("Array A:\n", a)
print("\nArray B:\n", b)

print("\n--- Vertical Concatenation (axis=0) ---")
print(concat_v)

print("\n--- Horizontal Concatenation (axis=1) ---")
print(concat_h)