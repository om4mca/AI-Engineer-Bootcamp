import numpy as np

def check_multiplication_compatibility(A: np.ndarray, B: np.ndarray):
    print(f"Shape A: {A.shape} | Shape B: {B.shape}")
    
    # 1. Matrix Multiplication (@) Check
    if A.shape[1] == B.shape[0]:
        print(f"  [VALID] Matrix Multiplication (A @ B) -> Output: ({A.shape[0]}, {B.shape[1]})")
    else:
        print(f"  [INVALID] Matrix Multiplication (A @ B): Inner dims {A.shape[1]} and {B.shape[0]} mismatch.")

    # 2. Element-wise (*) Check
    if A.shape == B.shape:
        print(f"  [VALID] Element-wise (A * B) -> Output: {A.shape}")
    else:
        print(f"  [INVALID] Element-wise (A * B): Shapes {A.shape} and {B.shape} must match exactly.")

# Example test
A = np.ones((2, 3))
B = np.ones((3, 4))

check_multiplication_compatibility(A, B)