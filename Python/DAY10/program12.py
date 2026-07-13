#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: Employee Salary Validation
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------

class InvalidSalaryError(Exception):
    """Raised when a salary figure violates logical payroll boundaries."""
    pass

class InvalidEmployeeDataError(Exception):
    """Raised when an structural field (like Employee ID) fails validation."""
    pass


class PayrollSystem:
    # Business standard constants
    MIN_SALARY = 1500.00       # Minimum wage floor rule
    MAX_SALARY = 250000.00     # Internal compliance ceiling cap

    @staticmethod
    def process_salary(emp_id, salary_input):
        # 1. Structural Validation
        emp_id = str(emp_id).strip()
        if not emp_id or not emp_id.isalnum():
            raise InvalidEmployeeDataError("Employee ID must be a non-empty alphanumeric string.")

        # 2. Data Type Handling
        try:
            salary = float(salary_input)
        except ValueError:
            raise ValueError("Salary must be a valid numeric amount (do not include currency symbols or commas).")

        # 3. Logical Compliance Validation
        if salary < 0:
            raise InvalidSalaryError("Process Denied: Base salary components cannot be negative numbers.")
            
        if salary < PayrollSystem.MIN_SALARY:
            raise InvalidSalaryError(
                f"Compliance Alert: Salary ({salary:,.2f}) falls below the corporate regulatory floor of {PayrollSystem.MIN_SALARY:,.2f}."
            )
            
        if salary > PayrollSystem.MAX_SALARY:
            raise InvalidSalaryError(
                f"Compliance Alert: Salary ({salary:,.2f}) exceeds the maximum authorized payroll cap of {PayrollSystem.MAX_SALARY:,.2f}."
            )

        # Success Return Block
        return {
            "ID": emp_id,
            "Gross": salary,
            "Monthly_Tax": salary * 0.22 # Sample calculations safely shielded by try boundaries
        }


def main():
    print("=== Corporate Payroll Configuration Interface ===")
    print(f"Limits Enforced -> Min: {PayrollSystem.MIN_SALARY:,.2f} | Max: {PayrollSystem.MAX_SALARY:,.2f}\n")

    while True:
        try:
            emp_id = input("Enter Employee ID (or type 'quit' to exit): ").strip()
            if emp_id.lower() == 'quit':
                break

            salary_raw = input(f"Enter Annual Gross Salary for [{emp_id}]: ").strip()

            # Process transaction through the compliance gate
            payroll_record = PayrollSystem.process_salary(emp_id, salary_raw)

        except ValueError as e:
            print(f"\n[Formatting Error]: {e}\n")
            
        except InvalidEmployeeDataError as e:
            print(f"\n[Data Entry Error]: {e}\n")
            
        except InvalidSalaryError as e:
            print(f"\n[Policy Violation]: {e}\n")
            
        else:
            print(f"\n[Record Verified Successfully]")
            print(f" -> Employee Ref ID : {payroll_record['ID']}")
            print(f" -> Approved Gross  : {payroll_record['Gross']:,.2f}")
            print(f" -> Est. Monthly Tax: {payroll_record['Monthly_Tax']:,.2f}\n")
            
        finally:
            print("-" * 55)

    print("\nSystem session closed. All verified records committed to ledger.")


if __name__ == "__main__":
    main()



# end of the program     