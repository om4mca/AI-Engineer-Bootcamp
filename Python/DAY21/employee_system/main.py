from service import EmployeeService

def print_menu():
    print("\n" + "💼 EMPLOYEE MANAGEMENT SYSTEM")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Save Records to File")
    print("7. Load Records from File")
    print("8. Exit")

def main():
    service = EmployeeService()
    service.load_from_file()  # Auto-load existing records at startup

    while True:
        print_menu()
        choice = input("\nEnter choice (1-8): ").strip()

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            salary = input("Enter Salary: ")
            email = input("Enter Email: ")
            
            try:
                service.add_employee(emp_id, name, dept, float(salary), email)
            except ValueError:
                print("❌ Invalid input: Salary must be a numerical value.")

        elif choice == "2":
            service.view_all_employees()

        elif choice == "3":
            emp_id = input("Enter Employee ID to Search: ")
            service.search_employee(emp_id)

        elif choice == "4":
            emp_id = input("Enter Employee ID to Update: ")
            print("(Press Enter without typing to keep existing field values)")
            name = input("New Name: ")
            dept = input("New Department: ")
            salary = input("New Salary: ")
            email = input("New Email: ")

            parsed_salary = float(salary) if salary.strip() else None
            
            service.update_employee(
                emp_id=emp_id,
                name=name if name else None,
                department=dept if dept else None,
                salary=parsed_salary,
                email=email if email else None
            )

        elif choice == "5":
            emp_id = input("Enter Employee ID to Delete: ")
            service.delete_employee(emp_id)

        elif choice == "6":
            service.save_to_file()

        elif choice == "7":
            service.load_from_file()

        elif choice == "8":
            service.save_to_file()  # Auto-save before exit
            print("👋 Session ended. Thank you!")
            break
        else:
            print("⚠️ Invalid menu selection. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()