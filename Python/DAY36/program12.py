import numpy as np

# 1. Simulation Parameters
num_flips = 1_000_000

# 2. Simulate Flips (1 = Heads, 0 = Tails)
# Using fair probability p = 0.5
flips = np.random.choice([0, 1], size=num_flips, p=[0.5, 0.5])

# 3. Calculate Empirical Probabilities
heads_count = np.sum(flips == 1)
tails_count = np.sum(flips == 0)

p_heads = heads_count / num_flips
p_tails = tails_count / num_flips

# 4. Display Results
print("=" * 55)
print(f"🪙 MONTE CARLO COIN TOSS REPORT ({num_flips:,} Flips)")
print("=" * 55)
print(
    f"Heads Count : {heads_count:,} | Empirical P(Heads): {p_heads:.5f}"
    f" ({p_heads*100:.3f}%)"
)
print(
    f"Tails Count : {tails_count:,} | Empirical P(Tails): {p_tails:.5f}"
    f" ({p_tails*100:.3f}%)"
)
print("-" * 55)
print("Theoretical P(Heads) = 0.50000 (50.000%)")
print("Theoretical P(Tails) = 0.50000 (50.000%)")
print(f"Error Margin         = {abs(p_heads - 0.5):.5f}")
print("=" * 55)