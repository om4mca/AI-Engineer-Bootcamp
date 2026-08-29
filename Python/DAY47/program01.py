def solve_linear_equation(a: float, b: float, c: float):
    """
    Solves ax + b = c for x.
    """
    if a == 0:
        if b == c:
            return "Infinitely many solutions (0 = 0)"
        else:
            return "No solution (Inconsistent equation)"
    
    # Calculate x directly
    x = (c - b) / a
    return x

# --- EXAMPLE 1: Standard Equation (3x - 7 = 11) ---
a, b, c = 3, -7, 11
x_sol = solve_linear_equation(a, b, c)

print("=== LINEAR EQUATION SOLVER ===")
print(f"Equation: {a}x + ({b}) = {c}")
print(f"Solution: x = {x_sol}")

# Verification
if isinstance(x_sol, (int, float)):
    is_correct = (a * x_sol + b) == c
    print(f"Verification Check: {a}({x_sol}) + ({b}) == {c} -> {is_correct} ✅")