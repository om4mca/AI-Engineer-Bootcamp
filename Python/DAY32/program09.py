import matplotlib.pyplot as plt
import numpy as np

# Set seed for reproducible data
np.random.seed(42)

# Generate synthetic Age and Salary data with a positive correlation
ages = np.random.randint(22, 62, size=80)
salaries = 28000 + (ages * 1850) + np.random.normal(0, 12000, size=80)

# 1. Figure setup
plt.figure(figsize=(9, 5))

# 2. Plot Scatter Plot
plt.scatter(
    ages, 
    salaries, 
    color='#1f77b4',        # Point fill color
    edgecolor='#0f4c81',    # Point border color
    s=60,                   # Size of markers
    alpha=0.8,              # Transparency
    label='Employees'
)

# 3. Add a Trendline (Linear Regression fit)
z = np.polyfit(ages, salaries, 1)
p = np.poly1d(z)
plt.plot(
    ages, 
    p(ages), 
    color='#e74c3c', 
    linestyle='--', 
    linewidth=2, 
    label='Trendline (Avg Growth)'
)

# 4. Styling & Formatting
plt.title('Employee Age vs. Annual Salary Correlation', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Age (Years)', fontsize=11, labelpad=10)
plt.ylabel('Annual Salary ($)', fontsize=11, labelpad=10)

# Format Y-axis to show currency ($50,000)
plt.gca().yaxis.set_major_formatter('${x:,.0f}')

# Grid & Spines
plt.grid(True, linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.legend(loc='upper left', frameon=True)
plt.tight_layout()

# Save & Display
plt.savefig('age_vs_salary_scatter.png', dpi=300)
plt.show()