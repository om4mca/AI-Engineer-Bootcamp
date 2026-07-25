import time
from contextlib import contextmanager

@contextmanager
def timer(label: str):
    start = time.perf_counter()
    print(f"[{label}] Starting...")
    try:
        # Pass control back to the 'with' block
        yield
    finally:
        # Guaranteed execution even if the 'with' block crashes
        elapsed = time.perf_counter() - start
        print(f"[{label}] Finished in {elapsed:.4f} seconds")

# Usage
with timer("Data Processing"):
    total = sum(i ** 2 for i in range(1_000_000))