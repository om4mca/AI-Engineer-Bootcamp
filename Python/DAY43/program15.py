import numpy as np

class MatrixValidator:
    """Validates dimensions and executes matrix operations safely."""

    @staticmethod
    def validate_and_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
        """Checks dimensions and performs matrix multiplication (A @ B)."""
        A = np.asarray(A)
        B = np.asarray(B)

        print(f"Matrix A shape: {A.shape}")
        print(f"Matrix B shape: {B.shape}")

        # Check compatibility: A's columns must equal B's rows
        if A.ndim < 2 or B.ndim < 2:
            raise ValueError("Both inputs must be at least 2D matrices.")

        if A.shape[1] != B.shape[0]:
            raise ValueError(
                f"Incompatible shapes for matrix multiplication: "
                f"Inner dimensions {A.shape[1]} (cols of A) and {B.shape[0]} (rows of B) do not match."
            )

        print(f"Compatibility status: VALID")
        print(f"Expected output shape: ({A.shape[0]}, {B.shape[1]})\n")

        # Execute matrix multiplication
        result = A @ B
        return result

    @staticmethod
    def check_all_operations(A: np.ndarray, B: np.ndarray):
        """Runs a diagnostic check across common matrix multiplication modes."""
        A, B = np.asarray(A), np.asarray(B)
        
        print("=" * 50)
        print("MATRIX COMPATIBILITY DIAGNOSTIC")
        print("=" * 50)
        print(f"A shape: {A.shape} | B shape: {B.shape}\n")

        # 1. Standard Matrix Multiplication (A @ B)
        if A.shape[1] == B.shape[0]:
            print(f"[✓] Matrix Multiplication (A @ B): VALID -> Output shape {(A.shape[0], B.shape[1])}")
        else:
            print(f"[X] Matrix Multiplication (A @ B): INVALID -> {A.shape[1]} != {B.shape[0]}")

        # 2. Reverse Matrix Multiplication (B @ A)
        if B.shape[1] == A.shape[0]:
            print(f"[✓] Reverse Multiplication (B @ A): VALID -> Output shape {(B.shape[0], A.shape[1])}")
        else:
            print(f"[X] Reverse Multiplication (B @ A): INVALID -> {B.shape[1]} != {A.shape[0]}")

        # 3. Transposed Multiplication (A.T @ B)
        if A.T.shape[1] == B.shape[0]:
            print(f"[✓] Transposed Multiplication (A.T @ B): VALID -> Output shape {(A.T.shape[0], B.shape[1])}")
        else:
            print(f"[X] Transposed Multiplication (A.T @ B): INVALID -> {A.T.shape[1]} != {B.shape[0]}")

        # 4. Element-wise Multiplication (A * B)
        if A.shape == B.shape:
            print(f"[✓] Element-wise Product (A * B): VALID -> Output shape {A.shape}")
        else:
            print(f"[X] Element-wise Product (A * B): INVALID -> Shapes {A.shape} vs {B.shape} do not match.")
        print("=" * 50 + "\n")


# ----------------------------------------------------
# Example Demonstrations
# ----------------------------------------------------

# Case 1: Valid Matrix Multiplication
print("--- TEST CASE 1: Valid Shapes (2x3 @ 3x2) ---")
A1 = np.array([[1, 2, 3], 
               [4, 5, 6]])

B1 = np.array([[7, 8], 
               [9, 10], 
               [11, 12]])

MatrixValidator.check_all_operations(A1, B1)
result1 = MatrixValidator.validate_and_multiply(A1, B1)
print("Result (A @ B):\n", result1)


# Case 2: Invalid Matrix Multiplication (Handled safely)
print("\n--- TEST CASE 2: Invalid Shapes (2x3 @ 2x2) ---")
A2 = np.array([[1, 2, 3], 
               [4, 5, 6]])

B2 = np.array([[1, 2], 
               [3, 4]])

try:
    MatrixValidator.validate_and_multiply(A2, B2)
except ValueError as e:
    print(f"Error caught successfully:\n{e}")