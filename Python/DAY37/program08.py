def sequential_draw_probability(bag, sequence, with_replacement=False):
    """Calculates the probability of drawing a SPECIFIC SEQUENCE of items.

    :param bag: Dict of item counts, e.g., {'Red': 5, 'Blue': 3, 'Green': 2}
    :param sequence: List of items in order, e.g., ['Red', 'Blue', 'Green']
    :param with_replacement: Bool (False = Dependent, True = Independent)
    :return: Probability float, list of step-by-step probabilities
    """
    current_bag = bag.copy()
    step_probabilities = []
    total_probability = 1.0

    for item in sequence:
        total_items = sum(current_bag.values())

        if total_items == 0 or current_bag.get(item, 0) == 0:
            return 0.0, []  # Impossible sequence

        # Calculate step probability
        p_step = current_bag[item] / total_items
        step_probabilities.append(p_step)
        total_probability *= p_step

        # Update bag if drawing without replacement
        if not with_replacement:
            current_bag[item] -= 1

    return total_probability, step_probabilities


# ==============================================================================
# Example Problem Execution
# ==============================================================================
# Bag contents: 5 Red, 3 Blue, 2 Green (Total = 10 items)
my_bag = {"Red": 5, "Blue": 3, "Green": 2}

# Desired Exact Sequence: Draw Red, then Blue, then Green
draw_sequence = ["Red", "Blue", "Green"]

# 1. Without Replacement (Dependent)
p_no_repl, steps_no_repl = sequential_draw_probability(
    my_bag, draw_sequence, with_replacement=False
)

# 2. With Replacement (Independent)
p_repl, steps_repl = sequential_draw_probability(
    my_bag, draw_sequence, with_replacement=True
)

# Output Results
print("=== SEQUENTIAL DRAWING PROBABILITY ===")
print(f"Bag Contents: {my_bag}")
print(f"Sequence    : {' -> '.join(draw_sequence)}\n")

print("1. WITHOUT REPLACEMENT (Dependent):")
for i, (item, p) in enumerate(zip(draw_sequence, steps_no_repl), 1):
    print(f"   Draw {i} ({item}): {p:.4f}")
print(f"   --> Total Sequential Probability: {p_no_repl:.4f} ({p_no_repl:.2%})\n")

print("2. WITH REPLACEMENT (Independent):")
for i, (item, p) in enumerate(zip(draw_sequence, steps_repl), 1):
    print(f"   Draw {i} ({item}): {p:.4f}")
print(f"   --> Total Sequential Probability: {p_repl:.4f} ({p_repl:.2%})")