import numpy as np

def solve_hospital_capacity(A_matrix: list, b_vector: list, tier_names: list):
    """
    Solves hospital resource allocation A * x = b.
    """
    A = np.array(A_matrix, dtype=np.float64)
    b = np.array(b_vector, dtype=np.float64)
    
    try:
        # Solve for patient capacity vector x
        x = np.linalg.solve(A, b)
        
        print("=== HOSPITAL RESOURCE ALLOCATION SOLVER ===")
        for name, count in zip(tier_names, x):
            print(f"• Optimal {name}: {count:.1f} beds/patients")
            
        # Verify exact solution
        is_valid = np.allclose(A @ x, b)
        print(f"All Constraints Fully Met: {is_valid} ✅")
        return x

    except np.linalg.LinAlgError:
        print("⚠️ Exact matching impossible. Falling back to Least-Squares (np.linalg.lstsq)...")
        x_lstsq, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
        return x_lstsq

# --- SOLVING THE HEALTHCARE SCENARIO ---
# Row 1: Nursing Hours (12*x1 + 6*x2 + 2*x3 = 240)
# Row 2: Equipment    (3*x1  + 1*x2 + 0*x3 = 35)
# Row 3: Daily Cost   (2500*x1 + 1000*x2 + 400*x3 = 32000)
A = [
    [12, 6, 2],
    [3, 1, 0],
    [2500, 1000, 400]
]
b = [240, 35, 32000]
tiers = ["ICU Patients (x1)", "Intermediate Patients (x2)", "General Ward Patients (x3)"]

patient_allocation = solve_hospital_capacity(A, b, tiers)