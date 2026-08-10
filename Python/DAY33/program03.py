import matplotlib.pyplot as plt

# Sample Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [12, 19, 15, 22, 28, 35]
costs = [8, 11, 10, 14, 18, 20]

categories = ['Laptops', 'Phones', 'Tablets', 'Accessories']
units_sold = [340, 520, 210, 890]

satisfaction = [4.5, 3.2, 4.8, 3.9, 4.1, 2.5, 4.7, 3.8, 4.2]
ad_spend = [1, 2, 3, 4, 5, 6]
revenue = [10, 18, 28, 35, 48, 55]

# 1. Initialize Figure and 2x2 Axes Grid all at once
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# =============================================================
# Plot 1: Top-Left (Row 0, Col 0) - Line Plot
# =============================================================
axes[0, 0].plot(months, sales, label='Sales', color='#1f77b4', marker='o')
axes[0, 0].plot(months, costs, label='Costs', color='#e74c3c', marker='s', linestyle='--')
axes[0, 0].set_title('1. Monthly Financials', fontweight='bold')
axes[0, 0].set_ylabel('Amount ($k)')
axes[0, 0].grid(True, linestyle='--', alpha=0.5)
axes[0, 0].legend()

# =============================================================
# Plot 2: Top-Right (Row 0, Col 1) - Horizontal Bar Chart
# =============================================================
axes[0, 1].barh(categories, units_sold, color='#2ecc71', edgecolor='#1e8449')
axes[0, 1].set_title('2. Category Volume (barh)', fontweight='bold')
axes[0, 1].set_xlabel('Units Sold')
axes[0, 1].grid(axis='x', linestyle='--', alpha=0.5)

# =============================================================
# Plot 3: Bottom-Left (Row 1, Col 0) - Histogram
# =============================================================
axes[1, 0].hist(satisfaction, bins=5, color='#8e44ad', edgecolor='#4a235a', alpha=0.85)
axes[1, 0].set_title('3. Customer Rating Distribution', fontweight='bold')
axes[1, 0].set_xlabel('Score (1 to 5)')
axes[1, 0].set_ylabel('Count')
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.5)

# =============================================================
# Plot 4: Bottom-Right (Row 1, Col 1) - Scatter Plot
# =============================================================
axes[1, 1].scatter(ad_spend, revenue, color='#e67e22', s=70, edgecolor='#d35400')
axes[1, 1].set_title('4. Ad Spend vs. Revenue', fontweight='bold')
axes[1, 1].set_xlabel('Ad Budget ($k)')
axes[1, 1].set_ylabel('Revenue ($k)')
axes[1, 1].grid(True, linestyle='--', alpha=0.5)

# =============================================================
# Dashboard Overall Styling & Display
# =============================================================
fig.suptitle('Company Performance Dashboard (plt.subplots)', fontsize=16, fontweight='bold')

# Adjust layout so subplots don't overlap
plt.tight_layout()

# Display
plt.show()