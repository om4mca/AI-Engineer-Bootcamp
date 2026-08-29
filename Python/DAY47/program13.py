import numpy as np

def solve_employee_parameters(A_coeffs: list, b_constants: list, param_names: list):
    """
    Solves a system of workforce equations A * x = b.
    
    Parameters:
        A_coeffs: Coefficients of employee variables per equation
        b_constants: Target resource metrics (e.g., budget, total hours)
        param_names: List of employee roles being calculated
    """
    A = np.array(A_coeffs, dtype=np.float64)
    b = np.array(b_constants, dtype=np.float64)
    
    try:
        # Solve exact linear system A * x = b
        x = np.linalg.solve(A, b)
        
        print("=== WORKFORCE PARAMETER SOLVER ===")
        for name, count in zip(param_names, x):
            print(f"• Required {name}: {count:.2f}")
            
        # Verify solution
        is_valid = np.allclose(A @ x, b)
        print(f"Constraints Fully Satisfied: {is_valid} ✅")
        return x

    except np.linalg.LinAlgError:
        print("⚠️ System has no unique solution (Singular Matrix). Falling back to Least-Squares...")
        x_lstsq, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
        return x_lstsq

# --- SOLVING THE BUSINESS PROBLEM ---
# Row 1 (Hours): 40*x1 + 40*x2 = 200
# Row 2 (Cost) : 2400*x1 + 1200*x2 = 10000
A = [
    [40, 40],
    [2400, 1200]
]
b = [200, 10000]
roles = ["Senior Engineers", "Junior Engineers"]

headcount = solve_employee_parameters(A, b, roles)