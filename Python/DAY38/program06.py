from collections import Counter
import math
import random


def binomial_pmf(k, n, p):
    """Calculates theoretical PMF using the Binomial formula: P(X = k) = nCr * p^k * (1-p)^(n-k)"""
    combinations = math.comb(n, k)
    return combinations * (p**k) * ((1 - p) ** (n - k))


# Setup parameters: Flipping 5 fair coins (n=5, p=0.5)
n_flips = 5
p_head = 0.5

# 1. Theoretical PMF
theoretical_pmf = {k: binomial_pmf(k, n_flips, p_head) for k in range(n_flips + 1)}

# 2. Empirical PMF (Simulating 10,000 trials)
random.seed(42)
num_trials = 10_000
simulated_data = [
    sum(random.choice([0, 1]) for _ in range(n_flips)) for _ in range(num_trials)
]

counts = Counter(simulated_data)
empirical_pmf = {k: counts[k] / num_trials for k in range(n_flips + 1)}

# 3. Print Comparison Table & ASCII Visualization
print("==================================================")
print("     PMF FOR FLIPPING 5 FAIR COINS (n=5, p=0.5)   ")
print("==================================================")
print(f"{'Heads (k)':<10} | {'Theoretical':<12} | {'Empirical':<12} | {'Histogram'}")
print("-" * 62)

max_p = max(theoretical_pmf.values())
for k in range(n_flips + 1):
    t_p = theoretical_pmf[k]
    e_p = empirical_pmf[k]
    bar = "█" * int((t_p / max_p) * 20)
    print(f"{k:<10} | {t_p:<12.4f} | {e_p:<12.4f} | {bar}")

# Axiom Check: Sum of probabilities must equal 1.0
print("-" * 62)
print(f"Sum of PMF Probabilities: {sum(theoretical_pmf.values()):.1f}")