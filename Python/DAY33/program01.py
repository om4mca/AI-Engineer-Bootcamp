import matplotlib.pyplot as plt

# 1. Dataset
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
product_a = [12000, 15000, 18000, 22000, 21000, 25000]
product_b = [8000,  9500,  11000, 14000, 16500, 19000]
product_c = [5000,  7000,  6500,  9000,  12000, 15500]

# 2. Initialize Figure Canvas
plt.figure(figsize=(10, 5))

# 3. Plot Multiple Lines
plt.plot(months, product_a, label='Product A', color='#1f77b4', linewidth=2.5, marker='o', linestyle='-')
plt.plot(months, product_b, label='Product B', color='#2ecc71', linewidth=2.5, marker='s', linestyle='--')
plt.plot(months, product_c, label='Product C', color='#e74c3c', linewidth=2.5, marker='^', linestyle=':')

# 4. Styling & Formatting
plt.title('Monthly Revenue Comparison by Product Line', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Month', fontsize=11, labelpad=10)
plt.ylabel('Revenue ($)', fontsize=11, labelpad=10)

# Format Y-axis ticks as currency ($10,000)
plt.gca().yaxis.set_major_formatter('${x:,.0f}')

# Grid & Spines Cleanup
plt.grid(True, linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 5. Add Legend & Display
plt.legend(loc='upper left', frameon=True)
plt.tight_layout()

plt.show()