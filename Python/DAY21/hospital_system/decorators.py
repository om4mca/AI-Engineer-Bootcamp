import functools
import logging

# Logger Setup
logging.basicConfig(
    filename="hospital_operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_operation(action_name):
    """Decorator to log operations and handle runtime errors."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logging.info(f"Starting operation: {action_name}")
                result = func(*args, **kwargs)
                logging.info(f"Successfully completed: {action_name}")
                return result
            except Exception as e:
                logging.error(f"Error in {action_name}: {str(e)}")
                print(f"\n❌ Error ({action_name}): {str(e)}")
        return wrapper
    return decorator