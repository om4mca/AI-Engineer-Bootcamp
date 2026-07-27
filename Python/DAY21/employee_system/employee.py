from exceptions import ValidationError

class Employee:
    """Employee Domain Model with Built-in Validation."""
    def __init__(self, emp_id, name, department, salary, email):
        self.emp_id = str(emp_id).strip()
        self.name = str(name).strip()
        self.department = str(department).strip()
        self.salary = float(salary)
        self.email = str(email).strip()
        self.validate()

    def validate(self):
        """Feature 8: Data Validation Rules."""
        if not self.emp_id:
            raise ValidationError("Employee ID cannot be empty.")
        if not self.name or len(self.name) < 2:
            raise ValidationError("Name must be at least 2 characters long.")
        if not self.department:
            raise ValidationError("Department cannot be empty.")
        if self.salary <= 0:
            raise ValidationError("Salary must be greater than zero.")
        if "@" not in self.email or "." not in self.email:
            raise ValidationError("Invalid email address format.")

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["emp_id"],
            data["name"],
            data["department"],
            data["salary"],
            data["email"]
        )

    def __str__(self):
        return f"ID: {self.emp_id:<6} | Name: {self.name:<15} | Dept: {self.department:<12} | Salary: ₹{self.salary:<10.2f} | Email: {self.email}"