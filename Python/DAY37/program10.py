def bayes_theorem(prior, likelihood, false_positive_rate):
    """Calculates Posterior Probability P(A | B) using Bayes' Theorem.

    :param prior: P(A) - Initial probability of event A
    :param likelihood: P(B | A) - Probability of evidence B given event A
    :param false_positive_rate: P(B | ~A) - Probability of evidence B given NO
    event A
    :return: dict containing Posterior P(A | B) and total Evidence P(B)
    """
    # Probability of NOT A
    p_not_a = 1.0 - prior

    # Total Evidence: P(B) = P(B|A)*P(A) + P(B|~A)*P(~A)
    evidence = (likelihood * prior) + (false_positive_rate * p_not_a)

    # Posterior: P(A|B) = (Likelihood * Prior) / Evidence
    posterior = (likelihood * prior) / evidence

    return {
        "Prior P(A)": prior,
        "Likelihood P(B|A)": likelihood,
        "Evidence P(B)": evidence,
        "Posterior P(A|B)": posterior,
    }


# ==============================================================================
# Example: Classic Medical Disease Test
# ==============================================================================
# Disease Prevalence in population (Prior): 1% -> P(Disease) = 0.01
# Test Sensitivity (Likelihood): 95% -> P(Positive | Disease) = 0.95
# Test False Positive Rate: 5% -> P(Positive | No Disease) = 0.05

prior_disease = 0.01
sensitivity = 0.95
false_pos_rate = 0.05

result = bayes_theorem(
    prior=prior_disease,
    likelihood=sensitivity,
    false_positive_rate=false_pos_rate,
)

print("=== BAYES' THEOREM COMPUTATION ===")
for key, val in result.items():
    print(f"{key:<20}: {val:.4f} ({val:.2%})")