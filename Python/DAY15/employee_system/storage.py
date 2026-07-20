"""File persistence handler for saving and loading employee records."""

import json
import os
from typing import List, Dict
from exceptions import InvalidInputError

class StorageHandler:
    def __init__(self, filepath: str = "employees_db.json"):
        self.filepath = filepath

    def load_records(self) -> List[dict]:
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            raise InvalidInputError(f"Database file '{self.filepath}' is corrupted.")
        except IOError as e:
            raise InvalidInputError(f"File system error: {str(e)}")

    def save_records(self, records: List[dict]) -> None:
        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(records, file, indent=4)
        except IOError as e:
            raise InvalidInputError(f"Failed to write to database: {str(e)}")