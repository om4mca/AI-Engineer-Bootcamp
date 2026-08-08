import matplotlib.pyplot as plt

# 1. Define Student Data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank']
marks = [85, 92, 78, 65, 88, 95]

# 2. Create Figure Container
plt.figure(figsize=(9, 5))

# 3. Plot Vertical Bar Chart
bars = plt.bar(
    students, 
    marks, 
    color='#4c72b0',      # Soft blue fill
    edgecolor='#1d3557',  # Dark border line
    width=0.5             # Bar thickness
)

# 4. Add Score Annotations on Top of Each Bar
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # Center horizontally
        yval + 1.5,                          # Position slightly above the bar top
        f'{yval}',                           # Display value
        ha='center', va='bottom',            # Alignment
        fontsize=10, fontweight='bold'
    )

# 5. Styling & Formatting
plt.title('Student Final Exam Marks', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Student Name', fontsize=11, labelpad=10)
plt.ylabel('Marks (Out of 100)', fontsize=11, labelpad=10)

# Set Y-axis limits (0 to 105 to give space for score text)
plt.ylim(0, 105)

# Add horizontal gridlines
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Clean borders (remove top and right spines)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 6. Adjust Layout & Show Plot
plt.tight_layout()
plt.show()