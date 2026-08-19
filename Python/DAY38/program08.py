import math
import random


def run_bernoulli_simulation(p_success=0.7, num_trials=10000, seed=42):
    random.seed(seed)

    # 1. Run Simulation: Generate binary outcomes (1 = Success, 0 = Failure)
    trials = [1 if random.random() < p_success else 0 for _ in range(num_trials)]

    # 2. Count Results
    success_count = sum(trials)
    failure_count = num_trials - success_count

    # 3. Calculate Empirical (Simulated) Metrics
    empirical_mean = success_count / num_trials
    empirical_var = sum((x - empirical_mean) ** 2 for x in trials) / num_trials
    empirical_std = math.sqrt(empirical_var)

    # 4. Calculate Theoretical Metrics
    theoretical_mean = p_success
    theoretical_var = p_success * (1 - p_success)
    theoretical_std = math.sqrt(theoretical_var)

    # 5. Display Summary
    print("==================================================")
    print(f"    BERNOULLI TRIAL SIMULATION (N = {num_trials:,})   ")
    print("==================================================")
    print(f"Target Success Probability (p) : {p_success:.2f}")
    print(
        f"Successes (1)                  : {success_count:,} ({empirical_mean:.2%})"
    )
    print(
        f"Failures  (0)                  : {failure_count:,} ({1 - empirical_mean:.2%})\n"
    )

    print("--------------------------------------------------")
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
    print("==================================================")


if __name__ == "__main__":
    run_bernoulli_simulation(p_success=0.7, num_trials=10000)