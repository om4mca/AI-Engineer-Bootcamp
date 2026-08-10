import matplotlib.pyplot as plt

# 1. Dataset
departments = ["Cardiology", "Orthopedic", "General", "Pediatrics"]
patients = [120, 95, 150, 80]

# 2. Data Analysis (Insights Extraction)
max_patients = max(patients)
min_patients = min(patients)

highest_dept = departments[patients.index(max_patients)]
lowest_dept = departments[patients.index(min_patients)]
total_patients = sum(patients)

# 3. Create Bar Chart Visualisation
plt.figure(figsize=(9, 5))

# Plot bars and color-code min/max values
bars = plt.bar(departments, patients, color='#008080', edgecolor='#004d4d', width=0.55)

for bar in bars:
    yval = bar.get_height()
    
    # Color highlighting
    if yval == max_patients:
        bar.set_color('#27ae60')  # Green for Highest
    elif yval == min_patients:
        bar.set_color('#e74c3c')  # Red for Lowest
        
    # Value labels on top of each bar
    plt.text(
        bar.get_x() + bar.get_width() / 2, 
        yval + 2.5, 
        f'{yval}', 
        ha='center', va='bottom', 
        fontsize=10, fontweight='bold'
    )

# Formatting Chart
plt.title('Hospital Patient Distribution by Department', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Department Name', fontsize=11, labelpad=10)
plt.ylabel('Number of Patients', fontsize=11, labelpad=10)
plt.ylim(0, max_patients + 25)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Spines cleanup
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()

# Display Chart
plt.show()

# 4. Print Insights Report to Console
print("=" * 45)
print("         HOSPITAL DATA ANALYSIS REPORT        ")
print("=" * 45)
print(f"• Total Patients Across All Departments : {total_patients}")
print(f"• Highest Patient Volume : {highest_dept} ({max_patients} Patients)")
print(f"• Lowest Patient Volume  : {lowest_dept} ({min_patients} Patients)")
print("=" * 45)