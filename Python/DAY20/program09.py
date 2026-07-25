from contextlib import contextmanager

@contextmanager
def db_transaction():
    print("1. [Setup] Opening connection & starting transaction...")
    conn = "Database Connection Handle"
    
    try:
        yield conn  # Execution pauses here! Control moves to 'with' block.
    finally:
        print("3. [Teardown] Resuming after yield: Committing & closing DB...")

# Usage
with db_transaction() as db:
    print(f"2. [Inside 'with'] Executing SQL query using: {db}")