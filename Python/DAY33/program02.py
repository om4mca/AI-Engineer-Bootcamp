import matplotlib.pyplot as plt
import numpy as np

# Sample Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_a = [10, 15, 12, 18, 22, 28]
sales_b = [5, 8, 14, 12, 19, 21]
categories = ['Electronics', 'Clothing', 'Home', 'Books']
item_counts = [120, 85, 40, 65]
satisfaction_scores = [4.2, 3.8, 4.5, 4.0, 3.5, 4.8, 2.9, 4.1]

# 1. Initialize overall figure size
plt.figure(figsize=(12, 8))

# =============================================================
# Subplot 1: Top-Left (Row 1, Col 1, Position 1) - Line Plot
# =============================================================
plt.subplot(2, 2, 1)
plt.plot(months, sales_a, marker='o', color='#1f77b4', label='Product A')
plt.plot(months, sales_b, marker='s', color='#ff7f0e', label='Product B')
plt.title('1. Monthly Sales Trend', fontweight='bold')
plt.ylabel('Sales ($k)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

# =============================================================
# Subplot 2: Top-Right (Row 1, Col 2, Position 2) - Bar Chart
# =============================================================
plt.subplot(2, 2, 2)
plt.bar(categories, item_counts, color='#2ecc71', edgecolor='#1e8449')
plt.title('2. Inventory by Category', fontweight='bold')
plt.ylabel('Units in Stock')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# =============================================================
# Subplot 3: Bottom-Left (Row 2, Col 1, Position 3) - Histogram
# =============================================================
plt.subplot(2, 2, 3)
plt.hist(satisfaction_scores, bins=5, color='#9b59b6', edgecolor='#4a235a', alpha=0.8)
plt.title('3. Customer Rating Distribution', fontweight='bold')
plt.xlabel('Rating (Out of 5)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# =============================================================
# Subplot 4: Bottom-Right (Row 2, Col 2, Position 4) - Scatter Plot
# =============================================================
plt.subplot(2, 2, 4)
x_val = [1, 2, 3, 4, 5, 6]
y_val = [12, 18, 25, 30, 42, 50]
plt.scatter(x_val, y_val, color='#e74c3c', s=60)
plt.title('4. Ad Spend vs Revenue', fontweight='bold')
plt.xlabel('Ad Spend ($k)')
plt.ylabel('Revenue ($k)')
plt.grid(True, linestyle='--', alpha=0.5)

# =============================================================
# Layout & Display
# =============================================================
plt.suptitle('Multi-Chart Analytics Dashboard', fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout() # Ensures subplot labels and titles don't overlap!
plt.show()