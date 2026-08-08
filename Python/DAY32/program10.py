import matplotlib.pyplot as plt
import numpy as np

# Set seed for reproducible synthetic data
np.random.seed(42)

# 1. Generate Synthetic Age and Salary Data
ages = np.random.randint(22, 62, size=80)
salaries = 28000 + (ages * 1850) + np.random.normal(0, 12000, size=80)

# 2. Initialize Figure
plt.figure(figsize=(9, 5))

# 3. Create Scatter Plot
plt.scatter(
    ages, 
    salaries, 
    color='#1f77b4',        # Blue fill color
    edgecolor='#0f4c81',    # Darker blue border
    s=60,                   # Point size
    alpha=0.8,              # Transparency
    label='Employees'
)

# 4. Add Linear Trendline
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

# 5. Styling & Formatting
plt.title('Employee Age vs. Annual Salary Correlation', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Age (Years)', fontsize=11, labelpad=10)
plt.ylabel('Annual Salary ($)', fontsize=11, labelpad=10)

# Format Y-axis to show dollar amounts ($100,000)
plt.gca().yaxis.set_major_formatter('${x:,.0f}')

# Grid & Spines Formatting
plt.grid(True, linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Legend & Display
plt.legend(loc='upper left', frameon=True)
plt.tight_layout()

plt.show()