import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Create plot
plt.figure(figsize=(8, 4.5))
plt.plot(x, y, color='blue', marker='o')

plt.title('Sample Plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.grid(True)

# -------------------------------------------------------------
# Save Chart as PNG File
# IMPORTANT: Call savefig() BEFORE calling show()
# -------------------------------------------------------------
plt.savefig('my_chart.png', dpi=300, bbox_inches='tight')

# Display plot
plt.show()