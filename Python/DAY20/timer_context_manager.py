import time
from contextlib import contextmanager

@contextmanager
def execution_timer(name: str = "Block"):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"[{name}] Executed in {elapsed:.6f} seconds")

# Usage
with execution_timer("Heavy Calculation"):
    result = sum(i ** 2 for i in range(1_000_000))