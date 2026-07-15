#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Employee Class
# Author: Om Roy
# Date: 12-07-2026
#--------------------------------------------

class Employee:
    def __init__(self, employee_id: str, name: str, position: str, salary: float):
        """Initializes a new corporate employee record."""
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
        self.performance_rating = "Not Rated"  # Track employee growth

    def display_employee(self):
        """Prints the comprehensive employee record profile."""
        print(f"\n--- Employee Profile: {self.employee_id} ---")
        print(f"Name:        {self.name}")
        print(f"Position:    {self.position}")
        print(f"Performance: {self.performance_rating}")
        print(f"Base Salary: {self.salary:,.2f}")

    def promote_employee(self, new_position: str, raise_percentage: float):
        """Promotes the employee to a new role and updates their pay simultaneously."""
        if not new_position or not isinstance(new_position, str):
            print("[Error] Promotion failed: Invalid job title.")
            return

        print(f"\n[PROMOTION] 🎉 {self.name} is moving up from {self.position} to {new_position}!")
        self.position = new_position
        
        if raise_percentage > 0:
            self.adjust_salary(raise_percentage)

    def adjust_salary(self, percentage: float):
        """Adjusts base compensation by a dynamic percentage modifier."""
        action = "raise" if percentage > 0 else "reduction"
        old_salary = self.salary
        self.salary *= (1 + percentage / 100)
        print(f"[Compensation] Approved {percentage}% {action}. Salary changed from {old_salary:,.2f} to {self.salary:,.2f}.")

    def assign_performance_rating(self, rating: str):
        """Applies internal performance tier parameters."""
        valid_ratings = ["Needs Improvement", "Meets Expectations", "Exceeds Expectations", "Outstanding"]
        if rating in valid_ratings:
            print(f"[HR Sync] {self.name}'s mid-year review locked in as: '{rating}'")
            self.performance_rating = rating
        else:
            print(f"[Error] Review rejected. Rating must be one of: {valid_ratings}")


# --- Performance & Verification Showcase ---
if __name__ == "__main__":
    print("Opening Global Directory Ecosystem...")

    # Instantiating various corporate employee tiers
    emp1 = Employee("EMP-206", "Om Roy", "Senior Developer", 115000.00)
    emp2 = Employee("EMP-412", "Sudhir Kumar", "UX Designer", 82000.00)

    # Initial Audit
    emp1.display_employee()
    emp2.display_employee()

    print("\n" + "="*40 + "\nExecuting Quarterly Enterprise Changes...")

    # Reviewing & Promoting Team Members
    emp1.assign_performance_rating("Outstanding")
    emp1.promote_employee("Lead Software Architect", 12.5)  # Promotion with a 12.5% raise

    emp2.assign_performance_rating("Exceeds Expectations")
    emp2.adjust_salary(4.0)  # Standard merit increase

    # Final Verification
    print("\n" + "="*40 + "\nFinal Employee Directory Output:")
    emp1.display_employee()
    emp2.display_employee()