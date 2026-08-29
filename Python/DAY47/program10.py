import numpy as np

def analyze_matrix_singularity(A: np.ndarray, tol: float = 1e-12) -> dict:
    """
    Analyzes a coefficient matrix A for singularity using Determinant, Rank, and Condition Number.
    """
    m, n = A.shape
    if m != n:
        return {"is_square": False, "is_singular": True, "reason": "Matrix is non-square"}
    
    # 1. Compute Determinant
    det_val = np.linalg.det(A)
    
    # 2. Compute Matrix Rank
    rank_val = np.linalg.matrix_rank(A)
    
    # 3. Compute Condition Number
    cond_num = np.linalg.cond(A)
    
    # Singularity decision criteria
    is_singular = (rank_val < n) or (abs(det_val) < tol) or (cond_num > 1e14)
    
    return {
        "is_square": True,
        "determinant": det_val,
        "rank": f"{rank_val} / {n}",
        "condition_number": cond_num,
        "is_singular": is_singular
    }

# --- TEST DATASETS ---
# Singular Matrix (Row 2 is 2x Row 1 -> Rank Deficient)
A_singular = np.array([
    [1,  2,  3],
    [2,  4,  6],
    [5,  7,  9]
], dtype=np.float64)

# Non-Singular Full-Rank Matrix
A_valid = np.array([
    [2,  1, -1],
    [-3, -1, 2],
    [-2, 1,  2]
], dtype=np.float64)

print("=== SINGULAR MATRIX DIAGNOSTIC ===")
print("Singular Matrix Result :", analyze_matrix_singularity(A_singular))
print("\nValid Matrix Result    :", analyze_matrix_singularity(A_valid))