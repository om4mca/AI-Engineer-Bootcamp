import matplotlib.pyplot as plt

# Monthly Sales Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [12500, 14200, 13800, 16500, 18200, 17900, 21000, 22500, 20800, 24100, 27800, 31500]

# Create Figure
plt.figure(figsize=(10, 5))

# Plot Sales Line
plt.plot(
    months, 
    sales, 
    color='#1e88e5',       # Professional blue line
    linestyle='-',         # Solid line
    linewidth=2.5,         # Line thickness
    marker='o',            # Circle markers at data points
    markersize=6,          # Marker size
    markerfacecolor='white', # White inner fill
    markeredgewidth=2,     # Marker border width
    label='Monthly Sales ($)'
)

# Titles & Labels
plt.title('Company Monthly Sales Performance (2026)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Month', fontsize=11, labelpad=10)
plt.ylabel('Sales Revenue ($)', fontsize=11, labelpad=10)

# Format Y-axis with commas for currency readability
plt.gca().yaxis.set_major_formatter('${x:,.0f}')

# Grid, Legend & Layout
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', frameon=True)
plt.tight_layout()

# Save & Show Plot
plt.savefig('sales_line_chart.png', dpi=300)
plt.show()