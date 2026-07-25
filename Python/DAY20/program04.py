class CustomResource:
    def __enter__(self):
        print("1. [__enter__] Acquiring resource setup...")
        # Whatever is returned here becomes the 'as' variable
        return "Connected Handle"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("3. [__exit__] Cleaning up resource...")
        return False

# Usage
with CustomResource() as handle:
    print(f"2. [Inside Block] Working with: {handle}")