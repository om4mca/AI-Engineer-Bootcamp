import numpy as np

# Number of trials
num_simulations = 1_000_000

# 1 = Heads, 0 = Tails
# Generate 2 coin flips per simulation trial
flips = np.random.choice([0, 1], size=(num_simulations, 2))

# Count heads per trial (0, 1, or 2)
heads_count = np.sum(flips, axis=1)

# Calculate empirical probabilities
p_two_heads = np.mean(heads_count == 2)
p_one_head = np.mean(heads_count == 1)
p_zero_heads = np.mean(heads_count == 0)
p_at_least_one = np.mean(heads_count >= 1)

print("=" * 50)
print(f"🪙 TWO COIN TOSS SIMULATION ({num_simulations:,} Trials)")
print("=" * 50)
print(
    f"P(Exactly 2 Heads) : {p_two_heads:.4f} ({p_two_heads*100:.2f}%)  [Theoretical:"
    " 25.00%]"
)
print(
    f"P(Exactly 1 Head)  : {p_one_head:.4f} ({p_one_head*100:.2f}%)  [Theoretical:"
    " 50.00%]"
)
print(
    f"P(0 Heads / 2 Tails): {p_zero_heads:.4f} ({p_zero_heads*100:.2f}%) "
    " [Theoretical: 25.00%]"
)
print(
    f"P(At Least 1 Head) : {p_at_least_one:.4f} ({p_at_least_one*100:.2f}%) "
    " [Theoretical: 75.00%]"
)
print("=" * 50)