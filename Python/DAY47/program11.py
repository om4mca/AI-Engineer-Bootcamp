import numpy as np

# Singular Matrix (Row 2 is 2x Row 1 -> det = 0)
A = np.array([
    [1, 2],
    [2, 4]
], dtype=np.float64)

b = np.array([5, 10], dtype=np.float64)

try:
    # Attempt standard exact solve
    x = np.linalg.solve(A, b)
    print("Exact Solution x:", x)

except np.linalg.LinAlgError as e:
    print(f"⚠️ LinAlgError Encountered: {e}")
    print("Matrix is singular or ill-conditioned. Proceeding to fallback solver...")