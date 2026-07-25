class ManagedResource:
    def __enter__(self):
        print("Resource acquired.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource released.")
        
        if exc_type is not None:
            print(f"Handled error inside __exit__: {exc_val}")
            
        # Return True to SUPPRESS the error from propagating outside
        # Return False (or None) to let the error RE-RAISE normally
        return False

# Usage without error
with ManagedResource():
    print("Executing work...")

print("---")

# Usage with error
try:
    with ManagedResource():
        raise ValueError("Something went wrong!")
except ValueError:
    print("Error caught outside 'with' block!")