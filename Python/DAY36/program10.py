import numpy as np

# Setup Bag: 6 Red Marbles (1), 4 Blue Marbles (0) -> Total 10
# We want to find P(Draw 2 Red Marbles in a row without replacement)

num_simulations = 1_000_000
success_count = 0

for _ in range(num_simulations):
    # Initial bag setup
    bag = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
    
    # Draw 1st marble randomly
    draw1_idx = np.random.randint(0, len(bag))
    draw1 = bag.pop(draw1_idx)
    
    # Draw 2nd marble from updated bag
    draw2_idx = np.random.randint(0, len(bag))
    draw2 = bag.pop(draw2_idx)
    
    # Check if both are Red (1)
    if draw1 == 1 and draw2 == 1:
        success_count += 1

# Empirical vs Theoretical Calculations
p_empirical = success_count / num_simulations

# Theoretical: P(Red1) * P(Red2 | Red1) = (6/10) * (5/9)
p_theoretical = (6 / 10) * (5 / 9)

print("=" * 55)
print("🔴 MARBLE DRAW SIMULATION (Without Replacement)")
print("=" * 55)
print(f"Theoretical P(2 Red Marbles) : {p_theoretical:.5f} ({p_theoretical*100:.2f}%)")
print(f"Empirical P(1M Simulations)  : {p_empirical:.5f} ({p_empirical*100:.2f}%)")
print("=" * 55)