import numpy as np

def employee_parameter_solver(A_matrix: list, b_vector: list, roles: list = None):
    """
    Solves for workforce parameters using matrix algebra.
    
    Pipeline: Equations -> Matrix A & Vector b -> np.linalg.solve() -> Verification
    """
    # 1. Pipeline Processing: Convert inputs to NumPy float arrays
    A = np.array(A_matrix, dtype=np.float64)
    b = np.array(b_vector, dtype=np.float64)
    
    # Optional role labeling fallback
    if roles is None:
        roles = [f"Parameter_{i+1}" for i in range(A.shape[1])]
        
    print("==================================================")
    print("          EMPLOYEE PARAMETER SOLVER              ")
    print("==================================================")
    
    # OUTPUT: Display Coefficient Matrix
    print("\nCoefficient Matrix (A):")
    print(A)
    
    # OUTPUT: Display Constant Vector
    print("\nConstant Vector (b):")
    print(b)
    
    # 2. Processing & Error Handling
    # Check 1: Ensure matrix A is square (m == n)
    if A.shape[0] != A.shape[1]:
        print("\n[ERROR] System cannot be solved exactly: Matrix A must be square.")
        print(f"Dimensions provided: {A.shape[0]} equations, {A.shape[1]} parameters.")
        return None

    try:
        # Step: np.linalg.solve()
        x = np.linalg.solve(A, b)
        
        # OUTPUT: Display Solution
        print("\nSolution Vector (x):")
        for role, val in zip(roles, x):
            print(f"  • {role}: {val:.4f}")
            
        # OUTPUT: Verification Step (A @ x == b)
        is_verified = np.allclose(A @ x, b)
        print(f"\nVerification:")
        print(is_verified)
        
        return x

    except np.linalg.LinAlgError as e:
        # Singular Matrix Error Handling
        print("\n[ERROR] Singular Matrix Detected!")
        print(f"Details: {e}")
        print("Reason: The equations are dependent or inconsistent (Determinant = 0).")
        
        # Fallback: Minimum-norm least-squares solution
        x_lstsq, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
        print("\nFallback Solution (Least-Squares / Minimum Norm):")
        for role, val in zip(roles, x_lstsq):
            print(f"  • {role}: {val:.4f}")
            
        return x_lstsq


# =====================================================================
# EXAMPLE USAGE 1: Standard Solvable System
# =====================================================================
# Problem: Allocate Senior & Junior Engineers based on Weekly Budget & Hours
# Row 1 (Hours): 40*Senior + 40*Junior = 200 Total Hours
# Row 2 (Cost) : 2400*Senior + 1200*Junior = 10000 Total Budget ($)
A_valid = [
    [40, 40],
    [2400, 1200]
]
b_valid = [200, 10000]
employee_roles = ["Senior Engineers", "Junior Engineers"]

print("\n--- TEST CASE 1: Standard System ---")
employee_parameter_solver(A_valid, b_valid, employee_roles)


# =====================================================================
# EXAMPLE USAGE 2: Singular Matrix System (Triggers Error Handling)
# =====================================================================
# Row 2 is an exact duplicate/multiple of Row 1 (Dependent system)
A_singular = [
    [40, 40],
    [80, 80]
]
b_singular = [200, 400]

print("\n\n--- TEST CASE 2: Singular Matrix (Error Handling) ---")
employee_parameter_solver(A_singular, b_singular, employee_roles)