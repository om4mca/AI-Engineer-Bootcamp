#--------------------------------------------
# AI Engineer Bootcamp
# Day 15
# Program: Employee model
# Author: Om Roy
# Date: 20-07-2026
#--------------------------------------------
from abc import ABC, abstractmethod
from typing import Dict, Any

class Employee(ABC):
    """Abstract Base Class for all employees."""
    def __init__(self, emp_id: str, name: str, department: str, role: str):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.role = role

    @property
    def emp_id(self) -> str:
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value: str):
        cleaned = value.strip().upper()
        if not cleaned:
            raise ValueError("Employee ID cannot be empty.")
        self._emp_id = cleaned

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        cleaned = value.strip().title()
        if not cleaned:
            raise ValueError("Name cannot be empty.")
        self._name = cleaned

    @abstractmethod
    def calculate_salary(self) -> float:
        """Polymorphic method for salary computation."""
        pass

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Serialization for JSON or database storage."""
        pass


class FullTimeEmployee(Employee):
    """Salaried full-time employee model."""
    def __init__(self, emp_id: str, name: str, department: str, role: str, base_salary: float, bonus: float = 0.0):
        super().__init__(emp_id, name, department, role)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self) -> float:
        return self.base_salary + self.bonus

    def to_dict(self) -> Dict[str, Any]:
        return {
            "emp_id": self.emp_id,
            "type": "FullTime",
            "name": self.name,
            "department": self.department,
            "role": self.role,
            "base_salary": self.base_salary,
            "bonus": self.bonus
        }


class PartTimeEmployee(Employee):
    """Hourly part-time employee model."""
    def __init__(self, emp_id: str, name: str, department: str, role: str, hourly_rate: float, hours_worked: float):
        super().__init__(emp_id, name, department, role)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self) -> float:
        return self.hourly_rate * self.hours_worked

    def to_dict(self) -> Dict[str, Any]:
        return {
            "emp_id": self.emp_id,
            "type": "PartTime",
            "name": self.name,
            "department": self.department,
            "role": self.role,
            "hourly_rate": self.hourly_rate,
            "hours_worked": self.hours_worked
        }


# Example Usage
if __name__ == "__main__":
    ft_emp = FullTimeEmployee("e101", "alice smith", "Engineering", "Backend Developer", 7500.0, 500.0)
    pt_emp = PartTimeEmployee("e102", "bob jones", "Design", "UI Designer", 45.0, 80)

    print(f"[{ft_emp.emp_id}] {ft_emp.name} | Monthly Pay: ${ft_emp.calculate_salary():,.2f}")
    print(f"[{pt_emp.emp_id}] {pt_emp.name} | Monthly Pay: ${pt_emp.calculate_salary():,.2f}")