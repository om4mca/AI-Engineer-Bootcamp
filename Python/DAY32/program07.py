import matplotlib.pyplot as plt
import numpy as np

# 1. Generate Sample Age Data (e.g., ages of 100 participants)
np.random.seed(42) # For reproducible random data
ages = [
    18, 19, 21, 22, 23, 24, 25, 25, 26, 27, 28, 29, 30, 31, 31, 32, 33, 34, 35, 
    36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48, 50, 52, 54, 55, 58, 60, 62, 65
]

# 2. Define Custom Age Bins (e.g., 10-year age groups)
bins = [10, 20, 30, 40, 50, 60, 70]

# 3. Create Figure Container
plt.figure(figsize=(9, 5))

# 4. Plot Histogram
counts, edges, bars = plt.hist(
    ages, 
    bins=bins, 
    color='#3498db',        # Clean blue fill
    edgecolor='#1f3a52',    # Dark border between bins
    linewidth=1.2,
    alpha=0.85
)

# 5. Add Mean Line Annotation
mean_age = np.mean(ages)
plt.axvline(
    mean_age, 
    color='#e74c3c', 
    linestyle='--', 
    linewidth=2, 
    label=f'Mean Age ({mean_age:.1f} yrs)'
)

# 6. Add Count Labels on Top of Each Bin Bar
for i in range(len(counts)):
    if counts[i] > 0:
        plt.text(
            (edges[i] + edges[i+1]) / 2, # Midpoint of bin range
            counts[i] + 0.3,              # Height slightly above bar
            int(counts[i]), 
            ha='center', va='bottom', 
            fontsize=10, fontweight='bold'
        )

# 7. Titles & Axis Labels
plt.title('Participant Age Distribution', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Age Group (Years)', fontsize=11, labelpad=10)
plt.ylabel('Number of People (Frequency)', fontsize=11, labelpad=10)

# Set X-axis ticks to match explicit bin boundaries
plt.xticks(bins)

# Grid & Spines Formatting
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.legend(loc='upper right')
plt.tight_layout()

# 8. Display Plot
plt.show()