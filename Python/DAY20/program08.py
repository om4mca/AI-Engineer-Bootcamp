from contextlib import contextmanager

@contextmanager
def managed_resource():
    # 1. Setup phase (__enter__)
    print("Acquiring resource...")
    resource = "Database Connection"
    
    try:
        # 2. Hand control to the 'with' block
        yield resource
    finally:
        # 3. Teardown phase (__exit__)
        print("Cleaning up resource...")

# Usage
with managed_resource() as res:
    print(f"Working with: {res}")