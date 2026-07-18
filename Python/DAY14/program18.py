

#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: ---Payroll  Class---
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

from abc import ABC, abstractmethod

class Employee(ABC):
    """Abstract base class representing a generic company employee."""
    def __init__(self, emp_id: int, name: str):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def calculate_payroll(self) -> float:
        """Abstract method to calculate net pay."""
        pass


class SalaryEmployee(Employee):
    """Subclass for employees paid a fixed monthly salary."""
    def __init__(self, emp_id: int, name: str, weekly_salary: float):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self) -> float:
        return self.weekly_salary


class HourlyEmployee(Employee):
    """Subclass for employees paid by the hour with overtime support."""
    def __init__(self, emp_id: int, name: str, hours_worked: float, hourly_rate: float):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self) -> float:
        if self.hours_worked <= 40:
            return self.hours_worked * self.hourly_rate
        
        # 1.5x overtime multiplier for hours exceeding 40
        regular_pay = 40 * self.hourly_rate
        overtime_hours = self.hours_worked - 40
        overtime_pay = overtime_hours * (self.hourly_rate * 1.5)
        return regular_pay + overtime_pay


class PayrollSystem:
    """Dispatches and tracks financial distributions across employee pools."""
    def __init__(self):
        self.employee_registry = []

    def add_employee(self, employee: Employee):
        self.employee_registry.append(employee)

    def process_payroll(self):
        print("=== PROCESSING COMPANY PAYROLL ===")
        total_payout = 0
        for emp in self.employee_registry:
            pay = emp.calculate_payroll()
            total_payout += pay
            print(f"ID: {emp.emp_id} | Name: {emp.name:<10} | Gross Pay: ${pay:,.2f}")
        print("==================================")
        print(f"Total Disbursed Funds: ${total_payout:,.2f}\n")


# Instantiate management system
payroll = PayrollSystem()

# Register diverse employee archetypes
payroll.add_employee(SalaryEmployee(101, "Om", 1500.00))
payroll.add_employee(HourlyEmployee(102, "Sudhir", 45, 20.00))  # 5 hours overtime

# Compute global disbursements
payroll.process_payroll()
