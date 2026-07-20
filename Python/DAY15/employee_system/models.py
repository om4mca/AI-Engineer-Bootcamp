"""OOP Domain models demonstrating Inheritance, Encapsulation, and Polymorphism."""

from abc import ABC, abstractmethod

class Employee(ABC):
    """Abstract Base Class for all employees."""
    def __init__(self, emp_id: str, name: str, department: str, role: str):
        self._emp_id = emp_id.strip().upper()
        self._name = name.strip().title()
        self._department = department.strip().title()
        self._role = role.strip().title()

    @property
    def emp_id(self) -> str:
        return self._emp_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def department(self) -> str:
        return self._department

    @property
    def role(self) -> str:
        return self._role

    @abstractmethod
    def calculate_salary(self) -> float:
        """Polymorphic method for salary calculation."""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Converts object instance to dict representation for storage."""
        pass

    def __str__(self) -> str:
        return (f"[{self._emp_id}] {self._name} | Department: {self._department} | "
                f"Role: {self._role} | Estimated Monthly Salary: ${self.calculate_salary():,.2f}")


class FullTimeEmployee(Employee):
    """Represents a salaried full-time employee with performance bonus."""
    def __init__(self, emp_id: str, name: str, department: str, role: str, base_salary: float, bonus: float = 0.0):
        super().__init__(emp_id, name, department, role)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self) -> float:
        return self.base_salary + self.bonus

    def to_dict(self) -> dict:
        return {
            "emp_id": self._emp_id,
            "type": "FullTime",
            "name": self._name,
            "department": self._department,
            "role": self._role,
            "base_salary": self.base_salary,
            "bonus": self.bonus
        }


class PartTimeEmployee(Employee):
    """Represents an hourly part-time employee."""
    def __init__(self, emp_id: str, name: str, department: str, role: str, hourly_rate: float, hours_worked: float):
        super().__init__(emp_id, name, department, role)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self) -> float:
        return self.hourly_rate * self.hours_worked

    def to_dict(self) -> dict:
        return {
            "emp_id": self._emp_id,
            "type": "PartTime",
            "name": self._name,
            "department": self._department,
            "role": self._role,
            "hourly_rate": self.hourly_rate,
            "hours_worked": self.hours_worked
        }