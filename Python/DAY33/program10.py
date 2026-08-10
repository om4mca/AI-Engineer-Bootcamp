import matplotlib.pyplot as plt

months_num = [1, 2, 3, 4, 5, 6]
revenue = [12000, 15000, 18000, 22000, 21000, 25000]

plt.figure(figsize=(8, 4))
plt.plot(months_num, revenue, marker='o')

# Set custom positions and string labels for X-axis
plt.xticks(
    ticks=[1, 2, 3, 4, 5, 6], 
    labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    rotation=30,          # Rotate text degrees
    fontsize=10
)

# Customize Y-axis tick locations
plt.yticks(ticks=[10000, 15000, 20000, 25000])

plt.title('Custom Tick Labels & Rotation', fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()