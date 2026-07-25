from contextlib import contextmanager

@contextmanager
def temporary_setup():
    print("1. Setup phase (Runs before block)")
    try:
        yield "Active Resource"  # Value bound to the 'as' variable
    finally:
        print("2. Cleanup phase (Guaranteed to run)")

# Usage
with temporary_setup() as res:
    print(f"   Working with: {res}")