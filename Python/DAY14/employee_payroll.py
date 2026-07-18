#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program:  Employee Payroll System
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

# employee_payroll.py

class EmployeePayroll:
    # Class variables for corporate-wide standard percentages
    HRA_PERCENT = 0.15  # 15% House Rent Allowance
    DA_PERCENT = 0.10   # 10% Dearness Allowance

    def __init__(self, emp_id: str, name: str, department: str, basic_salary: float, bonus: float = 0.0):
        """
        Constructor (__init__): Initializes the employee's personal 
        and basic financial profile records.
        """
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.basic_salary = basic_salary
        self.bonus = bonus

    @classmethod
    def from_string(cls, data_string: str):
        """
        Class Method: Acts as an alternative constructor. 
        Parses a comma-separated string to instantiate the class object automatically.
        Useful when reading lines directly from text data storage or log streams.
        """
        # Expected Format: "ID,Name,Dept,BasicSalary,Bonus"
        emp_id, name, department, basic_str, bonus_str = data_string.split(",")
        return cls(emp_id, name, department, float(basic_str), float(bonus_str))

    @staticmethod
    def calculate_tax(gross_income: float) -> float:
        """
        Static Method: An isolated utility function. 
        It does not rely on specific class properties or individual instance data, 
        making it reusable for generic income tax evaluations.
        """
        # Simple slab system: 10% tax if income is under 5,000, otherwise 20%
        if gross_income <= 5000:
            return gross_income * 0.10
        else:
            return (5000 * 0.10) + ((gross_income - 5000) * 0.20)

    def calculate_hra(self) -> float:
        return self.basic_salary * self.HRA_PERCENT

    def calculate_da(self) -> float:
        return self.basic_salary * self.DA_PERCENT

    def calculate_gross_salary(self) -> float:
        """Gross Salary = Basic + HRA + DA + Bonus"""
        return self.basic_salary + self.calculate_hra() + self.calculate_da() + self.bonus

    def calculate_net_salary(self) -> float:
        """Net Salary = Gross Salary - Tax Deduction"""
        gross = self.calculate_gross_salary()
        tax = self.calculate_tax(gross)
        return gross - tax

    def display_payslip(self):
        """Generates and prints a structured corporate salary ledger sheet."""
        gross = self.calculate_gross_salary()
        tax = self.calculate_tax(gross)
        net = self.calculate_net_salary()

        print("=" * 42)
        print(f"         CORPORATE PAYROLL BREAKDOWN      ")
        print("=" * 42)
        print(f"Employee ID : {self.emp_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print("-" * 42)
        print(f"Basic Salary      : {self.basic_salary:10.2f}")
        print(f"HRA (15%)         : {self.calculate_hra():10.2f}")
        print(f"DA (10%)          : {self.calculate_da():10.2f}")
        print(f"Performance Bonus : {self.bonus:10.2f}")
        print("-" * 42)
        print(f"Gross Earnings    : {gross:10.2f}")
        print(f"Tax Deducted      : -{tax:9.2f}")
        print("=" * 42)
        print(f"NET TAKE-HOME     : {net:10.2f}")
        print("=" * 42 + "\n")


# --- Demonstration ---
if __name__ == "__main__":
    # 1. Using the standard Constructor
    print("Initializing Employee 1 via Standard Constructor...")
    emp1 = EmployeePayroll(
        emp_id="EMP-101", 
        name="Om Roy", 
        department="Operations", 
        basic_salary=95000.00, 
        bonus=3500.00
    )
    emp1.display_payslip()

    # 2. Using the Class Method constructor alternative
    print("Initializing Employee 2 via Class Method String Parser...")
    raw_csv_line = "EMP-202,Sudhir Kumar,Logistics,6200.00,500.00"
    emp2 = EmployeePayroll.from_string(raw_csv_line)
    emp2.display_payslip()
    
    # 3. Demonstrating isolated call to the Static Method
    print("Testing Standalone Static Tax Utility (External Evaluation):")
    sample_income = 7500.00
    calculated_tax = EmployeePayroll.calculate_tax(sample_income)
    print(f"Estimated tax on a generic corporate lump sum of {sample_income:.2f} is {calculated_tax:.2f}")