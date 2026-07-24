#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: Timing + Logging Combined Decorator
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------

import logging
import time
from functools import wraps

# Setup clean, standard logger format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("AuditLogger")


def log_and_time(func):
    """Combined decorator that logs execution details, parameters, timing, and errors."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Format arguments cleanly
        args_str = ", ".join(map(repr, args))
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        params = ", ".join(filter(None, [args_str, kwargs_str]))
        
        logger.info(f"▶ START: '{func.__name__}' called with ({params})")
        
        # 2. Start high-precision timer
        start_time = time.perf_counter()
        
        try:
            # 3. Execute target function
            result = func(*args, **kwargs)
            
            # 4. Calculate duration
            duration_ms = (time.perf_counter() - start_time) * 1000
            
            logger.info(
                f"✅ END  : '{func.__name__}' returned {result!r} "
                f"[{duration_ms:.2f} ms]"
            )
            return result

        except Exception as error:
            # 5. Log failure and duration before re-raising error
            duration_ms = (time.perf_counter() - start_time) * 1000
            logger.error(
                f"❌ FAIL : '{func.__name__}' failed with {type(error).__name__}: {error} "
                f"[{duration_ms:.2f} ms]"
            )
            raise  # Re-raise so program control isn't broken
            
    return wrapper


# --- Example Usage ---

@log_and_time
def fetch_user_data(user_id, include_orders=False):
    """Simulates fetching user data from a database."""
    time.sleep(0.08)  # Simulate small delay
    return {"user_id": user_id, "name": "Om Prakash", "orders": 5 if include_orders else 0}


@log_and_time
def process_payout(account_id, amount):
    """Simulates processing a financial transaction."""
    time.sleep(0.02)
    if amount <= 0:
        raise ValueError("Payout amount must be greater than 0")
    return f"TXN_SUCCESS_{account_id}"


# --- Execution ---

print("=== 1. Successful Execution ===")
user_info = fetch_user_data(104, include_orders=True)

print("\n=== 2. Exception Scenario ===")
try:
    process_payout(8801, amount=-500)
except ValueError:
    pass