import numpy as np

# 1. Define Input Vectors
experience = np.array([2, 3, 5, 7], dtype=np.float64)
salary = np.array([30, 35, 48, 60], dtype=np.float64)

# 2. Build Design Matrix X (Column of 1s + Feature Column)
X = np.column_stack([
    np.ones(len(experience)),
    experience
])

# 3. Solve for Weights using Ordinary Least Squares
weights, residuals, rank, s = np.linalg.lstsq(X, salary, rcond=None)

w0_intercept = weights[0]
w1_coefficient = weights[1]

print("=== EMPLOYEE SALARY REGRESSION RESULT ===")
print(f"Design Matrix (X):\n{X}\n")
print(f"Target Vector (y):\n{salary}\n")
print(f"Intercept (w0)   : {w0_intercept:.4f} ($k base salary)")
print(f"Coefficient (w1) : {w1_coefficient:.4f} ($k per year of experience)")
print(f"Fitted Equation  : Salary = {w0_intercept:.2f} + {w1_coefficient:.2f} * Experience")