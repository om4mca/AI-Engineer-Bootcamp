import numpy as np
import pandas as pd


def run_bayes_medical_simulation(
    population_size=100_000,
    disease_prevalence=0.01,
    sensitivity=0.95,
    specificity=0.95,
    seed=42,
):
    """Simulates a population undergoing a medical test and calculates

    empirical vs. theoretical Bayesian posterior probability P(Disease |
    Positive).

    :param population_size: Total number of simulated patients
    :param disease_prevalence: Prior P(Disease) - base rate in population
    :param sensitivity: Likelihood P(Positive | Disease) - True Positive Rate
    :param specificity: P(Negative | No Disease) - True Negative Rate (1 -
    False Positive Rate)
    :param seed: Random seed for reproducibility
    """
    np.random.seed(seed)

    # 1. Generate Ground Truth: Disease Status (1 = Sick, 0 = Healthy)
    # P(Disease = 1) = disease_prevalence
    disease_status = np.random.choice(
        [1, 0],
        size=population_size,
        p=[disease_prevalence, 1 - disease_prevalence],
    )

    # 2. Simulate Medical Test Results
    # If Disease == 1: P(Positive) = sensitivity
    # If Disease == 0: P(Positive) = 1 - specificity (False Positive Rate)
    test_results = np.zeros(population_size, dtype=int)

    sick_indices = np.where(disease_status == 1)[0]
    healthy_indices = np.where(disease_status == 0)[0]

    # Test sick patients
    test_results[sick_indices] = np.random.choice(
        [1, 0], size=len(sick_indices), p=[sensitivity, 1 - sensitivity]
    )

    # Test healthy patients
    false_positive_rate = 1 - specificity
    test_results[healthy_indices] = np.random.choice(
        [1, 0],
        size=len(healthy_indices),
        p=[false_positive_rate, specificity],
    )

    # Combine into DataFrame
    df = pd.DataFrame(
        {"Disease": disease_status, "TestResult": test_results}
    )

    # ------------------------------------------------------------------
    # 3. Empirical (Simulated) Counts & Probabilities
    # ------------------------------------------------------------------
    total_positive_tests = len(df[df["TestResult"] == 1])
    true_positives = len(df[(df["TestResult"] == 1) & (df["Disease"] == 1)])
    false_positives = len(df[(df["TestResult"] == 1) & (df["Disease"] == 0)])

    empirical_posterior = (
        true_positives / total_positive_tests
        if total_positive_tests > 0
        else 0
    )

    # ------------------------------------------------------------------
    # 4. Theoretical Bayes Calculation
    # Formula: P(D|+) = [P(+|D) * P(D)] / [P(+|D)*P(D) + P(+|~D)*P(~D)]
    # ------------------------------------------------------------------
    prior = disease_prevalence
    likelihood = sensitivity
    evidence = (likelihood * prior) + (false_positive_rate * (1 - prior))

    theoretical_posterior = (likelihood * prior) / evidence

    # ------------------------------------------------------------------
    # 5. Display Simulation Output
    # ------------------------------------------------------------------
    print("==================================================")
    print("      MEDICAL TEST BAYESIAN SIMULATION            ")
    print("==================================================")
    print(f"Simulated Population Size  : {population_size:,}")
    print(f"Disease Prevalence (Prior) : {disease_prevalence:.2%}")
    print(f"Test Sensitivity           : {sensitivity:.2%}")
    print(f"Test Specificity           : {specificity:.2%}")
    print("--------------------------------------------------")
    print("POPULATION BREAKDOWN (Counts):")
    print(f"• Total Sick Patients      : {len(sick_indices):,}")
    print(f"• Total Healthy Patients   : {len(healthy_indices):,}")
    print(f"• True Positives (Sick & +): {true_positives:,}")
    print(f"• False Positives (Healthy & +): {false_positives:,}")
    print(f"• Total Positive Tests     : {total_positive_tests:,}")
    print("--------------------------------------------------")
    print("RESULTS COMPARISON: P(Disease | Positive Test)")
    print(f"• Theoretical Bayes Result : {theoretical_posterior:.2%}")
    print(f"• Empirical Simulation     : {empirical_posterior:.2%}")
    print("==================================================")


# Run Simulation
run_bayes_medical_simulation(
    population_size=100_000,
    disease_prevalence=0.01,  # 1% base rate
    sensitivity=0.95,  # 95% sensitivity
    specificity=0.95,  # 95% specificity (5% false positive rate)
)