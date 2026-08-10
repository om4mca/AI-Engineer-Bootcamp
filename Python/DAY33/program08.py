import matplotlib.pyplot as plt

categories = ['Engineering Department', 'Marketing Department', 'Sales & Operations', 'Human Resources']
values = [45, 28, 35, 12]

plt.bar(categories, values)

# Rotate X-axis labels by 45 degrees
plt.xticks(rotation=45, ha='right')

plt.tight_layout()  # Prevents rotated labels from getting cut off at the bottom
plt.show()