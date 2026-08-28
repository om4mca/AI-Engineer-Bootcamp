import numpy as np

# Define two candidate matrices
A = np.array([
    [1, 3, 2],
    [2, 4, 1],
    [0, 1, 5]
])

B = np.array([
    [1, 3, 2],
    [2, 6, 4],  # Row 2 = 2 * Row 1
    [0, 1, 5]
])

def compare_matrices(M1: np.ndarray, M2: np.ndarray, name1="Matrix A", name2="Matrix B"):
    r1, r2 = np.linalg.matrix_rank(M1), np.linalg.matrix_rank(M2)
    max_r1, max_r2 = min(M1.shape), min(M2.shape)
    
    print(f"=== RANK COMPARISON ===")
    print(f"{name1} (Shape {M1.shape}): Rank = {r1}/{max_r1} -> {'FULL RANK ✅' if r1 == max_r1 else 'RANK DEFICIENT ❌'}")
    print(f"{name2} (Shape {M2.shape}): Rank = {r2}/{max_r2} -> {'FULL RANK ✅' if r2 == max_r2 else 'RANK DEFICIENT ❌'}")
    
    if r1 > r2:
        print(f"\nConclusion: {name1} contains more independent information than {name2}.")
    elif r2 > r1:
        print(f"\nConclusion: {name2} contains more independent information than {name1}.")
    else:
        print(f"\nConclusion: Both matrices have the exact same rank ({r1}).")

compare_matrices(A, B)