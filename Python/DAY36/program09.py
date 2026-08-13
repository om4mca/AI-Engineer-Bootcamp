import numpy as np

# Simulate 1,000,000 trials
num_trials = 1_000_000

# Event A: Flip a fair coin (1 = Heads, 0 = Tails)
coin_flips = np.random.choice([0, 1], size=num_trials)

# Event B: Roll a fair die (1 to 6)
die_rolls = np.random.randint(1, 7, size=num_trials)

# Calculate individual probabilities
p_heads = np.mean(coin_flips == 1)
p_roll_6 = np.mean(die_rolls == 6)

# Calculate joint probability P(Heads AND Roll 6)
p_joint_empirical = np.mean((coin_flips == 1) & (die_rolls == 6))

# Theoretical product P(A) * P(B)
p_joint_theoretical = p_heads * p_roll_6

print(f"P(Heads)                 : {p_heads:.4f}")
print(f"P(Roll 6)                : {p_roll_6:.4f}")
print("-" * 45)
print(f"P(A) * P(B) Calculated  : {p_joint_theoretical:.4f}")
print(f"P(A AND B) Simulated     : {p_joint_empirical:.4f}")
print("-" * 45)
print(
    f"Difference: {abs(p_joint_theoretical - p_joint_empirical):.6f} (Proves"
    " Independence!)"
)