import matplotlib.pyplot as plt

# Sample Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue = [12, 15, 14, 28, 22, 25]  # Peak in April (Index 3, Value 28)

plt.figure(figsize=(9, 5))
plt.plot(months, revenue, marker='o', color='#1f77b4', linewidth=2)

# -------------------------------------------------------------
# Add Annotation
# -------------------------------------------------------------
plt.annotate(
    'Peak Revenue ($28k)',     # Label text
    xy=(3, 28),                 # Target point (Apr = index 3, Value = 28)
    xytext=(1.5, 30),           # Label text placement position
    arrowprops=dict(
        facecolor='black',      # Arrow head fill color
        shrink=0.08,            # Padding between arrow tip and point
        width=1.5,              # Arrow stem width
        headwidth=8             # Arrow head size
    ),
    fontsize=10,
    fontweight='bold',
    color='#c0392b'
)

plt.title('Monthly Revenue with Peak Annotation', fontweight='bold')
plt.ylabel('Revenue ($k)')
plt.ylim(10, 35)  # Extra Y space for annotation text
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()