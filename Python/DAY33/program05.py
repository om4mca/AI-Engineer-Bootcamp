import matplotlib.pyplot as plt
import numpy as np

# 1. Generate Sample Data
x = np.linspace(0, 10, 100)

# Initialize Figure Canvas
plt.figure(figsize=(12, 7))

# -------------------------------------------------------------
# 2. Main Line Styles Demonstration
# -------------------------------------------------------------

# Solid Line (default)
plt.plot(x, np.sin(x), linestyle='-', color='#1f77b4', linewidth=2, label="Solid  ('-')")

# Dashed Line
plt.plot(x, np.sin(x - 0.5), linestyle='--', color='#2ecc71', linewidth=2, label="Dashed ('--')")

# Dotted Line
plt.plot(x, np.sin(x - 1.0), linestyle=':', color='#e74c3c', linewidth=2.5, label="Dotted (':')")

# Dash-Dot Line
plt.plot(x, np.sin(x - 1.5), linestyle='-.', color='#9b59b6', linewidth=2, label="Dash-Dot ('-.')")

# Custom Loose Dashed Line (using tuples: (offset, (on_off_seq)))
plt.plot(x, np.sin(x - 2.0), linestyle=(0, (5, 5)), color='#e67e22', linewidth=2, label="Custom Dash (5, 5)")

# Custom Dense Dotted Line
plt.plot(x, np.sin(x - 2.5), linestyle=(0, (1, 1)), color='#34495e', linewidth=2, label="Custom Dense Dot (1, 1)")

# -------------------------------------------------------------
# 3. Formatting & Aesthetics
# -------------------------------------------------------------
plt.title('Matplotlib Line Styles & Formatting Guide', fontsize=15, fontweight='bold', pad=15)
plt.xlabel('X Axis', fontsize=11)
plt.ylabel('Y Axis', fontsize=11)

# Add custom grid
plt.grid(True, linestyle='--', alpha=0.5)

# Place legend outside or neatly in top-right
plt.legend(loc='upper right', frameon=True, fontsize=10)

# Display plot
plt.tight_layout()
plt.show()