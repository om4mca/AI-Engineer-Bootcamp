import math
import random
from collections import Counter


def run_binomial_simulation(n_trials=20, p_success=0.8, n_sims=10000, seed=42):
    random.seed(seed)

    # 1. Run Simulation: Sum n Bernoulli trials for each simulated batch
    results = [
        sum(1 if random.random() < p_success else 0 for _ in range(n_trials))
        for _ in range(n_sims)
    ]

    # 2. Compute Frequencies
    freq_dict = Counter(results)
    N = len(results)

    # 3. Calculate Empirical Statistics
    empirical_mean = sum(results) / N
    empirical_var = sum((x - empirical_mean) ** 2 for x in results) / N
    empirical_std = math.sqrt(empirical_var)

    # 4. Calculate Theoretical Statistics
    theoretical_mean = n_trials * p_success
    theoretical_var = n_trials * p_success * (1 - p_success)
    theoretical_std = math.sqrt(theoretical_var)

    # 5. Display Statistical Summary
    print("==================================================")
    print(f"   BINOMIAL SIMULATION: B(n={n_trials}, p={p_success})")
    print(f"   Simulated Batches: {n_sims:,}")
    print("==================================================")
    print(f"{'Metric':<20} | {'Empirical':<12} | {'Theoretical':<12}")
    print("--------------------------------------------------")
    print(
        f"{'Mean E[X]':<20} | {empirical_mean:<12.4f} | {theoretical_mean:<12.4f}"
    )
    print(
        f"{'Variance Var(X)':<20} | {empirical_var:<12.4f} | {theoretical_var:<12.4f}"
    )
    print(
        f"{'Std Dev (Sigma)':<20} | {empirical_std:<12.4f} | {theoretical_std:<12.4f}"
    )
    print("==================================================\n")

    # 6. Display Distribution Histogram
    print("==================================================")
    print("           DISTRIBUTION HISTOGRAM                 ")
    print("==================================================")
    max_freq = max(freq_dict.values())
    max_bar_width = 30

    min_val, max_val = min(results), max(results)
    for k in range(min_val, max_val + 1):
        count = freq_dict.get(k, 0)
        pct = (count / N) * 100
        bar = "█" * int((count / max_freq) * max_bar_width)
        print(
            f"Successes {k:2d} | {bar:<{max_bar_width}} | {count:5d} batches ({pct:5.2f}%)"
        )
    print("==================================================")


if __name__ == "__main__":
    # Simulate 10,000 batches of 20 trials with 80% success probability
    run_binomial_simulation(n_trials=20, p_success=0.8, n_sims=10000)