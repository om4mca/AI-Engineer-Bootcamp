import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 25, 40, 30, 85, 90, 110, 105, 130, 150]

plt.figure(figsize=(8, 4))
plt.plot(x, y, marker='o', color='#1f77b4')

# Set X and Y limits
plt.xlim(1, 10)     # Force X-axis to start at 1 and end at 10
plt.ylim(0, 180)    # Force Y-axis to start at 0 and end at 180 (adds breathing room for annotations)

plt.title('Axis Limits Example (plt)', fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()