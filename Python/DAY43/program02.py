import numpy as np

def check_matrix_compatibility(A: np.ndarray, B: np.ndarray) -> bool:
    shape_A = A.shape
    shape_B = B.shape
    
    print(f"Matrix A shape: {shape_A}")
    print(f"Matrix B shape: {shape_B}")
    
    # Compare inner dimensions: A's columns (shape_A[1]) vs B's rows (shape_B[0])
    if shape_A[1] == shape_B[0]:
        print(f"Valid! Result shape will be ({shape_A[0]}, {shape_B[1]})\n")
        return True
    else:
        print(f"Invalid! Inner dimensions {shape_A[1]} and {shape_B[0]} do not match.\n")
        return False

# --- Test Cases ---
A = np.zeros((2, 3))
B = np.zeros((3, 4))
C = np.zeros((2, 2))

check_matrix_compatibility(A, B)  # Valid: (2, 3) @ (3, 4)
check_matrix_compatibility(A, C)  # Invalid: (2, 3) @ (2, 2)