# Initial Deck State
total_cards = 52
aces_left = 4

# Step 1: P(1st Card is an Ace) -> P(A)
p_A = aces_left / total_cards

# Step 2: P(2nd Card is an Ace | 1st was an Ace) -> P(B | A)
# (1 Ace and 1 card removed)
p_B_given_A = (aces_left - 1) / (total_cards - 1)

# Step 3: P(3rd Card is an Ace | 1st & 2nd were Aces) -> P(C | A ∩ B)
# (2 Aces and 2 cards removed)
p_C_given_A_and_B = (aces_left - 2) / (total_cards - 2)

# Chain Rule Multiplication: P(A ∩ B ∩ C)
p_three_aces = p_A * p_B_given_A * p_C_given_A_and_B

print(f"P(1st Ace)            : {p_A:.4f}  (4/52)")
print(f"P(2nd Ace | 1st Ace)  : {p_B_given_A:.4f}  (3/51)")
print(f"P(3rd Ace | 1st & 2nd): {p_C_given_A_and_B:.4f}  (2/50)")
print("-" * 40)
print(f"P(All 3 Cards are Aces): {p_three_aces:.6f}  (24/132,600 = 1/5,525)")