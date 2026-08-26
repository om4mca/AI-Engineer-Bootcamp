import numpy as np

def safe_matrix_inverse(matrix: np.ndarray):
    """
    Attempts to invert a matrix safely by handling LinAlgError and shape errors.
    Returns (inverse_matrix, status_message).
    """
    A = np.asarray(matrix, dtype=float)

    # 1. Preemptive Validation: Check if matrix is 2D and square
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None, f"Error: Cannot invert non-square matrix of shape {A.shape}."

    # 2. Try Matrix Inversion with Exception Handling
    try:
        A_inv = np.linalg.inv(A)
        return A_inv, "Success: Matrix successfully inverted."

    except np.linalg.LinAlgError as e:
        # Triggered when matrix is singular (determinant is 0) or ill-conditioned
        return None, f"LinAlgError Exception Handled: Matrix is singular (det=0). Details: {e}"


# --- Demonstration with Test Cases ---

# Case 1: Invertible Matrix
A_valid = [[4, 7], [2, 6]]

# Case 2: Singular Matrix (Row 2 is 2x Row 1 -> det = 0)
A_singular = [[1, 2], [2, 4]]

# Case 3: Non-Square Matrix (2x3)
A_nonsquare = [[1, 2, 3], [4, 5, 6]]

for i, test_matrix in enumerate([A_valid, A_singular, A_nonsquare], start=1):
    print(f"--- Test Case #{i} ---")
    inv, message = safe_matrix_inverse(test_matrix)
    print(message)
    if inv is not None:
        print("Inverse Output:\n", np.round(inv, 4))
    print()