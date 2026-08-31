import numpy as np

def identify_system(A, b):
    m, n = A.shape
    print(f"Matrix Shape: {m} rows (equations) x {n} columns (unknowns)")
    
    if m > n:
        print("-> SYSTEM TYPE: Overdetermined (m > n)")
        
        # Check if an exact solution exists or if it requires Least Squares
        x_approx, residuals, rank, _ = np.linalg.lstsq(A, b, rcond=None)
        
        # Calculate residual error
        error = np.linalg.norm(A @ x_approx - b)
        if np.isclose(error, 0):
            print("-> SOLUTION STATUS: Redundant exact solution exists (Zero Error).")
        else:
            print(f"-> SOLUTION STATUS: Inconsistent. Requires Least Squares (RSS Error = {error**2:.4f}).")
            
    elif m == n:
        print("-> SYSTEM TYPE: Determined (m = n)")
    else:
        print("-> SYSTEM TYPE: Underdetermined (m < n)")

# --- Example 1: Overdetermined & Inconsistent System ---
A_over = np.array([
    [1, 2],
    [1, 3],
    [1, 5],
    [1, 7]
])  # 4 rows, 2 columns

b_over = np.array([30, 35, 48, 60])

identify_system(A_over, b_over)