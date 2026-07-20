#--------------------------------------------
# AI Engineer Bootcamp
# Day 15
# Program: Validator
# Author: Om Roy
# Date: 20-07-2026
#--------------------------------------------

# validator.py

class Validator:
    @staticmethod
    def validate_positive_number(value: str) -> float:
        """Ensures input is a valid number greater than zero."""
        try:
            num = float(value)
            if num <= 0:
                raise ValueError("Value must be greater than zero.")
            return num
        except ValueError as e:
            raise ValueError(f"Invalid numeric input: {e}")

    @staticmethod
    def validate_non_empty_string(value: str, field_name: str) -> str:
        """Ensures string input is not blank or whitespace."""
        cleaned = value.strip()
        if not cleaned:
            raise ValueError(f"Field '{field_name}' cannot be empty.")
        return cleaned


# Example Usage:
if __name__ == "__main__":
    try:
        user_age = Validator.validate_positive_number("25")
        user_name = Validator.validate_non_empty_string("  Alice ", "Name")
        print(f"✅ Validated: {user_name}, Age: {user_age}")
    except ValueError as err:
        print(f"🛑 Validation Error: {err}")