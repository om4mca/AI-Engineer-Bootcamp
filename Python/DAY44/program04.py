import numpy as np

def check_singular(matrix: np.ndarray) -> bool:
    """Returns True if matrix is singular, False if non-singular."""
    A = np.asarray(matrix, dtype=float)
    
    # 1. Dimension Check: Must be square
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError(f"Matrix must be square. Got shape {A.shape}.")
    
    # 2. Compute Determinant
    det = np.linalg.det(A)
    
    # 3. Check against zero using floating-point tolerance
    return np.isclose(det, 0.0, atol=1e-8)

# --- Test Cases ---

# 1. Non-Singular Matrix (det = 5 != 0)
A_valid = np.array([
    [2, 1],
    [1, 3]
])

# 2. Singular Matrix (Row 2 is 2x Row 1 -> det = 0)
A_singular = np.array([
    [1, 2],
    [2, 4]
])

print("A_valid is singular?", check_singular(A_valid))        # Output: False
print("A_singular is singular?", check_singular(A_singular))  # Output: True