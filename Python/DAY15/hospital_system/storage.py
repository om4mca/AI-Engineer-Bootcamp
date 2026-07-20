"""Handles JSON file persistence and exception-safe I/O operations."""

import json
import os
from typing import Dict, List
# Change from:
# from .exceptions import InvalidDataError

# To this:
from exceptions import InvalidDataError

class StorageHandler:
    """Manages file storage, serialization, and deserialization."""
    def __init__(self, filepath: str = "patients_db.json"):
        self.filepath = filepath

    def load_all(self) -> List[dict]:
        """Loads records from the JSON file into memory."""
        if not os.path.exists(self.filepath):
            return []
        
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            raise InvalidDataError(f"File '{self.filepath}' contains corrupted or non-JSON data.")
        except IOError as e:
            raise InvalidDataError(f"Failed to read file storage: {str(e)}")

    def save_all(self, records: List[dict]) -> None:
        """Writes all records safely to the persistent JSON storage."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(records, file, indent=4)
        except IOError as e:
            raise InvalidDataError(f"Failed to write to file storage: {str(e)}")