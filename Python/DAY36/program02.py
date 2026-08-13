import math
import numpy as np

# --- 1. Theoretical Binomial Calculation ---
def binomial_coin_prob(n, k):
    """Calculates theoretical probability of getting k heads in n flips."""
    combinations = math.comb(n, k)
    probability = combinations * (0.5 ** k) * (0.5 ** (n - k))
    return probability

# --- 2. Monte Carlo Simulation ---
def simulate_coin_flips(num_flips, num_trials=100_000):
    """Simulates coin flips using NumPy vectorization."""
    # 1 = Heads, 0 = Tails
    trials = np.random.choice([0, 1], size=(num_trials, num_flips))
    heads_per_trial = np.sum(trials, axis=1)
    return heads_per_trial

# --- Example Run ---
flips = 10
heads_target = 5

# Theoretical
p_theory = binomial_coin_prob(flips, heads_target)

# Empirical Simulation
sim_results = simulate_coin_flips(flips)
p_empirical = np.mean(sim_results == heads_target)

print(f"Coin Flips: {flips} | Target Heads: {heads_target}")
print(f"Theoretical P(Exactly {heads_target} Heads) : {p_theory:.4f} ({p_theory*100:.2f}%)")
print(f"Empirical P(100k Simulations)          : {p_empirical:.4f} ({p_empirical*100:.2f}%)")