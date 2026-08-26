import numpy as np

def analyze_matrix_invertibility(matrix: list | np.ndarray, name: str):
    A = np.asarray(matrix, dtype=float)
    print(f"=== Analyzing Matrix: {name} ===")
    print(f"Matrix A:\n{A}")
    
    # 1. Compute Determinant
    det_A = np.linalg.det(A)
    print(f"Determinant det(A): {det_A:.4f}")
    
    # 2. Check Invertibility Condition: det(A) != 0
    is_invertible = not np.isclose(det_A, 0.0, atol=1e-8)
    print(f"Invertible Condition (det != 0): {is_invertible}")
    
    # 3. Attempt Inversion & Demonstrate det(A^-1) = 1 / det(A)
    if is_invertible:
        A_inv = np.linalg.inv(A)
        det_A_inv = np.linalg.det(A_inv)
        reciprocal_det = 1.0 / det_A
        
        print(f"Inverse A^-1:\n{np.round(A_inv, 4)}")
        print(f"det(A^-1): {det_A_inv:.4f}")
        print(f"1 / det(A): {reciprocal_det:.4f}")
        print(f"Verification det(A^-1) == 1/det(A): {np.isclose(det_A_inv, reciprocal_det)}")
    else:
        print("Matrix is SINGULAR (det = 0). Standard inversion fails!")
        try:
            _ = np.linalg.inv(A)
        except np.linalg.LinAlgError as e:
            print(f"Caught Expected Exception: {e}")
    print("\n" + "-"*50 + "\n")

# --- 1. Non-Singular (Invertible) Matrix ---
# Non-zero determinant (det = 10) -> Area expands by 10x
A_non_singular = [
    [4, 7],
    [2, 6]
]
analyze_matrix_invertibility(A_non_singular, "Non-Singular (det != 0)")

# --- 2. Singular (Non-Invertible) Matrix ---
# Zero determinant (det = 0) -> Row 2 is 2x Row 1 (Linearly Dependent)
# Geometrically squashes 2D space onto a 1D line (area collapses to 0)
A_singular = [
    [1, 2],
    [2, 4]
]
analyze_matrix_invertibility(A_singular, "Singular (det == 0)")