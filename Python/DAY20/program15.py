import time
from contextlib import contextmanager

@contextmanager
def timer(label: str = "Task"):
    """Measures and logs elapsed time for a block of code."""
    start_time = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start_time
        print(f"[{label}] Elapsed time: {elapsed:.4f} seconds")

# Usage
with timer("Patient Search Query"):
    time.sleep(0.12)  # Simulating database query delay