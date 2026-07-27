import json
from contextlib import contextmanager
from exceptions import DataStorageError

@contextmanager
def safe_file_handler(filepath, mode):
    """Context Manager for safe file operations."""
    file = None
    try:
        file = open(filepath, mode, encoding="utf-8")
        yield file
    except OSError as e:
        raise DataStorageError(f"System file error on '{filepath}': {e}")
    finally:
        if file:
            file.close()

class FileManager:
    """Handles JSON serialization and deserialization."""
    def __init__(self, filename="employees_data.json"):
        self.filename = filename

    def save_employees(self, employee_dict):
        data = [emp.to_dict() for emp in employee_dict.values()]
        with safe_file_handler(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_employees(self):
        try:
            with safe_file_handler(self.filename, "r") as f:
                return json.load(f)
        except DataStorageError:
            return []  # Return empty collection if file does not exist