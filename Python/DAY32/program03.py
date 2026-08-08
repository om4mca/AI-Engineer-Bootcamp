import matplotlib.pyplot as plt

# Employee Years of Experience vs Average Salary data (approximate)
experience_years = [1, 2, 3, 5, 8, 10, 12, 15, 20]
avg_salary = [55000, 61000, 68000, 82000, 99000, 115000, 126000, 142000, 160000]

# 1. Create the figure container
plt.figure(figsize=(10, 5))

# 2. Plot the Line Chart
plt.plot(
    experience_years,
    avg_salary,
    color='#2e7d32',       # Line color (dark green)
    linestyle='-',         # Solid line style
    linewidth=2.5,         # Line thickness
    marker='s',            # Square markers at data points
    markersize=7,          # Marker size
    markerfacecolor='white', # Fill color inside marker
    markeredgewidth=2,     # Marker border thickness
    label='Avg. Salary'
)

# 3. Formatting Titles & Labels
plt.title('Average Employee Salary Progression by Experience', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Years of Experience', fontsize=11, labelpad=10)
plt.ylabel('Annual Salary ($)', fontsize=11, labelpad=10)

# Format Y-axis to show currency with commas (e.g., $100,000)
plt.gca().yaxis.set_major_formatter('${x:,.0f}')

# 4. Apply Grid, Legend, and Layout tuning
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', frameon=True)
plt.tight_layout()

# 5. Save/Display the Plot
plt.savefig('employee_salary_line_chart.png', dpi=300)
plt.show()