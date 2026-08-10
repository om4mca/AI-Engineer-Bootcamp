import matplotlib.pyplot as plt
import numpy as np

# 1. Generate Synthetic Data (e.g., Customer Ages)
np.random.seed(42)
ages = np.random.normal(loc=38, scale=12, size=300).astype(int).clip(18, 75)

# 2. Setup Figure Canvas with 2 Subplots to compare Bin styles
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# -------------------------------------------------------------
# Plot 1: Equal-width Bins (bins=10)
# -------------------------------------------------------------
counts1, bins1, patches1 = ax1.hist(
    ages, 
    bins=10, 
    color='#8e44ad', 
    edgecolor='#4a235a', 
    alpha=0.85
)

# Label count on top of each bin bar
for count, bin_left, bin_right in zip(counts1, bins1[:-1], bins1[1:]):
    if count > 0:
        ax1.text((bin_left + bin_right) / 2, count + 0.8, f'{int(count)}', ha='center', va='bottom', fontweight='bold', fontsize=9)

ax1.set_title('1. Equal-Width Bins (bins=10)', fontweight='bold')
ax1.set_xlabel('Age (Years)')
ax1.set_ylabel('Frequency / Count')
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# -------------------------------------------------------------
# Plot 2: Custom Bin Boundaries (bins=[18, 25, 35, 50, 65, 80])
# -------------------------------------------------------------
custom_bins = [18, 25, 35, 50, 65, 80]
counts2, bins2, patches2 = ax2.hist(
    ages, 
    bins=custom_bins, 
    color='#2980b9', 
    edgecolor='#1b4f72', 
    alpha=0.85
)

# Label count on top of each custom bin bar
for count, bin_left, bin_right in zip(counts2, bins2[:-1], bins2[1:]):
    if count > 0:
        ax2.text((bin_left + bin_right) / 2, count + 1.2, f'{int(count)}', ha='center', va='bottom', fontweight='bold', fontsize=9)

ax2.set_title('2. Custom Defined Bins (Age Groups)', fontweight='bold')
ax2.set_xlabel('Age Group Ranges')
ax2.set_ylabel('Frequency / Count')
ax2.set_xticks(custom_bins) # Match tick marks to bin boundaries
ax2.grid(axis='y', linestyle='--', alpha=0.5)

# -------------------------------------------------------------
# Overall Layout & Display
# -------------------------------------------------------------
fig.suptitle('Understanding Histogram Bins in Matplotlib', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()