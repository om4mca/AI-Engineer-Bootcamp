import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------------------
# 1. Create Synthetic E-Commerce Dataset
# -------------------------------------------------------------
np.random.seed(42)
n_rows = 300

dates = pd.date_range(start='2026-01-01', periods=n_rows, freq='D')
categories = np.random.choice(['Electronics', 'Clothing', 'Home & Kitchen', 'Books'], size=n_rows)
sales = np.random.normal(loc=150, scale=40, size=n_rows).round(2)
profit = sales * np.random.uniform(0.15, 0.40, size=n_rows)

df = pd.DataFrame({
    'Date': dates,
    'Category': categories,
    'Sales': sales,
    'Profit': profit
})

# Add Month Column for Aggregation
df['Month'] = df['Date'].dt.strftime('%Y-%m')

# -------------------------------------------------------------
# 2. Perform Pandas Data Aggregations
# -------------------------------------------------------------
# Group By Category: Total Sales & Profit
cat_summary = df.groupby('Category')[['Sales', 'Profit']].sum().reset_index()

# Group By Month: Monthly Financials
monthly_summary = df.groupby('Month')[['Sales', 'Profit']].sum()

# -------------------------------------------------------------
# 3. Create Matplotlib Subplots Canvas
# -------------------------------------------------------------
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
fig.suptitle('E-Commerce Performance Dashboard (Pandas + Matplotlib)', fontsize=16, fontweight='bold', y=0.98)

# -------------------------------------------------------------
# Chart 1: Monthly Financial Trend (Line Plot from Pandas)
# -------------------------------------------------------------
monthly_summary.plot(
    kind='line',
    ax=axes[0, 0],
    marker='o',
    linewidth=2,
    color=['#1f77b4', '#2ecc71']
)
axes[0, 0].set_title('1. Monthly Sales & Profit Trend', fontweight='bold')
axes[0, 0].set_ylabel('Amount ($)')
axes[0, 0].yaxis.set_major_formatter('${x:,.0f}')
axes[0, 0].grid(True, linestyle='--', alpha=0.5)

# -------------------------------------------------------------
# Chart 2: Category Revenue Breakdown (Bar Chart from Pandas)
# -------------------------------------------------------------
cat_summary.plot(
    kind='bar',
    x='Category',
    y='Sales',
    ax=axes[0, 1],
    color='#e67e22',
    legend=False,
    rot=0
)
axes[0, 1].set_title('2. Total Revenue by Category', fontweight='bold')
axes[0, 1].set_ylabel('Total Revenue ($)')
axes[0, 1].yaxis.set_major_formatter('${x:,.0f}')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.5)

# -------------------------------------------------------------
# Chart 3: Order Value Distribution (Histogram from Pandas)
# -------------------------------------------------------------
df['Sales'].plot(
    kind='hist',
    bins=15,
    ax=axes[1, 0],
    color='#8e44ad',
    edgecolor='#4a235a',
    alpha=0.85
)
axes[1, 0].set_title('3. Order Value Distribution', fontweight='bold')
axes[1, 0].set_xlabel('Order Amount ($)')
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.5)

# -------------------------------------------------------------
# Chart 4: Sales vs Profit Spread (Boxplot from Pandas)
# -------------------------------------------------------------
df.boxplot(
    column='Sales',
    by='Category',
    ax=axes[1, 1],
    grid=False,
    patch_artist=True
)
axes[1, 1].set_title('4. Sales Value Spread by Category', fontweight='bold')
axes[1, 1].set_xlabel('Category')
axes[1, 1].set_ylabel('Sales ($)')
plt.suptitle('')  # Clear default pandas boxplot title artifact

# -------------------------------------------------------------
# 4. Final Layout Adjustments
# -------------------------------------------------------------
plt.tight_layout()
plt.show()