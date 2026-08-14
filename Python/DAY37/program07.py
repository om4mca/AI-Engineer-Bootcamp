import math
from collections import Counter


def bag_ball_probability(
    bag, draws, target_combination, with_replacement=False
):
    """Calculates exact probability of picking a specific combination of balls.

    :param bag: Dict representing ball counts, e.g., {'Red': 5, 'Blue': 3,
    'Green': 2}
    :param draws: Total number of balls drawn from the bag
    :param target_combination: Dict of desired outcome, e.g., {'Red': 2, 'Blue':
    1}
    :param with_replacement: Boolean flag (True = Independent, False =
    Dependent)
    :return: Probability float
    """
    total_balls = sum(bag.values())
    target_draws = sum(target_combination.values())

    if target_draws != draws:
        raise ValueError("Sum of target combination must equal total draws!")

    # ------------------------------------------------------------------
    # Case 1: WITHOUT REPLACEMENT (Hypergeometric Distribution / Dependent)
    # ------------------------------------------------------------------
    if not with_replacement:
        # Total possible ways to draw 'draws' balls from 'total_balls'
        total_ways = math.comb(total_balls, draws)

        favorable_ways = 1
        for color, count in target_combination.items():
            available = bag.get(color, 0)
            if count > available:
                return 0.0  # Impossible draw
            favorable_ways *= math.comb(available, count)

        return favorable_ways / total_ways

    # ------------------------------------------------------------------
    # Case 2: WITH REPLACEMENT (Multinomial Distribution / Independent)
    # ------------------------------------------------------------------
    else:
        # Multinomial coefficient: n! / (k1! * k2! * ...)
        multinomial_coeff = math.factorial(draws)
        for count in target_combination.values():
            multinomial_coeff //= math.factorial(count)

        # Product of individual probabilities raised to their power
        prob_product = 1.0
        for color, count in target_combination.items():
            p_color = bag.get(color, 0) / total_balls
            prob_product *= p_color**count

        return multinomial_coeff * prob_product


# ==============================================================================
# Example Problem Execution
# ==============================================================================
# Bag contents: 5 Red, 3 Blue, 2 Green (Total = 10 balls)
my_bag = {"Red": 5, "Blue": 3, "Green": 2}

# Problem: Draw 3 balls. What is the probability of getting 2 Red and 1 Blue?
desired_draw = {"Red": 2, "Blue": 1, "Green": 0}

p_without = bag_ball_probability(
    bag=my_bag,
    draws=3,
    target_combination=desired_draw,
    with_replacement=False,
)

p_with = bag_ball_probability(
    bag=my_bag,
    draws=3,
    target_combination=desired_draw,
    with_replacement=True,
)

print("=== BAG AND BALL PROBABILITY RESULTS ===")
print(f"Bag Contents                     : {my_bag}")
print(f"Target Outcome (3 draws)         : 2 Red, 1 Blue")
print("-" * 50)
print(f"P(2 Red, 1 Blue | NO Replacement): {p_without:.4f} ({p_without:.2%})")
print(f"P(2 Red, 1 Blue | WITH Replacement): {p_with:.4f} ({p_with:.2%})")