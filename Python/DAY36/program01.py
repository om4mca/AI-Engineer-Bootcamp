import random


def simulate_coin_tosses(num_tosses):
    # 'H' for Heads, 'T' for Tails
    outcomes = ["Heads", "Tails"]

    # Perform random tosses
    results = [random.choice(outcomes) for _ in range(num_tosses)]

    # Count occurrences
    heads_count = results.count("Heads")
    tails_count = results.count("Tails")

    # Calculate experimental probabilities
    p_heads = heads_count / num_tosses
    p_tails = tails_count / num_tosses

    return heads_count, tails_count, p_heads, p_tails


# --- Execution ---
num_tosses = 10000
heads, tails, p_heads, p_tails = simulate_coin_tosses(num_tosses)

print("=" * 45)
print(f"🪙 COIN TOSS SIMULATION ({num_tosses:,} Tosses)")
print("=" * 45)
print(f"Heads Count : {heads} | Experimental P(Heads): {p_heads:.4f} ({p_heads*100:.2f}%)")
print(f"Tails Count : {tails} | Experimental P(Tails): {p_tails:.4f} ({p_tails*100:.2f}%)")
print("-" * 45)
print("Theoretical P(Heads) = 0.5000 (50.00%)")
print("Theoretical P(Tails) = 0.5000 (50.00%)")
print("=" * 45)