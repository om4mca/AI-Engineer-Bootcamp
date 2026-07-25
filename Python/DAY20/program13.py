import os
from contextlib import contextmanager


class EmployeeFileWriter:
    """Helper class providing structured employee writing methods."""
    
    def __init__(self, file_handle):
        self.file = file_handle

    def write_employee(self, emp_id: str, name: str, role: str, department: str):
        """Formats and writes a CSV employee record."""
        record = f"{emp_id},{name},{role},{department}\n"
        self.file.write(record)
        print(f"  [WRITTEN] {emp_id} - {name} ({role})")

    def write_header(self):
        """Writes standard CSV headers."""
        self.file.write("EmployeeID,Name,Role,Department\n")


@contextmanager
def managed_employee_file(filename: str, mode: str = "w"):
    """
    Context Manager for employee file handling.
    Ensures setup, error logging, and guaranteed file closure.
    """
    print(f"--> [OPEN] Accessing file '{filename}' in mode '{mode}'...")
    file_handle = open(filename, mode, encoding="utf-8")
    writer = EmployeeFileWriter(file_handle)

    try:
        # Pass the writer interface to the 'with' block
        yield writer
    except IOError as err:
        print(f"--> [ERROR] I/O Error during file operations: {err}")
        raise
    except Exception as err:
        print(f"--> [ERROR] Execution failed inside context block: {err}")
        raise
    finally:
        # Guaranteed cleanup phase
        file_handle.close()
        print(f"--> [CLOSE] File '{filename}' closed safely.\n")


# ==========================================
# Practical Usage & Error Handling
# ==========================================
if __name__ == "__main__":
    file_path = "employees_data.csv"

    print("--- 1. Writing Employee Records ---")
    with managed_employee_file(file_path, mode="w") as emp_file:
        emp_file.write_header()
        emp_file.write_employee("E101", "Aarav Sharma", "Developer", "Engineering")
        emp_file.write_employee("E102", "Priya Patel", "QA Lead", "Testing")
        emp_file.write_employee("E103", "Rohan Verma", "HR Manager", "Human Resources")

    print("--- 2. Verifying File Closure After Error ---")
    try:
        with managed_employee_file(file_path, mode="a") as emp_file:
            emp_file.write_employee("E104", "Ananya Sen", "DevOps Engineer", "Infrastructure")
            # Simulating a unexpected system crash mid-operation
            raise RuntimeError("Database synchronization failed!")
    except RuntimeError:
        print("Caught exception safely outside the 'with' block.")

    # Clean up generated test file
    if os.path.exists(file_path):
        os.remove(file_path)