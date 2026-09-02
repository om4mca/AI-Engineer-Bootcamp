from collections import Counter
import random


class ProbabilitySimulationSystem:
    """Object-Oriented Probability Simulation and Monte Carlo Engine."""

    def __init__(self, seed: int = 42):
        random.seed(seed)

    def simulate_coin_flips(self, n_trials: int = 100000) -> dict:
        """Demonstrates the Law of Large Numbers using large-scale coin tosses."""
        flips = [random.choice(["Heads", "Tails"]) for _ in range(n_trials)]
        counts = Counter(flips)
        head_prob = counts["Heads"] / n_trials
        tail_prob = counts["Tails"] / n_trials
        return {
            "Total Trials": n_trials,
            "Heads Count": counts["Heads"],
            "Tails Count": counts["Tails"],
            "Experimental Head Prob": round(head_prob, 4),
            "Experimental Tail Prob": round(tail_prob, 4),
        }

    def simulate_birthday_paradox(
        self, group_size: int = 23, n_simulations: int = 10000
    ) -> dict:
        """Simulates the Birthday Paradox to calculate probability of shared birthdays."""
        shared_count = 0
        for _ in range(n_simulations):
            birthdays = [random.randint(1, 365) for _ in range(group_size)]
            if len(birthdays) != len(set(birthdays)):
                shared_count += 1

        probability = shared_count / n_simulations
        return {
            "Group Size": group_size,
            "Simulations Run": n_simulations,
            "Shared Birthday Count": shared_count,
            "Estimated Probability": round(probability, 4),
        }

    def monte_carlo_pi(self, n_samples: int = 500000) -> dict:
        """Estimates the value of Pi using geometric Monte Carlo simulation."""
        inside_circle = 0
        for _ in range(n_samples):
            x = random.uniform(0.0, 1.0)
            y = random.uniform(0.0, 1.0)
            if x**2 + y**2 <= 1.0:
                inside_circle += 1

        pi_estimate = 4 * (inside_circle / n_samples)
        error = abs(pi_estimate - 3.141592653589793)
        return {
            "Total Samples": n_samples,
            "Points Inside Circle": inside_circle,
            "Estimated Pi": round(pi_estimate, 5),
            "Approximation Error": round(error, 5),
        }

    def simulate_dice_sum(
        self, n_trials: int = 50000, n_dice: int = 2, target_sum: int = 7
    ) -> dict:
        """Simulates rolling multiple dice to find empirical probability of a target sum."""
        success_count = 0
        for _ in range(n_trials):
            total = sum(random.randint(1, 6) for _ in range(n_dice))
            if total == target_sum:
                success_count += 1

        probability = success_count / n_trials
        return {
            "Dice Count": n_dice,
            "Target Sum": target_sum,
            "Total Trials": n_trials,
            "Estimated Probability": round(probability, 4),
        }


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("      PROBABILITY SIMULATION SYSTEM         ")
    print("============================================\n")

    sim_system = ProbabilitySimulationSystem(seed=42)

    # 1. Law of Large Numbers (Coin Tosses)
    print("--- [1] Law of Large Numbers (Coin Flips) ---")
    coin_res = sim_system.simulate_coin_flips(n_trials=100000)
    for k, v in coin_res.items():
        print(f"  {k:<25}: {v}")

    # 2. Birthday Paradox Simulation
    print("\n--- [2] Birthday Paradox Simulation (Group of 23) ---")
    bday_res = sim_system.simulate_birthday_paradox(group_size=23, n_simulations=10000)
    for k, v in bday_res.items():
        print(f"  {k:<25}: {v}")

    # 3. Monte Carlo Pi Estimation
    print("\n--- [3] Monte Carlo Pi Estimation ---")
    pi_res = sim_system.monte_carlo_pi(n_samples=500000)
    for k, v in pi_res.items():
        print(f"  {k:<25}: {v}")

    # 4. Dice Sum Probability Simulation
    print("\n--- [4] Dice Roll Simulation (Sum of 2 dice == 7) ---")
    dice_res = sim_system.simulate_dice_sum(n_trials=50000, n_dice=2, target_sum=7)
    for k, v in dice_res.items():
        print(f"  {k:<25}: {v}")