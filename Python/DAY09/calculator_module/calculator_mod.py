#--------------------------------------------
# AI Engineer Bootcamp
# Day 8
# Program: Calculator Module
# Author: Om Roy
# Date: 11-07-2026
#--------------------------------------------


import math
from datetime import datetime

class AdvancedCalculator:
    def __init__(self):
        """Initializes the calculator engine with an empty audit log trail."""
        self.history_log = []

    def _log_transaction(self, operation: str, expression: str, result: float):
        """Internal helper to capture mathematical audit paths."""
        self.history_log.append({
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "operation": operation,
            "expression": expression,
            "result": result
        })

    def add(self, a: float, b: float) -> float:
        res = a + b
        self._log_transaction("Addition", f"{a} + {b}", res)
        return res

    def subtract(self, a: float, b: float) -> float:
        res = a - b
        self._log_transaction("Subtraction", f"{a} - {b}", res)
        return res

    def multiply(self, a: float, b: float) -> float:
        res = a * b
        self._log_transaction("Multiplication", f"{a} * {b}", res)
        return res

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Mathematical breakdown: Core division by zero is undefined.")
        res = a / b
        self._log_transaction("Division", f"{a} / {b}", res)
        return res

    def square_root(self, value: float) -> float:
        if value < 0:
            raise ValueError("Domain Error: Square root operations require non-negative inputs.")
        res = math.sqrt(value)
        self._log_transaction("Square Root", f"sqrt({value})", res)
        return res

    def factorial(self, value: int) -> int:
        if value < 0:
            raise ValueError("Domain Error: Factorials require non-negative integers.")
        res = math.factorial(value)
        self._log_transaction("Factorial", f"{value}!", res)
        return res

    def get_history(self) -> list:
        """Returns the chronological runtime memory array."""
        return self.history_log