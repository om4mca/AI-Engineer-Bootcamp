class ConditionalProbability:

    @staticmethod
    def p_a_given_b(p_a_and_b: float, p_b: float) -> float:
        """Standard Conditional Probability: P(A | B) = P(A and B) / P(B)"""
        if p_b <= 0:
            raise ValueError("P(B) must be strictly greater than 0.")
        return p_a_and_b / p_b

    @staticmethod
    def bayes_theorem(p_b_given_a: float, p_a: float, p_b: float) -> float:
        """Bayes' Theorem: P(A | B) = (P(B | A) * P(A)) / P(B)"""
        if p_b <= 0:
            raise ValueError("P(B) must be strictly greater than 0.")
        return (p_b_given_a * p_a) / p_b


# --- Example: Medical Testing ---
# Disease Prevalence: P(D) = 1% = 0.01
# Test Sensitivity: P(Pos | D) = 95% = 0.95
# Overall Positive Test Rate: P(Pos) = 5% = 0.05

calc = ConditionalProbability()
p_disease_given_pos = calc.bayes_theorem(p_b_given_a=0.95, p_a=0.01, p_b=0.05)

print("--- ANALYTICAL CONDITIONAL PROBABILITY ---")
print(f"P(Disease | Positive Test) = {p_disease_given_pos:.2%}")