import matplotlib.pyplot as plt
import numpy as np

# Set seed for reproducible data
np.random.seed(42)

# Generate synthetic salary data (skewed distribution)
salaries = np.random.lognormal(mean=11.2, sigma=0.4, size=250)

# 1. Figure setup
plt.figure(figsize=(10, 5))

# 2. Plot Histogram
counts, bins, patches = plt.hist(
    salaries,
    bins=12,
    color='#2b5c8f',       # Steel blue fill
    edgecolor='#1a334e',   # Dark blue border
    linewidth=1.2,
    alpha=0.85
)

# 3. Add Summary Lines (Mean & Median)
mean_salary = np.mean(salaries)
median_salary = np.median(salaries)

plt.axvline(
    mean_salary, color='#e74c3c', linestyle='--', linewidth=2,
    label=f'Mean Salary (${mean_salary:,.0f})'
)
plt.axvline(
    median_salary, color='#2ecc71', linestyle='-', linewidth=2,
    label=f'Median Salary (${median_salary:,.0f})'
)

# 4. Add Count Labels on Bars
for count, bin_left, bin_right in zip(counts, bins[:-1], bins[1:]):
    if count > 0:
        plt.text(
            (bin_left + bin_right) / 2,
            count + 1,
            f'{int(count)}',
            ha='center', va='bottom',
            fontsize=9, fontweight='bold'
        )

# 5. Styling & Formatting
plt.title('Employee Salary Distribution', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Annual Salary ($)', fontsize=11, labelpad=10)
plt.ylabel('Number of Employees (Frequency)', fontsize=11, labelpad=10)

# Format X-axis with currency commas ($100,000)
plt.gca().xaxis.set_major_formatter('${x:,.0f}')

# Adjust Y-axis limit for label breathing room
plt.ylim(0, max(counts) + 8)

# Grid & Spines
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.legend(loc='upper right', frameon=True)
plt.tight_layout()

# Save & Display
plt.savefig('salary_histogram.png', dpi=300)
plt.show()