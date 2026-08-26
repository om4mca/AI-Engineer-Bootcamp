import numpy as np

def analyze_employee_matrices(matrices_dict):
    for name, matrix in matrices_dict.items():
        A = np.array(matrix, dtype=float)
        
        print("=" * 45)
        print(f"  {name.upper()}")
        print("=" * 45)
        
        # 1. Matrix & Shape
        print(f"Matrix:\n{A}")
        print(f"Shape: {A.shape}")
        
        # Invertibility requires a square matrix
        if A.shape[0] != A.shape[1]:
            print("Determinant: N/A (Non-square matrix)")
            print("Status: Non-Square (Not Invertible)\n")
            continue

        # 2. Determinant
        det = np.linalg.det(A)
        # Round determinant to prevent minor floating-point errors (e.g., 0.0000000000000001)
        det_rounded = round(det, 6)
        print(f"Determinant: {det_rounded}")

        # 3. Singular / Non-Singular Status & 4. Inverse + Verification
        if det_rounded != 0:
            print("Status: Non-Singular (Invertible)")
            
            # Inverse
            inv = np.linalg.inv(A)
            print(f"Inverse:\n{np.round(inv, 4)}")
            
            # Verification (A @ A_inv)
            verification = A @ inv
            print(f"Verification (A @ Inverse):\n{np.round(verification, 4)}")
            print("Identity Matrix ✅\n")
        else:
            print("Status: Singular (Non-Invertible)")
            print("Inverse: Impossible (Determinant is 0)")
            print("Verification: Cannot verify ✅\n")


# Define sample employee feature matrices
employee_matrices = {
    # Matrix 1: [Years Experience, Projects Completed]
    "Employee Matrix 1 (Invertible)": [
        [2, 1],
        [1, 3]
    ],
    
    # Matrix 2: Singular matrix (Row 2 / Col 2 is exactly double Row 1 / Col 1)
    "Employee Matrix 2 (Singular - Dependent Features)": [
        [1, 2],
        [2, 4]
    ],
    
    # Matrix 3: [Certifications, Peer Score (0-100), Years at Company]
    "Employee Matrix 3 (3x3 Invertible)": [
        [3, 85, 4],
        [1, 70, 2],
        [5, 95, 8]
    ]
}

# Run analyzer
analyze_employee_matrices(employee_matrices)