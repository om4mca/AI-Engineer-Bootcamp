import numpy as np
import pandas as pd


class BayesianAnalyzer:
    """A framework for discrete and continuous Bayesian analysis."""

    def __init__(self, prior: float, sensitivity: float, specificity: float):
        self.prior = prior
        self.sensitivity = sensitivity
        self.specificity = specificity
        self.false_positive_rate = 1.0 - specificity

    def compute_posterior(self) -> dict:
        """Calculates exact analytical posterior probability."""
        p_h = self.prior
        p_not_h = 1.0 - p_h

        # Likelihoods
        p_e_given_h = self.sensitivity
        p_e_given_not_h = self.false_positive_rate

        # Total Evidence P(E)
        evidence = (p_e_given_h * p_h) + (p_e_given_not_h * p_not_h)

        # Posterior P(H | E)
        posterior = (p_e_given_h * p_h) / evidence

        return {
            "Prior P(H)": p_h,
            "Likelihood P(E|H)": p_e_given_h,
            "False Positive Rate P(E|~H)": p_e_given_not_h,
            "Evidence P(E)": evidence,
            "Posterior P(H|E)": posterior,
        }

    def run_population_simulation(
        self, population_size: int = 100_000, seed: int = 42
    ) -> pd.DataFrame:
        """Simulates a full population to empirically test the Bayesian model."""
        np.random.seed(seed)

        # 1. State Assignment (1 = Disease, 0 = Healthy)
        status = np.random.choice(
            [1, 0],
            size=population_size,
            p=[self.prior, 1.0 - self.prior],
        )

        # 2. Test Execution
        test_results = np.zeros(population_size, dtype=int)
        sick_idx = np.where(status == 1)[0]
        healthy_idx = np.where(status == 0)[0]

        test_results[sick_idx] = np.random.choice(
            [1, 0],
            size=len(sick_idx),
            p=[self.sensitivity, 1.0 - self.sensitivity],
        )
        test_results[healthy_idx] = np.random.choice(
            [1, 0],
            size=len(healthy_idx),
            p=[self.false_positive_rate, self.specificity],
        )

        df = pd.DataFrame({"Actual_Status": status, "Test_Result": test_results})
        return df


# Execute Complete Bayesian Analysis
if __name__ == "__main__":
    analyzer = BayesianAnalyzer(
        prior=0.01, sensitivity=0.95, specificity=0.95
    )

    # Analytical Calculations
    analytical_results = analyzer.compute_posterior()

    print("==================================================")
    print("        ANALYTICAL BAYES ANALYSIS RESULTS         ")
    print("==================================================")
    for key, val in analytical_results.items():
        print(f"{key:<30}: {val:.4f} ({val:.2%})")

    # Empirical Population Simulation Validation
    df_sim = analyzer.run_population_simulation(population_size=100_000)

    pos_tests = df_sim[df_sim["Test_Result"] == 1]
    true_positives = pos_tests[pos_tests["Actual_Status"] == 1]
    empirical_posterior = len(true_positives) / len(pos_tests)

    print("\n==================================================")
    print("      EMPIRICAL POPULATION SIMULATION (100k)      ")
    print("==================================================")
    print(f"Total Positive Tests Generated   : {len(pos_tests):,}")
    print(f"True Positives (Sick & Tested +)  : {len(true_positives):,}")
    print(f"Empirical Posterior P(H | E)     : {empirical_posterior:.2%}")
    print("==================================================")