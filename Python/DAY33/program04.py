import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Generate Synthetic Business Dataset
np.random.seed(42)
n_months = 12

df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Revenue': [12000, 15000, 14000, 18000, 22000, 21000, 25000, 27000, 26000, 30000, 34000, 38000],
    'Expenses': [8000, 9500, 9000, 11000, 13000, 12500, 14000, 15000, 14500, 16000, 18000, 19500],
    'AdBudget': [1000, 1200, 1100, 1500, 2000, 1800, 2200, 2500, 2300, 2800, 3200, 3800]
})

# Department performance dataset
dept_df = pd.DataFrame({
    'Department': ['Engineering', 'Sales', 'Marketing', 'HR', 'Support'],
    'Headcount': [45, 30, 20, 10, 15],
    'Satisfaction': [4.2, 3.8, 4.0, 3.5, 4.1]
})

# Customer rating sample data
customer_ratings = np.random.normal(loc=4.1, scale=0.6, size=200).clip(1.0, 5.0)

# Salary distributions by department
salary_data = [
    np.random.normal(95000, 10000, 30), # Engineering
    np.random.normal(75000, 12000, 30), # Sales
    np.random.normal(68000, 8000, 30),  # Marketing
    np.random.normal(60000, 6000, 30),  # HR
    np.random.normal(55000, 5000, 30)   # Support
]

# 2. Setup Subplots Grid (3 Rows x 2 Columns)
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(14, 15))
fig.suptitle('Executive Business Analytics Dashboard', fontsize=18, fontweight='bold', y=0.98)

# -------------------------------------------------------------
# Chart 1: Line Plot (Revenue vs Expenses) - [0, 0]
# -------------------------------------------------------------
axes[0, 0].plot(df['Month'], df['Revenue'], label='Revenue', color='#1f77b4', marker='o', linewidth=2)
axes[0, 0].plot(df['Month'], df['Expenses'], label='Expenses', color='#e74c3c', marker='s', linestyle='--', linewidth=2)
axes[0, 0].set_title('1. Monthly Financial Trend', fontweight='bold')
axes[0, 0].set_ylabel('Amount ($)')
axes[0, 0].yaxis.set_major_formatter('${x:,.0f}')
axes[0, 0].grid(True, linestyle='--', alpha=0.5)
axes[0, 0].legend()

# -------------------------------------------------------------
# Chart 2: Vertical Bar Chart (Headcount by Dept) - [0, 1]
# -------------------------------------------------------------
bars2 = axes[0, 1].bar(dept_df['Department'], dept_df['Headcount'], color='#2ecc71', edgecolor='#1e8449', width=0.5)
axes[0, 1].set_title('2. Headcount by Department', fontweight='bold')
axes[0, 1].set_ylabel('Employees')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.5)
for bar in bars2:
    yval = bar.get_height()
    axes[0, 1].text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{int(yval)}', ha='center', va='bottom', fontweight='bold')

# -------------------------------------------------------------
# Chart 3: Scatter Plot (Ad Budget vs Revenue) - [1, 0]
# -------------------------------------------------------------
axes[1, 0].scatter(df['AdBudget'], df['Revenue'], color='#e67e22', edgecolor='#d35400', s=70)
# Trendline
z = np.polyfit(df['AdBudget'], df['Revenue'], 1)
p = np.poly1d(z)
axes[1, 0].plot(df['AdBudget'], p(df['AdBudget']), color='#2c3e50', linestyle='--', label='Trend')
axes[1, 0].set_title('3. Ad Budget vs. Revenue', fontweight='bold')
axes[1, 0].set_xlabel('Ad Spend ($)')
axes[1, 0].set_ylabel('Revenue ($)')
axes[1, 0].yaxis.set_major_formatter('${x:,.0f}')
axes[1, 0].xaxis.set_major_formatter('${x:,.0f}')
axes[1, 0].grid(True, linestyle='--', alpha=0.5)
axes[1, 0].legend()

# -------------------------------------------------------------
# Chart 4: Histogram (Customer Rating Distribution) - [1, 1]
# -------------------------------------------------------------
counts, bins, _ = axes[1, 1].hist(customer_ratings, bins=10, color='#9b59b6', edgecolor='#4a235a', alpha=0.85)
axes[1, 1].set_title('4. Customer Rating Distribution', fontweight='bold')
axes[1, 1].set_xlabel('Rating Score (1 to 5)')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].grid(axis='y', linestyle='--', alpha=0.5)

# -------------------------------------------------------------
# Chart 5: Horizontal Bar Chart (Satisfaction Score) - [2, 0]
# -------------------------------------------------------------
bars5 = axes[2, 0].barh(dept_df['Department'], dept_df['Satisfaction'], color='#3498db', edgecolor='#1d6fa5', height=0.5)
axes[2, 0].set_title('5. Department Satisfaction Score', fontweight='bold')
axes[2, 0].set_xlabel('Score (Out of 5)')
axes[2, 0].set_xlim(0, 5)
axes[2, 0].grid(axis='x', linestyle='--', alpha=0.5)
for bar in bars5:
    xval = bar.get_width()
    axes[2, 0].text(xval + 0.1, bar.get_y() + bar.get_height()/2, f'{xval:.1f}', ha='left', va='center', fontweight='bold')

# -------------------------------------------------------------
# Chart 6: Box Plot (Salary Spread by Department) - [2, 1]
# -------------------------------------------------------------
box = axes[2, 1].boxplot(
    salary_data, 
    tick_labels=dept_df['Department'], 
    patch_artist=True, 
    medianprops=dict(color='black', linewidth=1.5)
)
colors = ['#1f77b4', '#2ecc71', '#e67e22', '#9b59b6', '#3498db']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

axes[2, 1].set_title('6. Salary Range by Department', fontweight='bold')
axes[2, 1].set_ylabel('Salary ($)')
axes[2, 1].yaxis.set_major_formatter('${x:,.0f}')
axes[2, 1].grid(axis='y', linestyle='--', alpha=0.5)

# -------------------------------------------------------------
# 3. Final Spacing Adjustment & Display
# -------------------------------------------------------------
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()