import matplotlib.pyplot as plt

# 1. Define Department Data
departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Finance', 'Customer Support']
employee_counts = [45, 25, 38, 12, 20, 28]

# 2. Create Figure Container
plt.figure(figsize=(10, 5))

# 3. Create Vertical Bar Plot
bars = plt.bar(
    departments, 
    employee_counts, 
    color='#1f77b4',      # Professional blue color
    edgecolor='#0f4c81',  # Border color for crisp edges
    width=0.55            # Width of the bars
)

# 4. Add Data Labels on Top of Each Bar
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2, # X-position (centered)
        yval + 0.8,                         # Y-position (slightly above the bar)
        f'{yval}',                          # Text value
        ha='center', va='bottom',           # Alignment
        fontsize=10, fontweight='bold'
    )

# 5. Titles & Formatting
plt.title('Employee Distribution by Department', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Department', fontsize=11, labelpad=10)
plt.ylabel('Number of Employees', fontsize=11, labelpad=10)

# Set Y-axis limit to leave room for top labels
plt.ylim(0, max(employee_counts) + 7)

# Grid & Layout Tuning
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# 6. Display Plot
plt.show()