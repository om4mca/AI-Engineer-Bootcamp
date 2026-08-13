import random
import numpy as np


# --- 1. Die Roll Simulation ---
def simulate_die_even(num_trials=100_000):
    rolls = np.random.randint(1, 7, size=num_trials)
    even_count = np.sum(rolls % 2 == 0)
    p_empirical = even_count / num_trials
    return p_empirical


# --- 2. Two Dice Sum Simulation ---
def simulate_two_dice_sum_even(num_trials=100_000):
    die1 = np.random.randint(1, 7, size=num_trials)
    die2 = np.random.randint(1, 7, size=num_trials)
    sums = die1 + die2
    p_empirical = np.mean(sums % 2 == 0)
    return p_empirical


# Execute
trials = 1_000_000
p_die = simulate_die_even(trials)
p_sum = simulate_two_dice_sum_even(trials)

print(f"Single Die  - Empirical P(Even)       : {p_die:.4f} ({p_die*100:.2f}%)")
print(f"Single Die  - Theoretical P(Even)     : 0.5000 (50.00%)")
print("-" * 55)
print(f"Two Dice    - Empirical P(Sum is Even): {p_sum:.4f} ({p_sum*100:.2f}%)")
print(f"Two Dice    - Theoretical P(Sum Even) : 0.5000 (50.00%)")