class BayesCalculator:
    
    @staticmethod
    def standard_bayes(p_b_given_a: float, p_a: float, p_b: float) -> float:
        """
        Direct Bayes' Theorem calculation.
        P(A|B) = (P(B|A) * P(A)) / P(B)
        """
        if p_b <= 0:
            raise ValueError("P(B) must be greater than zero.")
        return (p_b_given_a * p_a) / p_b

    @staticmethod
    def expanded_bayes(p_b_given_a: float, p_a: float, p_b_given_not_a: float) -> float:
        """
        Bayes' Theorem expanded using the Law of Total Probability.
        P(B) = P(B|A)*P(A) + P(B|~A)*P(~A)
        """
        p_not_a = 1.0 - p_a
        p_b = (p_b_given_a * p_a) + (p_b_given_not_a * p_not_a)
        
        return (p_b_given_a * p_a) / p_b


# --- Example: Medical Diagnosis ---
# Disease Prevalence: P(Disease) = 1% = 0.01
# True Positive Rate (Sensitivity): P(Pos | Disease) = 99% = 0.99
# False Positive Rate: P(Pos | No Disease) = 5% = 0.05

calc = BayesCalculator()

p_disease_given_pos = calc.expanded_bayes(
    p_b_given_a=0.99,       # P(Pos | Disease)
    p_a=0.01,               # P(Disease)
    p_b_given_not_a=0.05    # P(Pos | No Disease)
)

print("--- MEDICAL TEST EXAMPLE ---")
print(f"P(Disease | Positive Test Result) = {p_disease_given_pos:.2%}")