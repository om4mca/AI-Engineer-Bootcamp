import matplotlib.pyplot as plt

# 1. Dataset
categories = ['Engineering & Tech', 'Sales & Marketing', 'Customer Support', 'Human Resources', 'Finance & Operations']
values = [120, 85, 60, 25, 40]

# 2. Setup Figure Canvas
plt.figure(figsize=(9, 5))

# 3. Render Horizontal Bar Chart using plt.barh()
bars = plt.barh(
    categories, 
    values, 
    color='#16a085',      # Teal bar color
    edgecolor='#0e6251',  # Border line color
    height=0.55,          # Controls bar thickness (height in horizontal orientation)
    alpha=0.9
)

# -------------------------------------------------------------
# 4. Add Value Labels Next to Each Bar
# -------------------------------------------------------------
for bar in bars:
    xval = bar.get_width() # For barh, width represents the value!
    plt.text(
        xval + 2,                            # X position (slightly to the right of the bar tip)
        bar.get_y() + bar.get_height() / 2,  # Y position (vertically centered)
        f'{xval}',                           # Text label
        ha='left', 
        va='center', 
        fontweight='bold', 
        fontsize=10
    )

# -------------------------------------------------------------
# 5. Styling & Layout Cleanup
# -------------------------------------------------------------
plt.title('Department Headcount Breakdown', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Number of Employees', fontsize=11, labelpad=10)
plt.ylabel('Department', fontsize=11, labelpad=10)

# Set X-axis limit to give space for labels
plt.xlim(0, max(values) + 20)

# Invert Y-axis so the top category appears first (optional)
plt.gca().invert_yaxis()

# Grid & Spines cleanup
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()