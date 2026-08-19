import random

num_simulations = 100_000
sum_counts = {s: 0 for s in range(2, 13)}

random.seed(42)

# Simulate rolls
for _ in range(num_simulations):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice_sum = die1 + die2
    sum_counts[dice_sum] += 1

# Display results & ASCII Histogram
print("==================================================")
print("     TWO DICE SUM PROBABILITY SIMULATION          ")
print("==================================================")
print(f"Total Rolls: {num_simulations:,}\n")

max_freq = max(sum_counts.values())
for s in range(2, 13):
    count = sum_counts[s]
    pct = (count / num_simulations) * 100
    bar = "█" * int((count / max_freq) * 30)
    print(f"Sum {s:2d} | {bar:<30} | {count:6d} rolls ({pct:5.2f}%)")
print("==================================================")