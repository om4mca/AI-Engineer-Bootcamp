import numpy as np
from scipy import integrate

# --- A. Integrating a Vector (Discrete Data Points) ---
# Example: Integrating velocity vector over time to find displacement
time = np.array([0, 1, 2, 3, 4, 5])       # x-axis vector
velocity = np.array([0, 2, 4, 6, 8, 10])  # y-axis vector

# Returns a single scalar result (Area under curve using Simpson's / Trapezoidal rule)
displacement_scalar = integrate.simpson(y=velocity, x=time)
print(f"Total Displacement (Scalar): {displacement_scalar}")  # Output: 25.0


# --- B. Definite Scalar Function Integration ---
# Integrating f(x) = x^2 from x = 0 to x = 3
def scalar_func(x):
    return x**2

result, error = integrate.quad(scalar_func, 0, 3)
print(f"Definite Integral Result: {result}")  # Output: 9.0


# --- C. Vector Integration (Element-wise Integration of a Vector Function) ---
# Integrating a vector-valued function F(t) = [t, t^2, cos(t)] from 0 to 1
def vector_func(t):
    return np.array([t, t**2, np.cos(t)])

# Perform 1D quad integration element-wise across the array
integrated_vector, _ = integrate.quad_vec(vector_func, 0, 1)
print(f"Integrated Vector: {integrated_vector}")  # Output: [0.5, 0.333..., 0.841...]