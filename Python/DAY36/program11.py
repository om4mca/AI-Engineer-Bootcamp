import matplotlib.pyplot as plt
import numpy as np

# 1. Setup Simulation Parameters
num_dice = 2
num_rolls = 100_000

# 2. Simulate Rolls (Random integers between 1 and 6)
# Creates a matrix of shape (num_rolls, num_dice)
rolls = np.random.randint(1, 7, size=(num_rolls, num_dice))

# Sum across dice for each roll
dice_sums = np.sum(rolls, axis=1)

# 3. Compute Empirical Frequencies and Probabilities
possible_sums, counts = np.unique(dice_sums, return_counts=True)
empirical_probs = counts / num_rolls

# 4. Display Results Summary
print("=" * 50)
print(f"🎲 DICE SIMULATION RESULTS ({num_rolls:,} Rolls of {num_dice} Dice)")
print("=" * 50)
print(f"Observed Mean Sum   : {np.mean(dice_sums):.4f} (Expected: {num_dice * 3.5})")
print(
    f"Observed Std Dev    : {np.std(dice_sums):.4f} (Expected:"
    f" {np.sqrt(num_dice * 35/12):.4f})"
)
print("-" * 50)

for sum_val, count, prob in zip(possible_sums, counts, empirical_probs):
    print(f"Sum = {sum_val:2d} | Count = {count:6d} | Probability = {prob*100:6.2f}%")

# 5. Visualizing Distribution
plt.figure(figsize=(10, 5))
plt.bar(possible_sums, empirical_probs, color="royalblue", edgecolor="black", alpha=0.7)
plt.title(f"Empirical Probability Distribution of Rolling {num_dice} Dice ({num_rolls:,} Trials)")
plt.xlabel("Sum of Dice")
plt.ylabel("Probability")
plt.xticks(possible_sums)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()