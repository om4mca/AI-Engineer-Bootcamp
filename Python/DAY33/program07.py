import matplotlib.pyplot as plt

# 1. Dataset
categories = ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance']
values = [45, 32, 28, 15, 22]

# 2. Custom Color Palette for each bar
custom_colors = ['#1f77b4', '#2ecc71', '#e67e22', '#9b59b6', '#3498db']

# 3. Create Figure Canvas
plt.figure(figsize=(9, 5))

# 4. Render Customized Bar Chart
bars = plt.bar(
    categories, 
    values, 
    color=custom_colors,      # Custom colors per bar
    edgecolor='#1a252f',      # Dark border around bars
    linewidth=1.2,            # Thickness of border line
    width=0.55,               # Width of each bar (0 to 1)
    alpha=0.9                 # Slight opacity
)

# -------------------------------------------------------------
# 5. Add Data Labels (Value Annotations) on Top of Each Bar
# -------------------------------------------------------------
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2, # X-position (center of bar)
        yval + 0.8,                        # Y-position (slightly above bar top)
        f'{yval}',                         # Label text
        ha='center',                       # Horizontal alignment
        va='bottom',                       # Vertical alignment
        fontsize=10, 
        fontweight='bold'
    )

# -------------------------------------------------------------
# 6. Styling, Axes & Spines Cleanup
# -------------------------------------------------------------
plt.title('Department Headcount Breakdown', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Department Name', fontsize=11, labelpad=10)
plt.ylabel('Number of Staff', fontsize=11, labelpad=10)

# Rotate X-tick labels horizontally or at an angle
plt.xticks(fontsize=10, rotation=0)

# Set Y-axis view boundary to give space for labels
plt.ylim(0, max(values) + 8)

# Add horizontal dashed gridlines only
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Clean up top and right border spines
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Display Chart
plt.tight_layout()
plt.show()