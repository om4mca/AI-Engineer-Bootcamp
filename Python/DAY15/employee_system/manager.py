"""Core Business Manager executing system operations."""

from typing import List, Dict
from models import Employee, FullTimeEmployee, PartTimeEmployee
from storage import StorageHandler
from exceptions import EmployeeNotFoundError, DuplicateEmployeeError

class EmployeeManager:
    def __init__(self, filepath: str = "employees_db.json"):
        self.storage = StorageHandler(filepath)
        self._employees: Dict[str, Employee] = {}
        self._load_all()

    def _load_all(self) -> None:
        records = self.storage.load_records()
        for rec in records:
            emp_type = rec.get("type")
            if emp_type == "FullTime":
                emp = FullTimeEmployee(
                    rec["emp_id"], rec["name"], rec["department"],
                    rec["role"], rec["base_salary"], rec.get("bonus", 0.0)
                )
            elif emp_type == "PartTime":
                emp = PartTimeEmployee(
                    rec["emp_id"], rec["name"], rec["department"],
                    rec["role"], rec["hourly_rate"], rec["hours_worked"]
                )
            else:
                continue
            self._employees[emp.emp_id] = emp

    def _sync(self) -> None:
        records = [emp.to_dict() for emp in self._employees.values()]
        self.storage.save_records(records)

    def add_employee(self, employee: Employee) -> None:
        if employee.emp_id in self._employees:
            raise DuplicateEmployeeError(employee.emp_id)
        self._employees[employee.emp_id] = employee
        self._sync()

    def search_employee(self, emp_id: str) -> Employee:
        emp_id = emp_id.strip().upper()
        if emp_id not in self._employees:
            raise EmployeeNotFoundError(emp_id)
        return self._employees[emp_id]

    def get_all_employees(self) -> List[Employee]:
        return list(self._employees.values())

    def update_employee(self, emp_id: str, **kwargs) -> Employee:
        emp = self.search_employee(emp_id)

        if kwargs.get("department"):
            emp._department = kwargs["department"].strip().title()
        if kwargs.get("role"):
            emp._role = kwargs["role"].strip().title()

        if isinstance(emp, FullTimeEmployee):
            if kwargs.get("base_salary") is not None:
                emp.base_salary = kwargs["base_salary"]
            if kwargs.get("bonus") is not None:
                emp.bonus = kwargs["bonus"]

        elif isinstance(emp, PartTimeEmployee):
            if kwargs.get("hourly_rate") is not None:
                emp.hourly_rate = kwargs["hourly_rate"]
            if kwargs.get("hours_worked") is not None:
                emp.hours_worked = kwargs["hours_worked"]

        self._sync()
        return emp