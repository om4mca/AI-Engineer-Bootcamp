import numpy as np

# Set seed for reproducible results
np.random.seed(42)

num_simulations = 1_000_000

# Generate 1,000,000 rolls of 3 dice -> Shape: (1000000, 3)
dice_rolls = np.random.randint(1, 7, size=(num_simulations, 3))

# Sum across the 3 dice for each simulation run
dice_sums = np.sum(dice_rolls, axis=1)

# Compute probability P(Sum > 14)
count_gt_14 = np.sum(dice_sums > 14)
p_empirical = np.mean(dice_sums > 14)

print(f"Total Simulations : {num_simulations:,}")
print(f"Favorable Count   : {count_gt_14:,}")
print(f"Empirical P(Sum > 14) = {p_empirical:.5f} ({p_empirical*100:.3f}%)")