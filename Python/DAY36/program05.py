import numpy as np


# --- 1. Single Die Simulation ---
def simulate_single_die_gt4(num_trials=100_000):
    rolls = np.random.randint(1, 7, size=num_trials)
    gt4_count = np.sum(rolls > 4)
    p_empirical = gt4_count / num_trials
    return p_empirical


# --- 2. Two Dice Sum Simulation ---
def simulate_two_dice_sum_gt4(num_trials=100_000):
    die1 = np.random.randint(1, 7, size=num_trials)
    die2 = np.random.randint(1, 7, size=num_trials)
    sums = die1 + die2
    p_empirical = np.mean(sums > 4)
    return p_empirical


# Execute Simulation
trials = 1_000_000
p_die = simulate_single_die_gt4(trials)
p_sum = simulate_two_dice_sum_gt4(trials)

print(f"Single Die  - Empirical P(X > 4)    : {p_die:.4f} ({p_die*100:.2f}%)")
print(f"Single Die  - Theoretical P(X > 4)  : 0.3333 (33.33%)")
print("-" * 55)
print(f"Two Dice    - Empirical P(Sum > 4)  : {p_sum:.4f} ({p_sum*100:.2f}%)")
print(f"Two Dice    - Theoretical P(Sum > 4): 0.8333 (83.33%)")