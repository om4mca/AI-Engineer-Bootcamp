import numpy as np

def hospital_parameter_solver(A_matrix: list, b_vector: list, system_title: str):
    """
    Solves hospital resource allocation equations A * x = b.
    Tracks matrix creation, vector creation, solving, verification, and error handling.
    """
    print(f"\n==================================================")
    print(f" {system_title.upper()}")
    print(f"==================================================")
    
    # 1. COEFFICIENT MATRIX (A)
    A = np.array(A_matrix, dtype=np.float64)
    print("\nCoefficient Matrix (A):")
    print(A)
    
    # 2. CONSTANT VECTOR (b)
    b = np.array(b_vector, dtype=np.float64)
    print("\nConstant Vector (b):")
    print(b)
    
    # Check Matrix Properties (Determinant & Rank)
    det_A = np.linalg.det(A)
    rank_A = np.linalg.matrix_rank(A)
    n = A.shape[1]
    
    print(f"\nMatrix Diagnostics:")
    print(f"• Determinant : {det_A:.4f}")
    print(f"• Rank        : {rank_A} / {n}")

    # 3. SOLUTION & ERROR HANDLING
    try:
        # Step: np.linalg.solve()
        x = np.linalg.solve(A, b)
        
        print("\nSolution Vector (x):")
        print(f"  • ICU Patients (x1)          : {x[0]:.2f}")
        print(f"  • General Ward Patients (x2) : {x[1]:.2f}")
        
        # 4. VERIFICATION
        verification = np.allclose(A @ x, b)
        print(f"\nVerification (A @ x == b):")
        print(verification)
        return "UNIQUE_SOLUTION"

    except np.linalg.LinAlgError as e:
        # ERROR HANDLING FOR SINGULAR MATRICES
        print("\n⚠️ ERROR HANDLER TRIGGERED: LinAlgError")
        print(f"• Details : {e}")
        print(f"• Reason  : Matrix is Singular (Determinant = 0, Rank {rank_A} < {n}).")
        print("  Equations are redundant/linearly dependent, meaning no unique inverse exists.")
        
        # Fallback Minimum-Norm Least-Squares Solution
        x_fallback, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
        print("\nFallback Solution (Least-Squares / Minimum Norm):")
        print(f"  • ICU Patients (x1)          : {x_fallback[0]:.2f}")
        print(f"  • General Ward Patients (x2) : {x_fallback[1]:.2f}")
        
        verification = np.allclose(A @ x_fallback, b)
        print(f"\nVerification of Fallback Solution (A @ x_fallback == b):")
        print(verification)
        return "SINGULAR_SYSTEM"


# =====================================================================
# SYSTEM 1: UNIQUE SOLUTION
# =====================================================================
# Scenario:
# Row 1 (Nursing Hours): 12 * ICU + 4 * General = 120 hrs
# Row 2 (Daily Budget) : $2000 * ICU + $500 * General = $17,500

A_unique = [
    [12, 4],
    [2000, 500]
]
b_unique = [120, 17500]

hospital_parameter_solver(A_unique, b_unique, "System 1: Unique Solution System")


# =====================================================================
# SYSTEM 2: SINGULAR SYSTEM
# =====================================================================
# Scenario (Redundant Information):
# Row 1 (Nursing Hours)  : 12 * ICU + 4 * General = 120 hrs
# Row 2 (Redundant Shift): 24 * ICU + 8 * General = 240 hrs (Row 2 = 2 * Row 1)

A_singular = [
    [12, 4],
    [24, 8]
]
b_singular = [120, 240]

hospital_parameter_solver(A_singular, b_singular, "System 2: Singular System")