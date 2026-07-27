import functools
import time

def log_execution_time(func):
    """Decorator to time function execution."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"⏱️ [{func.__name__}] completed in {duration:.4f}s")
        return result
    return wrapper

def retry(times=3, delay=0.1, exceptions=(Exception,)):
    """Decorator to retry failing operations."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"⚠️ Attempt {attempt}/{times} failed: {e}")
                    if attempt == times:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator