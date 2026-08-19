# Calculate expected value for discrete outcomes
outcomes = [8, 0, -2]
probabilities = [1 / 6, 2 / 6, 3 / 6]

# E[X] = sum(x * P(x))
expected_value = sum(x * p for x, p in zip(outcomes, probabilities))

print(f"Expected Value E[X]: ${expected_value:.2f}")
# Output: Expected Value E[X]: $0.33