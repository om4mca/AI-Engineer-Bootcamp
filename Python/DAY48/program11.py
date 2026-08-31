import numpy as np

def analyze_matrix_rank(X, name="Design Matrix"):
    m, p = X.shape  # m samples, p parameters (n features + 1 bias)
    
    # 1. Compute Matrix Rank
    rank = np.linalg.matrix_rank(X)
    
    # 2. Compute Singular Values via SVD
    _, s, _ = np.linalg.svd(X)
    
    # 3. Compute Condition Number: ratio of max to min singular value
    # High condition number (> 30) indicates severe multicollinearity
    cond_num = np.linalg.cond(X)
    
    print(f"=== {name} Analysis ===")
    print(f"Matrix Shape         : {m} samples x {p} parameters")
    print(f"Computed Rank        : {rank}")
    print(f"Singular Values      : {np.round(s, 4)}")
    print(f"Condition Number     : {cond_num:.4f}")
    
    if rank == p and cond_num < 30:
        print("Status               : FULL RANK (Stable unique solution exists)")
    elif rank == p and cond_num >= 30:
        print("Status               : FULL RANK but ILL-CONDITIONED (Near multicollinearity)")
    else:
        print("Status               : RANK DEFICIENT (Multicollinearity present, non-invertible X^T X)\n")

# --- Case 1: Full Rank Matrix ---
X_full = np.array([
    [1, 2, 35],
    [1, 3, 45],
    [1, 5, 52],
    [1, 7, 60],
    [1, 8, 68]
], dtype=np.float64)

# --- Case 2: Rank Deficient Matrix (Column 3 = 2 * Column 1) ---
X_deficient = np.array([
    [1, 2, 4],
    [1, 3, 6],
    [1, 5, 10],
    [1, 7, 14],
    [1, 8, 16]
], dtype=np.float64)

analyze_matrix_rank(X_full, "Full Rank System")
analyze_matrix_rank(X_deficient, "Rank Deficient System")