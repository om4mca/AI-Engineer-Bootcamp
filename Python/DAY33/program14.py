import matplotlib.pyplot as plt
import numpy as np

# 1. Generate Synthetic Dataset
np.random.seed(42)
n_points = 50

# X: Advertising Budget ($k)
ad_budget = np.random.uniform(10, 100, n_points)

# Y: Revenue Generated ($k) - positively correlated with budget
revenue = ad_budget * 2.5 + np.random.normal(0, 20, n_points)

# Continuous Variable 3: Conversion Rate (%) -> Map to Marker Color
conversion_rate = np.random.uniform(1.5, 6.0, n_points)

# Continuous Variable 4: Number of Campaigns -> Map to Marker Size
campaigns = np.random.randint(5, 30, n_points)
marker_sizes = campaigns * 12  # Scale size up for visualization

# 2. Setup Figure Canvas
plt.figure(figsize=(10, 6))

# 3. Create Customized Scatter Plot
scatter = plt.scatter(
    x=ad_budget,
    y=revenue,
    s=marker_sizes,            # Marker Size mapped to 'campaigns'
    c=conversion_rate,         # Marker Color mapped to 'conversion_rate'
    cmap='viridis',            # Color map (e.g., 'viridis', 'plasma', 'coolwarm')
    alpha=0.75,                # Transparency to show overlapping points
    edgecolors='#2c3e50',      # Dark border around each marker point
    linewidths=1.2              # Border thickness
)

# 4. Add Colorbar Legend for Color Mapping
cbar = plt.colorbar(scatter)
cbar.set_label('Conversion Rate (%)', fontsize=11, labelpad=10)

# -------------------------------------------------------------
# 5. Add Custom Annotations & Trendline
# -------------------------------------------------------------
# Add linear fit trendline
z = np.polyfit(ad_budget, revenue, 1)
p = np.poly1d(z)
plt.plot(
    np.sort(ad_budget), 
    p(np.sort(ad_budget)), 
    color='#e74c3c', 
    linestyle='--', 
    linewidth=2, 
    label='Trendline'
)

# Annotate Top Performing Campaign
max_idx = np.argmax(revenue)
plt.annotate(
    f'Peak Revenue\n(${revenue[max_idx]:,.0f}k)',
    xy=(ad_budget[max_idx], revenue[max_idx]),
    xytext=(ad_budget[max_idx] - 15, revenue[max_idx] + 15),
    arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.2),
    bbox=dict(boxstyle='round,pad=0.3', facecolor='#fcf3cf', edgecolor='#f39c12', lw=1),
    fontweight='bold',
    fontsize=9
)

# -------------------------------------------------------------
# 6. Styling, Axis & Spines Cleanup
# -------------------------------------------------------------
plt.title('Ad Budget vs. Revenue Impact Analysis', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Ad Budget ($k)', fontsize=11, labelpad=10)
plt.ylabel('Revenue ($k)', fontsize=11, labelpad=10)

# Currency tick formatting
plt.gca().xaxis.set_major_formatter('${x:,.0f}k')
plt.gca().yaxis.set_major_formatter('${x:,.0f}k')

# Grid & Spines
plt.grid(True, linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.legend(loc='upper left', frameon=True)
plt.tight_layout()
plt.show()