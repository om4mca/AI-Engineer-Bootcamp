class Employee:

    def __init__(self, employee_id, name, role):
        self.employee_id = employee_id
        self.name = name
        self.role = role

    def display_info(self):
        return (
            f"ID: {self.employee_id}, "
            f"Name: {self.name}, "
            f"Role: {self.role}"
        )

    def __str__(self):
        return self.display_info()