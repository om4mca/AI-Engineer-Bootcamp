import json
from contextlib import contextmanager
from exceptions import DataStorageError

@contextmanager
def safe_file_handler(filepath, mode):
    """Custom Context Manager for safe file I/O."""
    file = None
    try:
        file = open(filepath, mode, encoding="utf-8")
        yield file
    except OSError as e:
        raise DataStorageError(f"File system error on '{filepath}': {e}")
    finally:
        if file:
            file.close()

class FileManager:
    """Handles Saving and Loading Patient Data to File."""
    def __init__(self, filename="patients_data.json"):
        self.filename = filename

    def save_patients(self, patients_dict):
        # Convert objects to dictionary list
        data_to_save = [p.to_dict() for p in patients_dict.values()]
        with safe_file_handler(self.filename, "w") as f:
            json.dump(data_to_save, f, indent=4)

    def load_patients(self):
        try:
            with safe_file_handler(self.filename, "r") as f:
                return json.load(f)
        except DataStorageError:
            return []  # Return empty if file doesn't exist yet