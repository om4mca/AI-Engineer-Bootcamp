def solve_2x2_system(a1, b1, c1, a2, b2, c2):
    # Determinant of coefficient matrix
    det = a1 * b2 - a2 * b1
    
    if det == 0:
        # Check consistency for no solution vs infinite solutions
        if (a1 * c2 - a2 * c1 == 0) and (b1 * c2 - b2 * c1 == 0):
            return "Infinitely many solutions"
        else:
            return "No solution"
            
    # Cramer's Rule: Dx / Det, Dy / Det
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    return x, y

# System: 2x + 3y = 8 and 4x - 1y = 2
sol_x, sol_y = solve_2x2_system(2, 3, 8, 4, -1, 2)
print(f"Manual Verified Solution in Python: x = {sol_x:.1f}, y = {sol_y:.1f}")
# Output: x = 1.0, y = 2.0