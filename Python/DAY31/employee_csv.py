import pandas as pd
import numpy as np


# 1. Read CSV
# ==========================================
df = pd.read_csv("E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31//employee.csv")

# ==========================================
# 2. Display Dataset
# ==========================================
print("=== 2. Full Dataset ===")
print(df)
print("\n" + "="*50 + "\n")

# ==========================================
# 3. Show info()
# ==========================================
print("=== 3. Dataset Info ===")
df.info()
print("\n" + "="*50 + "\n")

# ==========================================
# 4. Show describe()
# ==========================================
print("=== 4. Statistical Summary (describe) ===")
print(df.describe())
print("\n" + "="*50 + "\n")

# ==========================================
# 5. Filter IT Department
# ==========================================
it_employees = df[df['Department'] == 'IT']
print("=== 5. IT Department Employees ===")
print(it_employees)
print("\n" + "="*50 + "\n")

# ==========================================
# 6 & 7. Group by Department & Average Salary
# ==========================================
dept_summary = df.groupby('Department', as_index=False).agg(
    Headcount=('EmployeeID', 'count'),
    Average_Salary=('Salary', 'mean'),
    Total_Payroll=('Salary', 'sum'),
    Average_Experience=('Experience', 'mean')
)

# Format Average Salary column for clean viewing
dept_summary['Average_Salary'] = dept_summary['Average_Salary'].round(2)

print("=== 6 & 7. Department Aggregations & Average Salary ===")
print(dept_summary)
print("\n" + "="*50 + "\n")

# ==========================================
# 8. Save Cleaned CSV
# ==========================================
df.to_csv("employees_cleaned.csv", index=False)
print("✔ Step 8: Cleaned CSV saved as 'employees_cleaned.csv'")

# ==========================================
# 9. Export Excel Report (Multi-Sheet)
# ==========================================
with pd.ExcelWriter("employee_analytics_report.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Full Data", index=False)
    it_employees.to_excel(writer, sheet_name="IT Department", index=False)
    dept_summary.to_excel(writer, sheet_name="Department Summary", index=False)

print("✔ Step 9: Multi-sheet Excel report saved as 'employee_analytics_report.xlsx'")
print("\n" + "="*50 + "\n")

# ==========================================
# 10. Print Final Summary
# ==========================================
total_employees = len(df)
overall_avg_salary = df['Salary'].mean()
top_dept_payroll = dept_summary.loc[dept_summary['Total_Payroll'].idxmax()]

print("=== 10. Executive Summary ===")
print(f"• Total Employees Analyzed : {total_employees}")
print(f"• Overall Average Salary   : ${overall_avg_salary:,.2f}")
print(f"• Highest Payroll Dept     : {top_dept_payroll['Department']} (${top_dept_payroll['Total_Payroll']:,.2f})")
print(f"• IT Staff Count           : {len(it_employees)}")
print("="*50)