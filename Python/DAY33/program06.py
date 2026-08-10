import matplotlib.pyplot as plt
import numpy as np

# 1. Generate Sample Data
x = np.arange(1, 11)

# Initialize Figure Canvas
plt.figure(figsize=(12, 7))

# -------------------------------------------------------------
# 2. Common Markers Demonstration
# -------------------------------------------------------------

# Circle ('o')
plt.plot(x, x + 10, marker='o', label="Circle ('o')", color='#1f77b4', linewidth=1.5)

# Square ('s')
plt.plot(x, x + 8, marker='s', label="Square ('s')", color='#2ecc71', linewidth=1.5)

# Triangle Up ('^')
plt.plot(x, x + 6, marker='^', label="Triangle Up ('^')", color='#e74c3c', linewidth=1.5)

# Diamond ('D')
plt.plot(x, x + 4, marker='D', label="Diamond ('D')", color='#9b59b6', linewidth=1.5)

# Star ('*')
plt.plot(x, x + 2, marker='*', label="Star ('*')", color='#e67e22', linewidth=1.5)

# Cross ('x')
plt.plot(x, x, marker='x', label="Cross ('x')", color='#16a085', linewidth=1.5)

# -------------------------------------------------------------
# 3. Customizing Marker Styling (Size, Fill, Edge)
# -------------------------------------------------------------
# Custom styled line at the bottom
plt.plot(
    x, x - 2, 
    marker='o', 
    markersize=10,             # Size of marker
    markerfacecolor='yellow',  # Inner fill color
    markeredgecolor='black',   # Outer border color
    markeredgewidth=2,         # Border thickness
    color='gray', 
    linestyle='--', 
    linewidth=2,
    label="Custom ('o' with border)"
)

# -------------------------------------------------------------
# 4. Styling & Layout
# -------------------------------------------------------------
plt.title('Matplotlib Marker Types & Styling Guide', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('X Values', fontsize=11)
plt.ylabel('Y Values', fontsize=11)

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', frameon=True, fontsize=10)

plt.tight_layout()
plt.show()