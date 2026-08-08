import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 42]
y2 = [5, 15, 18, 22, 35]

# Plot lines and assign labels
plt.plot(x, y1, color='blue', label='Product A')
plt.plot(x, y2, color='orange', label='Product B')

# Add Labels and Display Legend
plt.title('Product Sales Comparison')
plt.xlabel('Month')
plt.ylabel('Units Sold')

plt.legend() # Displays the legend box
plt.show()