"""CLI Driver for Employee Management System."""

from manager import EmployeeManager
from models import FullTimeEmployee, PartTimeEmployee
from exceptions import EmployeeSystemError

def prompt_float(prompt: str) -> float:
    while True:
        try:
            val = float(input(prompt).strip())
            if val < 0:
                print("⚠️ Value must be a non-negative number.")
                continue
            return val
        except ValueError:
            print("⚠️ Invalid entry. Please enter a valid decimal number.")


def prompt_string(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("⚠️ Entry cannot be left blank.")


def main():
    manager = EmployeeManager()

    while True:
        print("\n" + "=" * 45)
        print("     💼 EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Employee")
        print("4. Calculate Payroll / View Salaries")
        print("5. Exit")
        print("=" * 45)

        choice = input("Select an option (1-5): ").strip()

        try:
            if choice == "1":
                print("\n--- Add New Employee ---")
                emp_id = prompt_string("Employee ID (e.g. E101): ")
                name = prompt_string("Full Name: ")
                dept = prompt_string("Department: ")
                role = prompt_string("Job Role: ")

                print("Employment Type: [1] Full-Time  [2] Part-Time")
                emp_type = input("Choice (1 or 2): ").strip()

                if emp_type == "1":
                    base_sal = prompt_float("Base Monthly Salary ($): ")
                    bonus = prompt_float("Performance Bonus ($): ")
                    emp = FullTimeEmployee(emp_id, name, dept, role, base_sal, bonus)
                elif emp_type == "2":
                    rate = prompt_float("Hourly Rate ($): ")
                    hours = prompt_float("Hours Worked: ")
                    emp = PartTimeEmployee(emp_id, name, dept, role, rate, hours)
                else:
                    print("⚠️ Invalid employment type selected.")
                    continue

                manager.add_employee(emp)
                print(f"\n✅ Employee '{name}' added successfully!")

            elif choice == "2":
                print("\n--- Search Employee ---")
                emp_id = prompt_string("Enter Employee ID: ")
                emp = manager.search_employee(emp_id)
                print(f"\n✅ Record Found:\n{emp}")

            elif choice == "3":
                print("\n--- Update Employee ---")
                emp_id = prompt_string("Enter Employee ID to update: ")
                emp = manager.search_employee(emp_id)

                print("(Press Enter to skip updating a field)")
                dept = input(f"New Department [{emp.department}]: ").strip()
                role = input(f"New Role [{emp.role}]: ").strip()

                kwargs = {}
                if dept: kwargs["department"] = dept
                if role: kwargs["role"] = role

                if isinstance(emp, FullTimeEmployee):
                    sal_in = input(f"New Base Salary [{emp.base_salary}]: ").strip()
                    bonus_in = input(f"New Bonus [{emp.bonus}]: ").strip()
                    if sal_in: kwargs["base_salary"] = float(sal_in)
                    if bonus_in: kwargs["bonus"] = float(bonus_in)

                elif isinstance(emp, PartTimeEmployee):
                    rate_in = input(f"New Hourly Rate [{emp.hourly_rate}]: ").strip()
                    hours_in = input(f"New Hours Worked [{emp.hours_worked}]: ").strip()
                    if rate_in: kwargs["hourly_rate"] = float(rate_in)
                    if hours_in: kwargs["hours_worked"] = float(hours_in)

                updated_emp = manager.update_employee(emp_id, **kwargs)
                print(f"\n✅ Employee ID '{updated_emp.emp_id}' updated successfully!")

            elif choice == "4":
                print("\n--- Salary Calculation & Payroll Summary ---")
                employees = manager.get_all_employees()
                if not employees:
                    print("ℹ️ No employee records found.")
                else:
                    total_payroll = 0.0
                    for idx, emp in enumerate(employees, start=1):
                        salary = emp.calculate_salary()
                        total_payroll += salary
                        print(f"{idx}. {emp.name} ({emp.emp_id}) -> Monthly Payout: ${salary:,.2f}")
                    
                    print("-" * 45)
                    print(f"💰 TOTAL MONTHLY PAYROLL: ${total_payroll:,.2f}")

            elif choice == "5":
                print("\n👋 Exiting Employee Management System. Goodbye!")
                break

            else:
                print("⚠️ Invalid choice. Select an option between 1 and 5.")

        except EmployeeSystemError as e:
            print(f"\n🛑 System Error: {e}")
        except Exception as e:
            print(f"\n🛑 Unexpected Error: {e}")


if __name__ == "__main__":
    main()