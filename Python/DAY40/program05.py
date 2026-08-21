import math
from scipy.special import comb, perm

class ProbabilityCalculator:
    
    # 1. BASIC SINGLE EVENT PROBABILITY
    @staticmethod
    def event_probability(favorable_outcomes: int, total_outcomes: int) -> float:
        """P(A) = Favorable Outcomes / Total Outcomes"""
        if total_outcomes <= 0:
            raise ValueError("Total outcomes must be greater than zero.")
        return favorable_outcomes / total_outcomes

    # 2. COMBINATORICS (Counting Rules)
    @staticmethod
    def combinations(n: int, r: int) -> int:
        """nCr: Number of ways to choose r items from n (Order does NOT matter)"""
        return int(comb(n, r))

    @staticmethod
    def permutations(n: int, r: int) -> int:
        """nPr: Number of ways to arrange r items from n (Order MATTERS)"""
        return int(perm(n, r))

    # 3. INDEPENDENT EVENTS (AND Rule)
    @staticmethod
    def prob_a_and_b_independent(prob_a: float, prob_b: float) -> float:
        """P(A and B) = P(A) * P(B) for independent events"""
        return prob_a * prob_b

    # 4. MUTUALLY EXCLUSIVE / NON-MUTUALLY EXCLUSIVE EVENTS (OR Rule)
    @staticmethod
    def prob_a_or_b(prob_a: float, prob_b: float, prob_a_and_b: float = 0.0) -> float:
        """P(A or B) = P(A) + P(B) - P(A and B)"""
        return prob_a + prob_b - prob_a_and_b

    # 5. CONDITIONAL PROBABILITY & BAYES' THEOREM
    @staticmethod
    def conditional_prob(prob_a_and_b: float, prob_b: float) -> float:
        """P(A | B) = P(A and B) / P(B)"""
        if prob_b == 0:
            raise ValueError("P(B) cannot be zero for conditional probability.")
        return prob_a_and_b / prob_b

    @staticmethod
    def bayes_theorem(prob_b_given_a: float, prob_a: float, prob_b: float) -> float:
        """P(A | B) = (P(B | A) * P(A)) / P(B)"""
        if prob_b == 0:
            raise ValueError("P(B) cannot be zero.")
        return (prob_b_given_a * prob_a) / prob_b


# ==============================================================================
# EXAMPLE USAGE & DEMONSTRATION
# ==============================================================================
calc = ProbabilityCalculator()

print("--- 1. Single Event ---")
# Rolling a 4 or higher on a standard 6-sided die (3 favorable: 4, 5, 6)
p_die = calc.event_probability(favorable_outcomes=3, total_outcomes=6)
print(f"P(Roll 4+) = {p_die:.2%}")

print("\n--- 2. Combinatorics ---")
# Ways to pick a 5-card hand out of a standard 52-card deck
ways_to_choose = calc.combinations(n=52, r=5)
print(f"Combinations (52 choose 5): {ways_to_choose:,}")

print("\n--- 3. Compound Events ---")
# Rolling two 6s in a row (Independent AND rule)
p_six = 1 / 6
p_two_sixes = calc.prob_a_and_b_independent(p_six, p_six)
print(f"P(Two 6s in a row) = {p_two_sixes:.4f} ({p_two_sixes:.2%})")

# Drawing a Red card (26/52) OR a King (4/52) with 2 Red Kings overlapping
p_red = 26 / 52
p_king = 4 / 52
p_red_king = 2 / 52
p_red_or_king = calc.prob_a_or_b(p_red, p_king, p_red_king)
print(f"P(Red OR King) = {p_red_or_king:.2%}")

print("\n--- 4. Bayes' Theorem ---")
# P(Disease) = 1%, P(Positive | Disease) = 99%, P(Positive Overall) = 5%
p_disease_given_positive = calc.bayes_theorem(
    prob_b_given_a=0.99, 
    prob_a=0.01, 
    prob_b=0.05
)
print(f"P(Disease | Positive Test) = {p_disease_given_positive:.2%}")