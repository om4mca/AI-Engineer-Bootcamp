import matplotlib.pyplot as plt

# 1. Sample Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 2. Create the Plot
plt.plot(x, y)

# 3. Add Title and Axis Labels
plt.title('My Awesome Chart Title', fontsize=14, fontweight='bold')
plt.xlabel('X-Axis Label (e.g., Time in Days)', fontsize=12)
plt.ylabel('Y-Axis Label (e.g., Revenue in $)', fontsize=12)

# 4. Display the Plot
plt.show()