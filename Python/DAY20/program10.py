import sqlite3

class DatabaseResource:
    """Context Manager for managing a database connection resource."""
    
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None

    def __enter__(self) -> sqlite3.Cursor:
        print(f"--> [ALLOCATE] Opening connection to '{self.db_name}'...")
        self.connection = sqlite3.connect(self.db_name)
        # Return a cursor object to work with inside the 'with' block
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type:
                print(f"--> [ERROR DETECTED] Rolling back transaction: {exc_val}")
                self.connection.rollback()
            else:
                print("--> [SUCCESS] Committing transaction...")
                self.connection.commit()
            
            print("--> [RELEASE] Closing database connection...")
            self.connection.close()
        
        # Return False so any unhandled exception bubbles up normally
        return False


# Usage
try:
    with DatabaseResource(":memory:") as cursor:
        cursor.execute("CREATE TABLE users (id INT, name TEXT)")
        cursor.execute("INSERT INTO users VALUES (1, 'Aarav')")
        print("    Inside block: Data inserted into memory DB.")
except Exception as err:
        print(f"Caught error outside: {err}")