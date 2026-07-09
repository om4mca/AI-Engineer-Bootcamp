# ------------------------------------------
# AI Engineer Bootcamp
# Day 7
# Program: Employee Attendance System
# Author: Om Roy
# Date: 09-07-2026
#------------------------------------------


# Initial sample data
attendance = {
    "EMP001": "Present",
    "EMP002": "Absent"
}

def add_employee():
    emp_id = input("Enter new Employee ID (e.g., EMP003): ").strip().upper()
    if emp_id in attendance:
        print("Error: This Employee ID already exists in the system.")
        return
    
    # By default, new employees can start with an unassigned or absent status
    attendance[emp_id] = "Absent"
    print(f"Employee {emp_id} added to the system (Default: Absent).")

def mark_present():
    emp_id = input("Enter Employee ID to mark Present: ").strip().upper()
    if emp_id in attendance:
        attendance[emp_id] = "Present"
        print(f"Employee {emp_id} marked Present.")
    else:
        print("Employee ID not found. Add them first using Option 1.")

def mark_absent():
    emp_id = input("Enter Employee ID to mark Absent: ").strip().upper()
    if emp_id in attendance:
        attendance[emp_id] = "Absent"
        print(f"Employee {emp_id} marked Absent.")
    else:
        print("Employee ID not found. Add them first using Option 1.")

def display_attendance():
    if not attendance:
        print("No employees registered in the system.")
        return
    
    print("\n--- Attendance Sheet ---")
    print(f"{'Employee ID':<15} | {'Status':<10}")
    print("-" * 30)
    for emp_id, status in attendance.items():
        # Quick visual indicator for easier reading
        icon = "🟢" if status == "Present" else "🔴"
        print(f"{emp_id:<15} | {icon} {status:<10}")
    print("-" * 30)

def count_present():
    # Loop through values and count how many are "Present"
    present_count = list(attendance.values()).count("Present")
    total_count = len(attendance)
    print(f"\n Present: {present_count} / Total Registered: {total_count}")

def main():
    while True:
        print("\n--------- EMPLOYEE ATTENDANCE SYSTEM ---------")
        print("1. Add Employee")
        print("2. Mark Present")
        print("3. Mark Absent")
        print("4. Display Attendance")
        print("5. Count Present Employees")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            mark_present()
        elif choice == '3':
            mark_absent()
        elif choice == '4':
            display_attendance()
        elif choice == '5':
            count_present()
        elif choice == '6':
            print("Exiting system. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()