import numpy as np

def analyze_linear_system(A_matrix: list, b_vector: list, tol: float = 1e-10):
    """
    Analyzes the solvability, rank, and condition number of A x = b.
    """
    A = np.array(A_matrix, dtype=np.float64)
    b = np.array(b_vector, dtype=np.float64)
    
    m, n = A.shape
    b_col = b.reshape(-1, 1)
    aug_matrix = np.hstack([A, b_col])
    
    # Calculate Ranks using Singular Value Decomposition (SVD) tolerance
    rank_A = np.linalg.matrix_rank(A, tol=tol)
    rank_aug = np.linalg.matrix_rank(aug_matrix, tol=tol)
    
    print("================ LINEAR SYSTEM SOLUTION ANALYZER ================")
    print(f"• System Dimensions : {m} equations, {n} variables")
    print(f"• Rank(A)           : {rank_A}")
    print(f"• Rank([A | b])     : {rank_aug}")
    
    # 1. Check Solvability Status
    if rank_A < rank_aug:
        status = "INCONSISTENT (No Solution)"
        details = "The constant vector b lies outside the column space of A."
        solution = None

    elif rank_A == rank_aug == n:
        status = "CONSISTENT (1 Unique Solution)"
        details = "Full column rank achieved."
        solution = np.linalg.solve(A, b) if m == n else np.linalg.lstsq(A, b, rcond=None)[0]

    else: # rank_A == rank_aug < n
        status = f"CONSISTENT (Infinitely Many Solutions)"
        free_vars = n - rank_A
        details = f"Rank deficiency detected. System has {free_vars} free variable(s)."
        # Compute minimum-norm particular solution using SVD / Pseudo-Inverse
        solution, _, _, _ = np.linalg.lstsq(A, b, rcond=None)

    print(f"• Status            : {status}")
    print(f"• Diagnostic        : {details}")
    
    if solution is not None:
        print(f"• Solution Vector x : {solution.round(4)}")
        
    return {
        "status": status,
        "rank_A": rank_A,
        "rank_aug": rank_aug,
        "solution": solution
    }

# --- TEST 1: Unique Solution (2x2) ---
A1 = [[2, 3], [4, -1]]
b1 = [8, 2]
analyze_linear_system(A1, b1)

print("\n")

# --- TEST 2: Inconsistent / No Solution (0 = 7) ---
A2 = [[1, 2], [2, 4]]
b2 = [5, 3]
analyze_linear_system(A2, b2)

print("\n")

# --- TEST 3: Infinite Solutions (Dependent Equations) ---
A3 = [[1, 2], [2, 4]]
b3 = [5, 10]
analyze_linear_system(A3, b3)