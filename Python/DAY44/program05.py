import numpy as np

def is_non_singular(matrix: np.ndarray) -> bool:
    """Returns True if the matrix is non-singular (invertible), False otherwise."""
    A = np.asarray(matrix, dtype=float)
    
    # 1. Dimension Check: Must be square
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError(f"Matrix must be square. Received shape {A.shape}.")
    
    # 2. Calculate Determinant
    det = np.linalg.det(A)
    
    # 3. Check if determinant is safely away from 0 using numerical tolerance
    return not np.isclose(det, 0.0, atol=1e-8)

# --- Test Cases ---

# 1. Non-Singular Matrix (det = 5 != 0)
A_invertible = np.array([
    [2, 1],
    [1, 3]
])

# 2. Singular Matrix (det = 0)
A_singular = np.array([
    [1, 2],
    [2, 4]
])

print("Is A_invertible non-singular?", is_non_singular(A_invertible))  # Output: True
print("Is A_singular non-singular?", is_non_singular(A_singular))      # Output: False