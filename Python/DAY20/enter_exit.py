class TraceManager:
    def __enter__(self):
        print("1. Entering context: setting up resources...")
        # Whatever is returned here is bound to the `as` variable
        return "Resource Handle"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("2. Exiting context: cleaning up resources...")
        
        # If an error occurred inside the block:
        if exc_type is not None:
            print(f"   -> Caught Exception Type: {exc_type.__name__}")
            print(f"   -> Error Details: {exc_val}")
            
            # Returning True SUPPRESSES the error so execution continues.
            # Returning False (or None) RE-RAISES the error.
            return True 

# Usage
with TraceManager() as resource:
    print(f"   -> Inside block using: {resource}")
    # Uncommenting below triggers exception handling in __exit__:
    # raise ValueError("Something went wrong!")

print("3. Code outside the block continues running.")