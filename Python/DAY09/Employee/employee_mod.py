#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Employee Module
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------

import uuid
import math
from datetime import datetime

class Employee:
    def __init__(self, name: str, base_salary: float, performance_score: int = 3):
        """
        Initializes a core employee profile.
        performance_score scales from 1 (lowest) to 5 (highest).
        """
        self.employee_id = f"EMP-{str(uuid.uuid4())[:6].upper()}"
        self.name = name
        self.base_salary = base_salary
        self.performance_score = performance_score
        self.hire_date = datetime.now().strftime("%Y-%m-%d")

    def calculate_bonus(self) -> float:
        """Calculates performance bonus percentages dynamically using mathematical thresholds."""
        if self.performance_score == 5:
            multiplier = 0.20  # 20% top-performer bonus
        elif self.performance_score == 4:
            multiplier = 0.10  # 10% high-performer bonus
        elif self.performance_score == 3:
            multiplier = 0.05  # 5% standard bonus
        else:
            multiplier = 0.0
            
        return round(self.base_salary * multiplier, 2)

    def calculate_net_pay(self, tax_rate: float = 0.15) -> float:
        """Computes ultimate take-home earnings post-tax allocations."""
        gross_earnings = self.base_salary + self.calculate_bonus()
        tax_deduction = gross_earnings * tax_rate
        net_pay = gross_earnings - tax_deduction
        
        # Ceil values to the next integer value for clean account transfers
        return math.ceil(net_pay)

    def get_details(self) -> dict:
        """Returns structured map of employee metrics."""
        return {
            "ID": self.employee_id,
            "Name": self.name,
            "Hired": self.hire_date,
            "Performance Rating": self.performance_score,
            "Base Pay": self.base_salary,
            "Bonus": self.calculate_bonus(),
            "Net Take Home": self.calculate_net_pay()
        }