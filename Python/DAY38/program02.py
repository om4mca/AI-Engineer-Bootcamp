import numpy as np

# Simulate flipping 10 coins, 100,000 times
n_coins = 10
p_heads = 0.5
n_simulations = 100_000

# Generate binomial random sample
simulation = np.random.binomial(n=n_coins, p=p_heads, size=n_simulations)

# Print frequency breakdown
print(f"--- COIN FLIP DISTRIBUTION ({n_coins} Coins, {n_simulations:,} Trials) ---")
for k in range(n_coins + 1):
    count = np.sum(simulation == k)
    prob = count / n_simulations
    bar = "█" * int(prob * 100 / 2)
    print(f"Heads: {k:2d} | {bar:<15} | {prob:.4%}")