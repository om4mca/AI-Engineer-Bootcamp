import numpy as np

# 1. Initialize generator with a specific seed value (e.g., 42)
rng = np.random.default_rng(seed=42)

# Generate numbers
floats = rng.random(4)
integers = rng.integers(low=1, high=100, size=4)

print("--- Run 1 ---")
print("Floats  :", floats)
print("Integers:", integers)


# 2. Re-initialize generator with the SAME seed to reproduce results
rng_reproduced = np.random.default_rng(seed=42)

floats_again = rng_reproduced.random(4)
integers_again = rng_reproduced.integers(low=1, high=100, size=4)

print("\n--- Run 2 (Same Seed 42) ---")
print("Floats  :", floats_again)
print("Integers:", integers_again)