import os
from contextlib import contextmanager


@contextmanager
def employee_file(filename: str, mode: str = "w"):
    """Context Manager to safely handle employee file operations."""
    print(f"Opening file '{filename}' in mode '{mode}'...")
    file = open(filename, mode)
    
    try:
        yield file
    except IOError as e:
        print(f"File Error Handled: {e}")
        raise
    except Exception as e:
        print(f"Unexpected Error Handled: {e}")
        raise
    finally:
        file.close()
        print(f"Employee file '{filename}' closed safely.")


# ==========================================
# Usage & Closure Verification
# ==========================================
if __name__ == "__main__":
    file_path = "employees.txt"

    print("--- 1. Writing Employee Data ---")
    with employee_file(file_path, "w") as file:
        file.write("101, Om, Developer\n")
        file.write("102, Rahul, Tester\n")
        print("Employee records written successfully.")

    # Verification: Check if file closed
    print(f"\nVerification -> Is file closed? {file.closed}")

    print("\n--- 2. Reading Employee Data Back ---")
    with employee_file(file_path, "r") as file:
        content = file.read()
        print("File Contents:\n" + content.strip())

    print("\n--- 3. Testing Error Handling & Cleanup ---")
    try:
        with employee_file(file_path, "a") as file:
            file.write("103, Ananya, Manager\n")
            # Simulating an error during writing
            raise RuntimeError("Database sync failed while updating file!")
    except RuntimeError as err:
        print(f"Caught outside block: {err}")

    # Double check that the file closed even after a runtime crash
    print(f"Verification after error -> Is file closed? {file.closed}")

    # Clean up generated test file
    if os.path.exists(file_path):
        os.remove(file_path)