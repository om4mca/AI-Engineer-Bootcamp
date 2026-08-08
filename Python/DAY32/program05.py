import matplotlib.pyplot as plt

# 1. Define Categories (Longer text labels work great here!)
projects = [
    'Alpha (R&D)', 
    'Beta (MVP)', 
    'Gamma (Testing)', 
    'Delta (Launch Prep)', 
    'Epsilon (Maintenance)'
]
completion_percentage = [15, 40, 60, 75, 98]

# 2. Set Figure Size
plt.figure(figsize=(10, 5))

# 3. Create Horizontal Bar Chart (plt.barh)
bars = plt.barh(
    projects, 
    completion_percentage, 
    color='#1f77b4',       # Clean blue fill
    edgecolor='#0f4c81',   # Dark blue border
    height=0.6             # Bar height/thickness
)

# 4. Add Percentage Labels Next to Each Bar
for bar in bars:
    xval = bar.get_width()
    plt.text(
        xval + 1.5,                              # Position slightly right of bar tip
        bar.get_y() + bar.get_height() / 2,     # Vertically centered on the bar
        f'{xval}%',                             # Text format
        ha='left', va='center',                 # Alignment
        fontsize=10, fontweight='bold'
    )

# 5. Styling & Formatting
plt.title('Company-wide Project Completion Status', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Completion Percentage (%)', fontsize=11, labelpad=10)

# Set X-axis limits to leave room for end-labels
plt.xlim(0, 110)

# Format X-axis ticks to show percentage symbol
plt.gca().xaxis.set_major_formatter('{x:.0f}%')

# Add vertical grid lines only
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Clean look: remove top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Adjust layout & display
plt.tight_layout()
plt.show()