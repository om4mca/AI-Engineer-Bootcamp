import functools
import logging

# Feature 10: Logging Setup (logs stored in employee_operations.log)
logging.basicConfig(
    filename="employee_operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_operation(action_name):
    """Decorator to log operation start/success and catch runtime errors."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logging.info(f"Initiated: {action_name}")
                result = func(*args, **kwargs)
                logging.info(f"Completed: {action_name}")
                return result
            except Exception as e:
                logging.error(f"Failed [{action_name}]: {str(e)}")
                print(f"\n❌ Error in {action_name}: {str(e)}")
        return wrapper
    return decorator